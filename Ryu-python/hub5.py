from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib import mac
from ryu.lib.packet import packet,ethernet

class hub(app_manager.RyuApp):
	OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

	def __init__(self, *args, **kwargs):
		super(hub,self).__init__(*args, **kwargs)
		self.sat = {}
	
	@set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
	def _packet_in_handler(self, ev):
		msg = ev.msg
		dp = msg.datapath
		# src = eth.src
		ofproto = dp.ofproto
		data = msg.data

		pkt = packet.Packet(msg.data)
		eth = pkt.get_protocol(ethernet.ethernet)
		src = eth.src
		dst = eth.dst
		switch = dp.id

		self.sat.setdefault(switch,{})

		self.sat[switch][src] = msg.in_port

		if dst in self.sat[switch]:
			if dst != src:
				output = self.sat[switch][dst]
		else:
			output = ofproto.OFPP_FLOOD

		actions = [dp.ofproto_parser.OFPActionOutput(output)]
		out = dp.ofproto_parser.OFPPacketOut(datapath=dp, buffer_id=msg.buffer_id, 
			in_port=msg.in_port, actions=actions)
		dp.send_msg(out)

		if output != ofproto.OFPP_FLOOD:
			self.addflow(dp,msg.in_port,actions,dst)


	def addflow(self,dp,in_port,actions,dst):
		ofproto = dp.ofproto
		match = dp.ofproto_parser.OFPMatch(in_port=in_port, dl_dst=mac.haddr_to_bin(dst))
		mod = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match,priority=ofproto.OFP_DEFAULT_PRIORITY,actions=actions)
		dp.send_msg(mod)