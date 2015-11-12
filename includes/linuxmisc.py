import os,sys

class class_linuxmisc():

	class_header = 'Linux Miscelaneous'

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
		self.toolslist.append(    ('Disable History Logging', #description
																'unset HISTFILE',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Record Remote MIC', #description
																'ssh %1@%2 arecord - | aplay -',  #Tool
																[], #parameters
																[], #user parameters
																[('Remote ssh user name ', '%1'),('Remote Host', '%2') ], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('List of log files', #description
																'cat /etc/*syslog*.conf | grep -v "^#"',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
