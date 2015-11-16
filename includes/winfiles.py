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
																'echo " \
\n Windows 10                             10.0* \
\n Windows Server 2016 Technical Preview  10.0* \
\n Windows 8.1                            6.3* \
\n Windows Server 2012 R2                 6.3* \
\n Windows 8                              6.2 \
\n Windows Server 2012                    6.2 \
\n Windows 7                              6.1 \
\n Windows Server 2008 R2                 6.1 \
\n Windows Server 2008                    6.0 \
\n Windows Vista                          6.0 \
\n Windows Server 2003 R2                 5.2 \
\n Windows Server 2003                    5.2 \
\n Windows XP 64-Bit Edition              5.2 \
\n Windows XP                             5.1 \
\n Windows 2000                           5.0 \
																"',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																False) ) #Needs root
