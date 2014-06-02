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

	return [key, firstName, lastName];
