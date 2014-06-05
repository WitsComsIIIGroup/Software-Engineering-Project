#Read Data from Database
#David Torpey

def readData():
	
	#Database Conect	
	import sqlite3;

	dataCon = sqlite3.connect('SEProj.db');
	conCursor = dataCon.cursor();	
	
	#Extract Content
	table = conCursor.execute("Select * from People")
	
	#Create Arrays
	key =[];
	firstName = [];
	lastName = [];

	#Fill Arrays	
	for record in table:
		key.append(record[0]);		
		firstName.append(record[1]);
		lastName.append(record[2]);

	#Print Unsorted content
	print("First 15 and Last 15 Unsorted Names");
	if len(key) >= 15:
		for i in range(15):
			print (key[i] + ": " + lastName[i] + " " + firstName[i]);
		
		print ("*****************************************************");
		
		for i in range(len(key)-15, len(key)):
			print (key[i] + ": " + lastName[i] + " " + firstName[i]);
	
	else:
		for i in range(len(key)):
			print (key[i] + ": " + lastName[i] + " " + firstName[i]);

	return [key, firstName, lastName];
