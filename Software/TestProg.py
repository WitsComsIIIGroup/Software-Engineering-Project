#TestProg Module
#Python 2.7
# Group effort, constructed by all members.

#Import Modules
import CreateDatabase
import ReadIn
import DataStore
import ReadDatabase
import Sort
import OutputFile
import os
import CheckFormat
import TerminalPrint

#Link Database
CreateDatabase.create();

#Extract Content from File
inputFileDir = raw_input("Please enter the input .txt file directory and file name:")

try:
        fileInput = open(inputFileDir, 'r');
except Exception as e:
        print "Could not find file " + inputFileDir
        print "Please ensure that your input file is in the directory you specified and restart the application."
        os._exit(0);
try:
        contentArray = ReadIn.readIn(fileInput);
except Exception as e:
        os._exit(0);
fileInput.close;

#Split into Arrays

key = contentArray[0];
fullName = contentArray[1];

firstName =[];
lastName =[];

for entry in fullName:
        splitNames = entry.split(' ');  
        firstName.append(splitNames[1]);
        lastName.append(splitNames[0]);

#Store Content in Database
DataStore.store(key, firstName, lastName);

#Read from database
extContent = ReadDatabase.readData();

key = extContent[0];
firstName = extContent[1];
lastName = extContent[2];

#Display1st 15 and last 15 raw entries
print "1st and last 15 entries (Unsorted)"

if len(key) >= 15:
    for i in range(15):
        print (key[i] + ":" + firstName[i] + " " + lastName[i]);
		
        print ("*****************************************************");
		
        for i in range(len(key)-15,len(key)):
            print (key[i] + ":" + firstName[i] + " " + lastName[i]);

else:
    for i in range(len(key)):
        print (key[i] + ":" + firstName[i] + " " + lastName[i]);


#Sort
sortArray = [];

for j in range(0, len(key) - 1):
        sortArray.append(key[j] + "," + firstName[j] + " " + lastName[j]);

correctFlag = False
flag = raw_input("How would you like to sort the data (ASC, DESC):");
        
if (flag == "ASC") or (flag == "DESC") or (flag == "asc") or (flag == "desc"):
        correctFlag = True

if (correctFlag == False):
        print("Incorrect sort flag. Please type in only ASC or DESC");
        print("Please restart application and try again.");
        os._exit(0);

sortedArray = Sort.quickSort(sortArray, flag);

#Split Content
del key[:];
del firstName[:];
del lastName[:];

for line in sortedArray:
        splitVals = line.split(',');
        key.append(splitVals[0]);
        
        nameSplit = splitVals[1].split(' ');
        firstName.append(nameSplit[0]);
        lastName.append(nameSplit[1]);

#OutputFile
outputFileDir = 'Files/lab3Output.txt'
OutputFile.writeFile(key, firstName, lastName, outputFileDir);

#PrintOutFile
TerminalPrint.PrintOutFile();
