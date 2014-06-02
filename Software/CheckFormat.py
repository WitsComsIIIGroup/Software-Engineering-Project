#Import Modules
#Jeroen Schmidt

import re
import os

#Check that Text File is of Correct Format
def checkFormat(line, lineNumber):
        line = line.rstrip();
	matchObj = re.match('\d{6}[,][ ][a-zA-Z]{2,25}[ ][a-zA-Z]{2,25}[ ]{0,25}$', line.strip(os.linesep), re.M|re.I)
			
	if matchObj:
	  	return line
	else:
		print "Text File contains line(s) of incorrect format"		
		print "Incorrect format on line " + str(lineNumber)
		print "Please check that the lines in the file match the format specified in the README."
		os._exit();
	
