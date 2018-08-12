from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER,CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib import mac
from ryu.lib.packet import packet,ethernet

class hub(app_manager.RyuApp):
	OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
	sat = {}

	def __init__(self, *args, **kwargs):
		super(hub,self).__init__(*args, **kwargs)

	@set_ev_cls(ofp_event.EventOFPSwitchFeatures,CONFIG_DISPATCHER)
	def _switch_features_handler(self,ev):
		msg = ev.msg
		dp = msg.datapath
		ofproto = dp.ofproto
		parser = dp.ofproto_parser

		match = parser.OFPMatch()
		actions =  [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER, ofproto.OFPCML_NO_BUFFER)]
		self.addflow(dp,0,match,actions)

	
	@set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
	def _packet_in_handler(self, ev):
		msg = ev.msg
		dp = msg.datapath
		ofproto = dp.ofproto
		parser = dp.ofproto_parser

		pkt = packet.Packet(msg.data)
		eth = pkt.get_protocol(ethernet.ethernet)
		src = eth.src
		dst = eth.dst
		switch = dp.id

		self.sat.setdefault(switch,{})

		self.sat[switch][src] = msg.match['in_port']

		if dst in self.sat[switch]:
			if dst != src:
				output = self.sat[switch][dst]
		else:
			output = ofproto.OFPP_FLOOD

		match = parser.OFPMatch(in_port=self.sat[switch][src],eth_src=src)

		actions = [dp.ofproto_parser.OFPActionOutput(output)]
		out = dp.ofproto_parser.OFPPacketOut(datapath=dp, buffer_id=msg.buffer_id, in_port=self.sat[switch][src], actions=actions)
		dp.send_msg(out)

		if output != ofproto.OFPP_FLOOD:
			self.addflow(dp,ofproto.OFP_DEFAULT_PRIORITY,match,actions)


	def addflow(self,dp,priority,match,actions):
		ofproto = dp.ofproto
		parser = dp.ofproto_parser
		inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,actions)] 
		mod = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match,priority=priority,instructions=inst)
		dp.send_msg(mod)