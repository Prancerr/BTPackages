import sys

#Function to skip blank lines when reading file
def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line
           

#Function prints  dependencies of package 'argpack' for command line dependencies            
def outputpack(argpack, packs, depends):
    if argpack in packs:
        position = packs.index(argpack) #Find its position within the list
        print "%s ->" %packs[position], 
        for i in range (0,len(depends[position])):
            print depends[position][i],
    else:
        print "%s ->" %argpack #If no dependencies, just print package 


#Imports text file information
def readfile(filelist, packs, depends):
    for line in nonblank_lines(open(filelist)):
        if "->" not in line: #If an invalid line, terminate program
            sys.exit("Error: Invalid input file")
        line = line.strip('\n')
        splitline = line.split(" -> ") #Split into package and dependencies
        packs.append(splitline[0]) #First element is package
        splitdep = splitline[1].split() #Second element split into individual dependencies
        depends.append(splitdep) #Add to depends list            


#Finds all packs and depends, adds to lists
def finddepend(packs, depends):
    olddepend = []
    while(olddepend != depends): #Keep iterating until no changes made
        olddepend = [x[:] for x in depends] #Copy of matrix at start of iteration to compare
        for pack in range (0,len(packs)): #Cycle through all packages
            for i in range (0,len(depends[pack])): #Cycle through dependencies within 'pack'
                workon = depends[pack][i] #Search for transitive dependencies of this dependency 
                for j in range (0,len(packs)):
                    if workon == packs[j]: #Add dependencies of 'workon'
                        for k in range (0,len(depends[j])): 
                            if depends[j][k] not in depends[pack] and depends[j][k] != packs[pack]:
                                depends[pack].append(depends[j][k]) #If not repeat or package itself, add to list of dependencies   
                                     



packs = [] 
depends = [] #Seperate lists for packages and dependencies 

readfile("%s" %sys.argv[1], packs, depends)
finddepend(packs, depends)
                    
for i in range (0,len(packs)): #Sort dependencies alphabetically
    depends[i].sort()

if len(sys.argv) == 2: #If no packages in command line, print whole list
    for i in range (0,len(packs)):
        print "%s ->" %packs[i],
        for j in range (0,len(depends[i])):
            print depends[i][j],
        print 
        
elif len(sys.argv) > 2: #Else print command line packages          
    for i in range (2, len(sys.argv)):
        outputpack("%s" %sys.argv[i], packs, depends)
        print
        

    

    
    
    
    
      



    
    
