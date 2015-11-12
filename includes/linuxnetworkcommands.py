import os,sys



class class_linuxnetworktools:

	class_header = 'Linux Network Commands'

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
		self.toolslist.append(    ('Network Active Connections', 
																'watch', 
																['ss', '-tp'],
																[],
																[],
																False,
																True,#except 
																True) ) #Needs root
		self.toolslist.append(    ('TCP Connection', 
																'watch netstat', 
																['-ant'],
																[],
																[], 
																False, 
																True ,#except 
																True) ) #Needs root
		self.toolslist.append(    ('UDP Connection', 
																'watch netstat', 
																['-anu'],
																[],
																[], 
																False, 
																True ,#except 
																True) ) #Needs root
		self.toolslist.append(    ('Established Connection', 'watch lsof', ['-i'],[],[], False, True ,#except 
																True) ) #Needs root
		self.toolslist.append(    ('SMB Connect', 'smbclient -U <Username> \\\\IP\\Share', [],  [],   [], True, False ,#except 
																True) ) #Needs root
		self.toolslist.append(    ('Mount Windows Share', 
																'mount -t cifs -o username=<share user>,password=<share password> //WIN_PC_IP/<share name> /mnt', 
																[],  
																[],
																[], 
																False, 
																False ,#except 
																True) ) #Needs root
		self.toolslist.append(    ('Set Ip And Netmask', 
																'ifconfig %1 %2/%3',  #Tool
																[], #parameters
																[], #user parameters
																[ ('Interface', '%1'), ('Ip', '%2'),  ('Mask', '%3'),], #REplacement parameters
																False, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Create virtual Interface', 
																'ifconfig %1:%4 %2/%3',  #Tool
																[], #parameters
																[], #user parameters
																[ ('Interface', '%1'), ('Ip', '%2'),  ('Mask', '%3'), ('Virtual Interface number', '%4')], #REplacement parameters
																False, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Set default Gateway', 
																'route add default gw %1',  #Tool
																[], #parameters
																[], #user parameters
																[ ('Gateway Ip', '%1')], #REplacement parameters
																False, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Change MAC Address (env vars)', 
																'export MAC=%1',  #Tool
																[], #parameters
																[], #user parameters
																[ ('New Mac Address', '%1')], #REplacement parameters
																False, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Change MAC Address (ifconfig)', 
																'ifconfig %1 hw ether %2',  #Tool
																[], #parameters
																[], #user parameters
																[ ('Interface', '%1'), ('New Mac Address', '%2')], #REplacement parameters
																False, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Built-in Wifi Scanner', 
																'iwlist %1 scan',  #Tool
																[], #parameters
																[], #user parameters
																[ ('Interface', '%1')], #REplacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Domain Lookup for IP (DIG)', 
																'dig -x %1',  #Tool
																[], #parameters
																[], #user parameters
																[ ('Ip', '%1')], #REplacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Domain Lookup for IP - generic', 
																'host %1',  #Tool
																[], #parameters
																[], #user parameters
																[ ('Ip', '%1')], #REplacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Add Hidden Interface', 
																'ip addr add ip %1/%2 dev eth0',  #Tool
																[], #parameters
																[], #user parameters
																[ ('Ip', '%1'), ('Mask', '%2' )  ], #REplacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Turn on/off IP Forwarding', 
																'echo "%1" > /proc/sys/net/ipv4/ip_forward',  #Tool
																[], #parameters
																[], #user parameters
																[ ('On=1, Off=0', '%1')], #REplacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Add DNS Server', 
																'echo "nameserver %1" >> /etc/resolve.conf',  #Tool
																[], #parameters
																[], #user parameters
																[ ('Ip', '%1')], #Replacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
	
