import os
import random
import string
linesCreated = 900000;


#Create
file = open('test.txt','w');
file.truncate();

key = random.sample(range(100000,1000000), linesCreated);

#Write
for i in range(linesCreated):
	random_string1 = '';
	random_string2 = '';
	for i2 in range(16):
		random_string1 += random.choice(string.ascii_letters);
		random_string2 += random.choice(string.ascii_letters);

	file.write(str(key[i]) + ',' + str(random_string1) + ' ' + str(random_string2) + os.linesep);

file.close();