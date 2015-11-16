import os,sys

class class_winsysteminfo():

	class_header = 'Windows System Info'

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
		self.toolslist.append(    ('Get OS Version', #description
																'ver',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																False) ) #Needs root
		self.toolslist.append(    ('Show Services Information', #description
																'sc quer',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																False) ) #Needs root
		self.toolslist.append(    ('Show runing services', #description
																'tasklist /svc',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																False) ) #Needs root
		self.toolslist.append(    ('Show tasks and loaded modules', #description
																'tasklist /m',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																False) ) #Needs root
		self.toolslist.append(    ('Show running processes', #description
																'tasklist',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																False) ) #Needs root
		self.toolslist.append(    ('Kill Running process by PID', #description
																'taskkill /PID %1 /F',  #Tool
																[], #parameters
																[], #user parameters
																[('PID','%1')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																False) ) #Needs root
		self.toolslist.append(    ('Show complete system info and Hotfixes', #description
																'systeminfo',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																False) ) #Needs root
		self.toolslist.append(    ('Search Registry for keywords', #description
																'reg query HKLM /f %1 /t REG_SZ /s',  #Tool
																[], #parameters
																[], #user parameters
																[('Keyword (eg assword)','%1')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																False) ) #Needs root
		self.toolslist.append(    ('List drives', #description
																'fsutil fsinfo drives',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																False) ) #Needs root
		self.toolslist.append(    ('Search for all files with an extension', #description
																'dir /a /s /b %1:\*.%2',  #Tool
																[], #parameters
																[], #user parameters
																[('Drive letter (eg C,D,E)','%1'),('Extension (eg pdf,xls,doc)','%2')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																False) ) #Needs root
		self.toolslist.append(    ('Search for  all patches', #description
																'dir /a /s /b %1:\*.%2',  #Tool
																[], #parameters
																[], #user parameters
																[('Drive letter (eg C,D,E)','%1'),('Extension (eg pdf,xls,doc)','%2')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																False) ) #Needs root
