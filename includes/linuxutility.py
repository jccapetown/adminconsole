import os,sys

class class_linuxutility:

	class_header = 'Linux System Info'

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
		self.toolslist.append(    ('Remote desktop to <ip>', #description
																'rdesktop %1 ',  #Tool
																[], #parameters
																[], #user parameters
																[('Host Ip', '%1')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Add user', #description
																'useradd -m %1 ',  #Tool
																[], #parameters
																[], #user parameters
																[('Username', '%1')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Change user password', #description
																'passwd %1 ',  #Tool
																[], #parameters
																[], #user parameters
																[('Username', '%1')], #Replacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Remove user', #description
																'rmuser %1 ',  #Tool
																[], #parameters
																[], #user parameters
																[('Username', '%1')], #Replacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Record user shell', #description
																'script -a %1 ',  #Tool
																[], #parameters
																[], #user parameters
																[('Log filename', '%1')], #Replacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Find man pages containing <keyword>', #description
																'apropos %1 ',  #Tool
																[], #parameters
																[], #user parameters
																[('Keyword', '%1')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('View user command history', #description
																'cat /home/%1/.bash_history',  #Tool
																[], #parameters
																[], #user parameters
																[('Uername', '%1' )], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
	
	

