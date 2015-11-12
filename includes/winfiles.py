import os,sys

class class_winfiles():

	class_header = 'Windows Files'

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
		self.toolslist.append(    ('Windows Versions', #description
																'echo "\n NT 3.1        Windows NT 3.1 (ALL) test \
																\n NT 3.1        Windows NT 3.1 (ALL) test \
																\n NT 3.1        Windows NT 3.1 (ALL) test \
																\n NT 3.1        Windows NT 3.1 (ALL) test \
																"',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
