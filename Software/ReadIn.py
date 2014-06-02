#ReadIn Module
#Donovan Platt

#Import Modules
import CheckFormat
import os

#Declare Arrays	
key = [];
fullName = [];

def readIn(fileInput):
	
	#Extract Content from File
	lineNumber = 0	

	for line in fileInput:
		lineNumber += 1;
		line = CheckFormat.checkFormat(line, lineNumber);
		
		key.append(line.split(',')[0].rstrip());
		fullName.append(line.split(',')[1].rstrip());
			
	return [key, fullName];


