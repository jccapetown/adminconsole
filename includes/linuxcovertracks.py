import os,sys

class class_linuxcovertracks():

	class_header = 'Linux "Cover your Tracks"'

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
		self.toolslist.append(    ('clear auth.log', #description
																'echo "" > /var/log/auth.log',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Clear current user history', #description
																'echo "" > ~/.bash_history',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Clear current session', #description
																'history -c',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Set the history maximum lines to zero', #description
																'export HISTFILESIZE=0',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Set the history maximum commands to zero', #description
																'export HISTSIZE=0',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																False ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Kill current session', #description
																'kill -9 $$',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root

