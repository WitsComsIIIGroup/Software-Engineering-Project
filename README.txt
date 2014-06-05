Python Student Database Program Version 1.0.0 24/05/2014

CONTENT:

-Description
-General Usage
-Documentation
-Libraries
-Installation
-Running the product
-Running Tests
-General Notes
---------------------------------------------------------------
GIT CLONE

This project is available via an online GIT repository.

From terminal execute the following command:
git clone https://github.com/WitsComsIIIGroup/Software-Engineering-Project.git

This will clone the repository into the directory you are currently in.
---------------------------------------------------------------

DESCRIPTION:

This software processes data from an input text file consisting 
of key/value pairs where the value is the fullname of a student 
corresponding to the key, and a six-digit integer number. It 
accesses the file of records and sorts the data based on a flag 
(ASC,DESC), which represent ascending or descending sorting. It
then displays the first 15 and the last 15 key/value pairs of
the sorted data. The input data is also stored in a database,
using the SQLite DBMS.

---------------------------------------------------------------

GENERAL USAGE:

- The software only supports common operating systems such as Windows
  and Unix-based systems (e.g. Linux and Mac OS). There is
  no support for Windows NT Server or other similar platforms.

- The software may be stored anywhere on disk.

- There is no installation wizard procedure for this software.

----------------------------------------------------------------

DOCUMENTATION:

The documentation for this product is available in PDF format. It 
details the design and implementation of this software and the 
requirements that led to its development.

----------------------------------------------------------------

LIBRARIES:

The following special Libraries are used

-sys
-os

----------------------------------------------------------------

INSTALLING ON WINDOWS OR UNIX-BASED SYSTEMS:

When installing Python Student Database Program version
1.0.0 on any of the aforementioned supported operating systems,
merely store the program in the desired folder on disk. Extract
the folder if you have it in .zip format.

----------------------------------------------------------------

RUNNING THE SOFTWARE (Linux systems):

Be advised that there is no graphical user interface/user 
interface for this software. The program runs solely through
the command line/terminal of your system.

To run the software, open the command line/terminal on your
system, change you current working directory to that of where
the program is stored. Then, run the following command:

python TestProg.py
 
An alternative method of program execution is to use the Python
IDLE. You will need Python version 2.0 or later to do this. 
Open the IDLE, open TestProg.py and press F5 on your keyboard.

Both methods will result (assuming there are no errors in your
input text file) in a prompt to input the sort flag (ASC or DESC)
which allows the user to choose whether to sort the data in 
ascending or descending order respectively.

-------------------------------------------------------------

RUNNING TESTS:

Please see section 3 of the software document.

--------------------------------------------------------------

GENERAL NOTES:

- There is no copyright on this software. No rights will be 
  reserved for the software itself or the source code thereof.
  python Student Database Program version 1.0 and its use
  are not subject to licence agreement.

- No rolling support will be provided for the software.

- python Student Database Program version 1.0 is open-source
  freeware.
---------------------------------------------------------------

SOFTWARE DEVELOPERS:

- Jeroen Schmidt
- Donovan Platt
- Mufaro Simbisayi
- David Torpey