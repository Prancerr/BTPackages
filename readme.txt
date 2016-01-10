PACKFINDER
Python Program for finding direct and transitive dependencies from a text file

Requirements:
The program requires Python 2.7 to run

Running:
To run program in the command line:

python PackFinder.py packages.txt

this will return the dependencies from packages.txt in the format:

swingui -> extensions framework runner
awtui -> framework runner

packages.txt is a text file containing the direct dependency information.  This file MUST be in the format:

gui -> awtui swingui
swingui -> runner extensions
textui -> runner framework
awtui -> runner

Any other format wil terminate the program.

By default the program searches for packages.txt in the working directory, but this can changed (eg. replace with /a/folder/packages.txt).

To output the dependencies of set packages, add them to the command line when running:

python PackFinder.py packages.txt swingui 

will output the dependencies of swingui. Multiple packages can be added in one command.  
