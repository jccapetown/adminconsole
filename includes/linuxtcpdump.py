import os,sys

class class_linuxtcpdump():

	class_header = 'Linux IPTables'

	toolslist = []

	#Advancemode WILL execute everything
	advancemode = False


	def __init__(self):
		self.toolslist = []
		#Tool Setup
		#1. Tupple:
			#1.1 Description
			#1.2 Tool
			#1.3 Parameters [list]
			#1.4 user Inputs [list] of (Tuple )
				#1.4.1	Question 
				#1.4.2	Tool Parameter
			#1.5 Replacelist [list] of (tuples)
				#1.5.1 Question
				#1.5.2 Replace Variable eg. %1
			#1.6 allow user to "press continue"
			#1.7 Execute or print (Boolean): True=execute False=print
			
		#Tools
		self.toolslist.append(    ('Capture Packets to pcap file', #description
																'tcpdump -i %1 -XX -w %2',  #Tool
																[], #parameters
																[], #user parameters
																[('Interface', '%1'),('Output Filename', '%2')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Capture Packets for a port', #description
																'tcpdump -i %1 port %2',  #Tool
																[], #parameters
																[], #user parameters
																[('Interface', '%1'),('Port', '%2')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Capture Packets for a host', #description
																'tcpdump -i %1 host %2',  #Tool
																[], #parameters
																[], #user parameters
																[('Interface', '%1'),('Host', '%2')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Capture Packets for a host and port', #description
																'tcpdump -i %1 host %2 and port %3',  #Tool
																[], #parameters
																[], #user parameters
																[('Interface', '%1'),('Host', '%2'), ('Port','%3')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Show all connections to a host', #description
																'tcpdump -i %1 -tttt dst %2',  #Tool
																[], #parameters
																[], #user parameters
																[('Interface', '%1'),('Host', '%2')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Print all ping responses', #description
																'tcpdump -i %1 \'icmp[icmptype] == icmp-echoreply\'',  #Tool
																[], #parameters
																[], #user parameters
																[('Interface', '%1')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Capture 50 DNS packets with timestamps', #description
																'tcpdump -i %1 -c 50 -tttt \'udp and port 53\' ',  #Tool
																[], #parameters
																[], #user parameters
																[('Interface', '%1')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
