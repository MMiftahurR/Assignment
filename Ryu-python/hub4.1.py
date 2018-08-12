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

		pkt = packet.Packet(msg.data)
		eth = pkt.get_protocol(ethernet.ethernet)
		dst = eth.dst

		if switch == 1:
			if dst == '01:00:00:00:00:00/01:00:00:00:00:00':
				match = dp.ofproto_parser.OFPMatch(eth_dst=dst)
				actions1 = [dp.ofproto_parser.OFPActionOutput(ofproto.OFPP_ALL)]
				mod = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match,cookie=0,
					command=ofproto.OFPFC_ADD,idle_timeout=0.1,hard_timeout=0.2,priority=15,
					flags=ofproto.OFPFF_SEND_FLOW_REM,actions=actions1)
				dp.send_msg(mod)
			elif dst == 'a6:a0:04:50:0d:b5':
				match2 = dp.ofproto_parser.OFPMatch(eth_dst=dst)
				actions2 = [dp.ofproto_parser.OFPActionOutput(1)]
				mod2 = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match2,cookie=0,
					command=ofproto.OFPFC_ADD,idle_timeout=5,hard_timeout=5,priority=10,
					flags=ofproto.OFPFF_SEND_FLOW_REM,actions=actions2)
				dp.send_msg(mod2)
			elif dst == '92:ad:41:aa:bc:66':
				match2 = dp.ofproto_parser.OFPMatch(eth_dst=dst)
				actions2 = [dp.ofproto_parser.OFPActionOutput(2)]
				mod2 = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match2,cookie=0,
					command=ofproto.OFPFC_ADD,idle_timeout=5,hard_timeout=5,priority=10,
					flags=ofproto.OFPFF_SEND_FLOW_REM,actions=actions2)
				dp.send_msg(mod2)

		elif switch == 2:
			if dst == '01:00:00:00:00:00/01:00:00:00:00:00':
				match = dp.ofproto_parser.OFPMatch(eth_dst=dst)
				actions1 = [dp.ofproto_parser.OFPActionOutput(ofproto.OFPP_ALL)]
				mod = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match,cookie=0,
					command=ofproto.OFPFC_ADD,idle_timeout=0.1,hard_timeout=0.2,priority=15,
					flags=ofproto.OFPFF_SEND_FLOW_REM,actions=actions1)
				dp.send_msg(mod)
			elif dst == '92:ad:41:aa:bc:66':
				match2 = dp.ofproto_parser.OFPMatch(eth_dst=dst)
				actions2 = [dp.ofproto_parser.OFPActionOutput(1)]
				mod2 = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match2,cookie=0,
					command=ofproto.OFPFC_ADD,idle_timeout=5,hard_timeout=5,priority=10,
					flags=ofproto.OFPFF_SEND_FLOW_REM,actions=actions2)
				dp.send_msg(mod2)
			elif dst == 'a6:a0:04:50:0d:b5':
				match2 = dp.ofproto_parser.OFPMatch(eth_dst=dst)
				actions2 = [dp.ofproto_parser.OFPActionOutput(2)]
				mod2 = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match2,cookie=0,
					command=ofproto.OFPFC_ADD,idle_timeout=5,hard_timeout=5,priority=10,
					flags=ofproto.OFPFF_SEND_FLOW_REM,actions=actions2)
				dp.send_msg(mod2)

		    