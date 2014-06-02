#Data Store Module
#Donovan Platt

#Import Modules
import sqlite3;
import sys;
import os;

#Create Database Connection
dataCon = sqlite3.connect('SEProj.db');
conCursor = dataCon.cursor();	

def store(key, firstName, lastName):
	
	conCursor.execute("Delete from People");

	#Store Data
	for i in range(0, len(key) - 1):
		sKey = key[i];
		sFirst = firstName[i];
		sLast = lastName[i];
                checkKey(sKey);
		
		conCursor.execute("Insert into People Values (?, ?, ?)", (sKey, sFirst, sLast));
	
	dataCon.commit();
	conCursor.close();

#Check for duplicate keys
def checkKey(sKey):
	table = conCursor.execute("Select * from People")
	
	#Create Arrays
	key = [];
	for record in table:
		if (record[0] == sKey):
			print "Duplicate keys detected in text file. Please ensure that all keys are unique."
			print "Duplicate key is: " + sKey;
			os._exit(0)
		 		
		
	
