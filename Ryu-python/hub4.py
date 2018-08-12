from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.packet import packet,ethernet

class hub(app_manager.RyuApp):
	OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

	def __init__(self, *args, **kwargs):
		super(hub,self).__init__(*args, **kwargs)
	
	@set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
	def _packet_in_handler(self, ev):
		msg = ev.msg
		dp = msg.datapath
		# src = eth.src
		ofproto = dp.ofproto
		switch = dp.id
		data = msg.data

		if switch == 1:
			match2 = dp.ofproto_parser.OFPMatch(in_port=2)
			actions2 = [dp.ofproto_parser.OFPActionOutput(1)]
			mod2 = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match2,cookie=0,
				command=ofproto.OFPFC_ADD,idle_timeout=5,hard_timeout=5,priority=10,
				flags=ofproto.OFPFF_SEND_FLOW_REM,actions=actions2)
			dp.send_msg(mod2)

			match1 = dp.ofproto_parser.OFPMatch(in_port=1)
			actions1 = [dp.ofproto_parser.OFPActionOutput(2)]
			mod1 = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match1,cookie=0,
				command=ofproto.OFPFC_ADD,idle_timeout=5,hard_timeout=5,priority=10,
				flags=ofproto.OFPFF_SEND_FLOW_REM,actions=actions1)
			dp.send_msg(mod1)

		elif switch == 2:
			match2 = dp.ofproto_parser.OFPMatch(in_port=2)
			actions2 = [dp.ofproto_parser.OFPActionOutput(1)]
			mod2 = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match2,cookie=0,
				command=ofproto.OFPFC_ADD,idle_timeout=5,hard_timeout=5,priority=10,
				flags=ofproto.OFPFF_SEND_FLOW_REM,actions=actions2)
			dp.send_msg(mod2)

			match1 = dp.ofproto_parser.OFPMatch(in_port=1)
			actions1 = [dp.ofproto_parser.OFPActionOutput(2)]
			mod1 = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match1,cookie=0,
				command=ofproto.OFPFC_ADD,idle_timeout=5,hard_timeout=5,priority=10,
				flags=ofproto.OFPFF_SEND_FLOW_REM,actions=actions1)
			dp.send_msg(mod1)

		    