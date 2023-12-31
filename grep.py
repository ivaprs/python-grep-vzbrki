#Resources Used
#https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
#https://stackoverflow.com/questions/6473283/basic-python-file-io-variables-with-enumerate
#https://www.w3schools.com/python/ref_string_join.asp

def grep(pattern, flags, files):
    flaglist = flags.split()
    results = []
    tempRes = []

    for file in files: #iterate through files

        f = open(file, 'r') #open and read file
        lines = f.readlines() 

        for lineNum, line in enumerate(lines): #iterate through file lines and retain line number


            if '-i' in flaglist: #flag for case-insensitive comparison
                newPat = pattern.lower()
                newLine = line.lower()
            else: #newPat and newLine added to retain original line case-sensitivity for output
                newPat = pattern
                newLine = line


            matchLine = 0 #default flag set to 0; when -x active and pattern doesn't match full line, flag is set to 1 and line is not added to results
            if '-x' in flaglist:
                if not newPat == newLine.strip():
                    matchLine = 1

            if (newPat in newLine and matchLine == 0) ^ ('-v' in flaglist): #checks for invert flag with XOR

                if '-l' in flaglist: #flag for only printing names of files; if a match is found, we go on to next file
                    results.append(f"{file}\n")
                    break 

                elif '-n' in flaglist: #flag for including line number
                    results.append(f"{file}:{lineNum+1}:{line}")
                
                else: #default 
                    results.append(f"{file}:{line}")
        f.close() #close file

    if len(files) < 2 and '-l' not in flaglist: #when there is only a single file and we aren't just printing file names ('-l' flag) we remove the file name prefix 
        for i in results:
            tempRes.append(i.split(':', 1)[1])
        results = tempRes


    return ''.join(results) 
