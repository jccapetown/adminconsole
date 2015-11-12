import os,sys

class class_linuxstartupservices():

	class_header = 'Startup Services (Update-RC.D)'

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
		self.toolslist.append(    ('Service Startup Status', #description
																'service --status-all',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Start a Service', #description
																'service %1 start',  #Tool
																[], #parameters
																[], #user parameters
																[('Service name', '%1')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Stop a Service', #description
																'service %1 stop',  #Tool
																[], #parameters
																[], #user parameters
																[('Service name', '%1')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Get a Service\'s status', #description
																'service %1 status',  #Tool
																[], #parameters
																[], #user parameters
																[('Service name', '%1')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
