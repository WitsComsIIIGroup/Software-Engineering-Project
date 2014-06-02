#Create Output Text File
#Jeroen Schmidt

#Import Modules
import os

def writeFile(key, firstName, lastName, fileName):
	#Create
	try:
		file = open(fileName, 'w');
	except Exception as e:
		print "File could not be created."
		print "Application will now terminate."
		os._exit()
		
	file.truncate();

	#Write
	for i in range(len(key)):
		file.write(key[i] + ': ' + lastName[i] + ' ' + firstName[i] + os.linesep);

	file.close();
