#Resources Used
#https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
#https://stackoverflow.com/questions/6473283/basic-python-file-io-variables-with-enumerate
#https://www.w3schools.com/python/ref_set_add.asp
#

def grep(pattern, flags, files):
    flaglist = flags.split()
    results = []
    matchingFiles = set() #initialize matching file tracker

    for file in files: #iterate through files

        f = open(file, 'r') #open and read in file
        lines = f.readlines() 

        for lineNum, line in enumerate(lines): #iterate through file lines
            if '-i' in flaglist: #flag for case-insensitive comparison
                newPat = pattern.lower()
                newLine = line.lower()
            else: #newPat and newLine needed to retain original line case-sensitivity for output
                newPat = pattern
                newLine = line

            if newPat in newLine:
                matchingFiles.add(file) #adds unique file name to matchingFiles list

                if '-l' in flaglist: #flag for only printing names of files
                    results.append(f"{file}\n")
                    break #if a match is found, we go on to next file

                elif '-n' in flaglist: #flag for including line number
                    results.append(f"{file}:{lineNum+1}:{line}")
                
                else: #default 
                    results.append(f"{file}:{line}")
        f.close()
    #currently not working in this commit, getting index out of range error
    #if len(matchingFiles) < 2 and '-l' not in flaglist: #when there are not multiple files with matching patterns, we remove the file name prefix
    #    results = line.split(':', maxsplit=1)[1]
    #raise Exception(results)
    return ''.join(results)
