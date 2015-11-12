#Framework for running tools

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

#Tool example
import os

class Tool_framework():
	class_header = None
	toolslist = None
	advancemode = False

	def __init__(self, toolslist, class_header):
		self.toolslist = toolslist
		self.class_header = (class_header).ljust(50) + 'Execute | Root'

	def tools_count(self):
		return len(self.toolslist)

	def list_tools(self):
		for ix, tool in enumerate(self.toolslist):
			if ix+1 > 9:
				spaces = 1
			else:
				spaces = 2

			printparams = ''
			#check if the tool is executable
			if tool[6]:
				printparams = printparams + '  yes'.ljust(8) + '|'
			else:
				printparams = printparams + '  no'.ljust(8)+ '|'  
					
			if tool[7]:
				printparams = printparams + ' yes'
			else:
				printparams = printparams + ' no'
			
				
			print (' '*2 +  str(ix+1) + '.' + ' '*spaces + tool[0]).ljust(52)  + printparams
		print ' '
		print ' '*2 + 'x.  ' + 'Exit' 

	def run_tool(self, ix):
		params = " ".join(self.toolslist[ix][2])
		command = self.toolslist[ix][1]
		questions = self.toolslist[ix][3]
		replacements = self.toolslist[ix][4]
		addWait = self.toolslist[ix][5]
		execute = self.toolslist[ix][6]
		needRoot = self.toolslist[ix][7] 			

		os.system('clear')
		for num, obj in enumerate(questions):
			question, parameter = obj
			answ = raw_input(' '*2 + question+': ')
			params = params + ' ' + parameter + ' ' + answ

		for num, obj in enumerate(replacements):
			question, replacewith = obj
			answ = raw_input(' '*2 + question+': ')
			command = command.replace(replacewith, answ)

		print " "
		try:
			if self.advancemode:
				execute = True

			if execute:
				print self.toolslist[ix][0]
				if needRoot:
					os.system(' sudo ' + command + ' ' + params)
				else:
					os.system(' ' + command + ' ' + params)
			else:
				print 'This command may cause damage to your computer and will not be executed.'
				raw_input("You can run the following command: " + command + ' ' + params)
			print " "
		except Exception, e:
			print e.message

		if addWait:
			raw_input('Press any key to continue...')

	def tool_count(self):
		val = len(self.toolslist)
		return val


	def run_menu(self, mainheader):
		selection = ''
		while selection != 'x':
			os.system('clear')
			print self.class_header
			print mainheader
			print ' '*2 + self.class_header
			print ' '*2 + '='*len(self.class_header)
			self.list_tools()
			print ''
			selection = raw_input('Run tool #: ')
			try:
				selection = int(selection)-1
				if selection < 0:
					continue;
	
				if self.tool_count() >= int(selection):
					self.run_tool(selection)
				
			except Exception, e:
				#print e.message
				pass



