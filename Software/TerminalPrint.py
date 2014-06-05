#ReadIn Module
#Mufaro Simbisayi

#Declare Arrays
def PrintOutFile():	
	key = [];
	fullName = [];
	
	lab3Output = open('Files/lab3Output.txt', 'r')

	for line in lab3Output:
		key.append(line.split(':')[0].strip("\n"));
		fullName.append(line.split(':')[1].strip("\n"));
	
	if len(key) >= 15:
		for i in range(15):
			print (key[i] + ":" + fullName[i]);
		
		print ("*****************************************************");
		
		for i in range(len(key)-15,len(key)):
			print (key[i] + ":" + fullName[i]);
	
	else:
		for i in range(len(key)):
			print (key[i] + ":" + fullName[i]);
