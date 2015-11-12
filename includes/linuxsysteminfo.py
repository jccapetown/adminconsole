import os,sys

class class_linuxsysteminfo:

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
		self.toolslist.append(    ('Current username', #description
																'id',  #Tool
																[], #parameters
																[], #user parameters
																[ ], #Replacement parameters
																True, #allow continue
																True,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Logged on users', #description
																'w',  #Tool
																[], #parameters
																[], #user parameters
																[ ], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('User Information', #description
																'who -a',  #Tool
																[], #parameters
																[], #user parameters
																[ ], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Last users logged on', #description
																'last -a',  #Tool
																[], #parameters
																[], #user parameters
																[ ], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Show top processes', #description
																'ps -ef',  #Tool
																[], #parameters
																[], #user parameters
																[ ], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Disk usage - free', #description
																'df -h',  #Tool
																[], #parameters
																[], #user parameters
																[ ], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Kernel version / CPU info', #description
																'uname -a',  #Tool
																[], #parameters
																[], #user parameters
																[ ], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Mounted file system', #description
																'mount',  #Tool
																[], #parameters
																[], #user parameters
																[ ], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Show list of users', #description
																'getent passwd',  #Tool
																[], #parameters
																[], #user parameters
																[ ], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Show list of groups', #description
																'getent group',  #Tool
																[], #parameters
																[], #user parameters
																[ ], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Show shadow file', #description
																'getent shadow',  #Tool
																[], #parameters
																[], #user parameters
																[ ], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Show port services', #description
																'getent services',  #Tool
																[], #parameters
																[], #user parameters
																[ ], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Kill Process with <pid>', #description
																'kill %1',  #Tool
																[], #parameters
																[], #user parameters
																[ ('Process id', '%1')], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Show OS info', #description
																'cat /etc/*release*',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Show OS info', #description
																'cat /etc/*release*',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Kernel version', #description
																'cat /proc/version',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Installed Packages (RPM)', #description
																'rpm -ivh *.rpm',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
		self.toolslist.append(    ('Show location of executable', #description
																'which %1 ',  #Tool
																[], #parameters
																[], #user parameters
																[('Executalbe name', '%1')], #Replacement parameters
																True, #allow continue
																True,#execute 
																True ))	#execute
	
	

