import random
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER,CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3,ether
from ryu.lib import mac
from ryu.lib.packet import packet,ethernet,arp,ipv4,tcp,ether_types

class loadBalancer(app_manager.RyuApp):
	OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

	def __init__(self, *args, **kwargs):
		super(loadBalancer,self).__init__(*args, **kwargs)
		self.mac_to_port = {}
		self.serverlist = []
		self.virtual_lb_ip = "10.0.0.100"
		self.virtual_lb_mac = "AB:BC:CD:EF:AB:BC"
		self.serverlist.append({'ip': "10.0.0.1", 'mac': "02:b4:db:b6:41:a5","outport": "1"})
		self.serverlist.append({'ip': "10.0.0.2", 'mac': "7a:15:74:aa:92:68", "outport": "2"})
		self.serverlist.append({'ip': "10.0.0.3", 'mac': "de:6f:ab:ea:e1:b4", "outport": "3"})
		self.req = 0
		self.requestnumber = 0

	def function_for_arp_reply(self, dst_ip,dst_mac):
		arp_target_mac = dst_mac # Menjadikan IP dan MAC virtual LB sebagai IP Src dan MAC dari #ARP reply
		src_ip = self.virtual_lb_ip
		src_mac = self.virtual_lb_mac
		arp_opcode = 2 # ARP opcode (Operationcode)2 untuk ARP reply
		hardware_type = 1 # 1 = Ethernet ie 10Mb
		arp_protocol = 2048 # 2048 = IPv4 packet
		ether_protocol = 2054 # 2054 = ARP protocol
		len_of_mac = 6 # length of MAC in bytes
		len_of_ip = 4 # length of IP in bytes
		pkt = packet.Packet()
		ether_frame = ethernet.ethernet(dst_mac, src_mac, ether_protocol) # Dealing with only layer 2
		arp_reply_pkt = arp.arp(hardware_type, arp_protocol, len_of_mac, len_of_ip,arp_opcode, src_mac, src_ip,arp_target_mac, dst_ip) # Building the ARP reply packet, 
		pkt.add_protocol(ether_frame)
		pkt.add_protocol(arp_reply_pkt)
		pkt.serialize()
		return pkt
	
	def inisialisasiUrutan():
		#ukuran = len(self.serverlist)
		index = 0
		daftarServer = []
		for i in self.serverlist:
			daftarServer.append(index) 	
			index += 1
		return daftarServer
	
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
		eth = pkt.get_protocols(ethernet.ethernet)[0]
		in_port = msg.match['in_port']

		if eth.ethertype == ether_types.ETH_TYPE_LLDP:
			return

		if eth.ethertype == ether.ETH_TYPE_ARP:
			arp_header = pkt.get_protocols(arp.arp)[0]
			if arp_header.dst_ip == self.virtual_lb_ip and arp_header.opcode == arp.ARP_REQUEST:
				reply_pkt = self.function_for_arp_reply(arp_header.src_ip,arp_header.src_mac)
				actions = [parser.OFPActionOutput(in_port)]
				packet_out = parser.OFPPacketOut(datapath=dp,in_port=ofproto.OFPP_ANY,data=reply_pkt.data,actions=actions,buffer_id=0xffffffff)
				dp.send_msg(packet_out)
				return

		ip_header = pkt.get_protocols(ipv4.ipv4)[0]
		tcp_header = pkt.get_protocols(tcp.tcp)[0]
		match = parser.OFPMatch(in_port=in_port, eth_type=eth.ethertype,eth_src=eth.src, eth_dst=eth.dst,ip_proto=ip_header.proto,ipv4_src=ip_header.src, ipv4_dst=ip_header.dst,tcp_src=tcp_header.src_port,tcp_dst=tcp_header.dst_port)

		#algoritma RR
		#server = self.req % 3
		if self.req < len(self.serverlist):
			server = self.req
			self.req += 1
		else:
			self.req = 0
			server = self.req
		self.requestnumber +=1
		print("request {} , server index {}".format(self.requestnumber,server))
		server_mac_selected = self.serverlist[server]['mac']
		server_ip_selected = self.serverlist[server]['ip']
		server_outport_selected = int(self.serverlist[server]['outport'])
		
		actions = [parser.OFPActionSetField(ipv4_src=self.virtual_lb_ip),parser.OFPActionSetField(eth_src=self.virtual_lb_mac),
		parser.OFPActionSetField(eth_dst=server_mac_selected),parser.OFPActionSetField(ipv4_dst=server_ip_selected),
		parser.OFPActionOutput(server_outport_selected)]

		inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
		cookie = random.randint(0, 0xffffffffffffffff)
		flow_mod = parser.OFPFlowMod(datapath=dp, match=match, idle_timeout=7, instructions=inst,buffer_id=msg.buffer_id, cookie=cookie)
		dp.send_msg(flow_mod)

		match = parser.OFPMatch(in_port=server_outport_selected, eth_type=eth.ethertype, eth_src=server_mac_selected,
			eth_dst=self.virtual_lb_mac, ip_proto=ip_header.proto, ipv4_src=server_ip_selected,
			ipv4_dst=self.virtual_lb_ip, tcp_src=tcp_header.dst_port, tcp_dst=tcp_header.src_port)
		actions = [parser.OFPActionSetField(eth_src=self.virtual_lb_mac),parser.OFPActionSetField(ipv4_src=self.virtual_lb_ip),parser.OFPActionSetField(ipv4_dst=ip_header.src), parser.OFPActionSetField(eth_dst=eth.src),parser.OFPActionOutput(in_port)]
		inst2 = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
		cookie = random.randint(0, 0xffffffffffffffff)
		flow_mod2 = parser.OFPFlowMod(datapath=dp, match=match, idle_timeout=7, instructions=inst2, cookie=cookie)
		dp.send_msg(flow_mod2)

	def addflow(self,dp,priority,match,actions,buffer_id=None):
		ofproto = dp.ofproto
		parser = dp.ofproto_parser
		inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,actions)]
		if buffer_id: 
			mod = dp.ofproto_parser.OFPFlowMod(datapath=dp,buffer_id=buffer_id,match=match,priority=priority,instructions=inst)
		else:
			mod = dp.ofproto_parser.OFPFlowMod(datapath=dp,match=match,priority=priority,instructions=inst)
		dp.send_msg(mod)
