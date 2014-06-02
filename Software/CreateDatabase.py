#Create Database Module
#Mufaro Simbisayi

def create():
	#Create Database Connection
	import sqlite3;

	dataCon = sqlite3.connect('SEProj.db');
	conCursor = dataCon.cursor();

	#Create Table
	conCursor.execute('''Create Table if Not Exists People (Key text, First_Name text, Last_Name text)''');
	
	dataCon.commit();
	conCursor.close();
