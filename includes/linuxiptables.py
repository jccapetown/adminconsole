import os,sys

class class_linuxiptables():

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
		self.toolslist.append(    ('Dump IPTables to file', #description
																'iptables-save -c %1',  #Tool
																[], #parameters
																[], #user parameters
																[('Filename', '%1')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Restore IPTables from file', #description
																'iptables-restore %1',  #Tool
																[], #parameters
																[], #user parameters
																[('Filename', '%1')], #Replacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('List all IPTable rules (numbered)', #description
																'iptables -L -v --line-numbers',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Allow outbound port from anywhere', #description
																'iptables -A OUTPUT -o %1 -p %2 --dport %3 -m state --state NEW,ESTABLISHED -j ACCEPT ',  #Tool
																[], #parameters
																[], #user parameters
																[('Interface', '%1'), ('Protocol (tcp or udp)','%2') , ('Dest. Port','%3') ], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Allow inbound port from anywhere', #description
																'iptables -A Input -o %1 -p %2 --dport %3 -m state --state NEW,ESTABLISHED -j ACCEPT ',  #Tool
																[], #parameters
																[], #user parameters
																[('Interface', '%1'), ('Protocol (tcp or udp)','%2') , ('Dest. Port','%3') ], #Replacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
