from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet,ethernet

class hub(app_manager.RyuApp):
	OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

	def __init__(self, *args, **kwargs):
		super(hub,self).__init__(*args, **kwargs)

	@set_ev_cls(ofp_event.EventOFPSwitchFeatures,CONFIG_DISPATCHER)
	def switch_features_handler(self,ev):
		msg = ev.msg
		dp = msg.datapath
		ofproto = dp.ofproto
		parser = dp.ofproto_parser

		match = parser.OFPMatch()
		actions =  [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER, ofproto.OFPCML_NO_BUFFER)]
		self.addflow(dp,0,match,actions)
	
	@set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
	def packet_in_handler(self, ev):
		msg = ev.msg
		datapath = msg.datapath
		ofproto = datapath.ofproto
		data = msg.data
		parser = datapath.ofproto_parser

		pkt = packet.Packet(msg.data)
		eth = pkt.get_protocol(ethernet.ethernet)
		src = eth.src

		if src == '92:dc:73:f7:e5:f2' : 
			out_port=2
		else:
			out_port=1

		#actions = [datapath.ofproto_parser.OFPActionOutput(ofproto.OFPP_FLOOD)] (Flooding)
		match = parser.OFPMatch(in_port=msg.match['in_port'],eth_src=src)
		actions = [datapath.ofproto_parser.OFPActionOutput(out_port)]
		out = datapath.ofproto_parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,
		 in_port=msg.match['in_port'], actions=actions)
		datapath.send_msg(out)
		self.addflow(datapath,ofproto.OFP_DEFAULT_PRIORITY,match,actions)

	def addflow(self,dp,priority,match,actions):
		ofproto = dp.ofproto
		parser = dp.ofproto_parser
		inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,actions)] 
		mod = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match,priority=priority,instructions=inst)
		dp.send_msg(mod)