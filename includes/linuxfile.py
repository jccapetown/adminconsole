import os,sys

class class_linuxfile():

	class_header = 'Linux File Commands'

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
		self.toolslist.append(    ('Compare files', #description
																'diff %1 %2 ',  #Tool
																[], #parameters
																[], #user parameters
																[('File 1', '%1'), ('File 2', '%2') ], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Search for setuid files', #description
																'find / -perm 4000 -o -perm 2000 -exec ls -ldb {} \;',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																False) ) #Needs root
		self.toolslist.append(    ('Set immutable bit on file or folder', #description
																'chattr +i -R %1',  #Tool
																[], #parameters
																[], #user parameters
																[('Folder or file', '%1' )], #Replacement parameters
																True, #allow continue
																False ,#execute 
																False) ) #Needs root
		self.toolslist.append(    ('Unset immutable bit on file or folder', #description
																'chattr -i -R %1',  #Tool
																[], #parameters
																[], #user parameters
																[('Folder or file', '%1' )], #Replacement parameters
																True, #allow continue
																False ,#execute 
																False) ) #Needs root
		self.toolslist.append(    ('Shred a File', #description
																'shred -f -u %1',  #Tool
																[], #parameters
																[], #user parameters
																[('File', '%1' )], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Change Filestamp to match <file> timestamp', #description
																'touch -r %1 %2',  #Tool
																[], #parameters
																[], #user parameters
																[('File with wanted timestamp', '%1' ), ('File that needs to change', '%2')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Change Filestamp', #description
																'touch -t %1 %2',  #Tool
																[], #parameters
																[], #user parameters
																[('Timestamp (YYYYMMDDHHSS)', '%1' ), ('File to apply to', '%2')], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('List Connected Drives', #description
																'fdisk -l',  #Tool
																[], #parameters
																[], #user parameters
																[], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Compute md5 of a file', #description
																'md5sum -t %1',  #Tool
																[], #parameters
																[], #user parameters
																[ ('Filename','%1') ], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
		self.toolslist.append(    ('Compute md5 of a string', #description
																'echo -n "%1" | md5sum',  #Tool
																[], #parameters
																[], #user parameters
																[ ('String','%1') ], #Replacement parameters
																True, #allow continue
																True ,#execute 
																True) ) #Needs root
