# Program searches text file for words that match a given pattern
# Bonga Njamela
# 23/06/20

import simplematch

#def find_start(filename, liner):
#    """Function takes in a file and returns TRUE if line contains 'START'""" 
#    countlines = 0
#    for lines in filename:
#        countlines += 1
#        if liner == lines:
#            for words in lines.split():
#                if words == 'START':
#                    return countlines


asterix = '*'
print(asterix*5, "Word Search", asterix*5)        
    
try:
    userFile = input("Enter the name of the words file:\n")
    myFile = open(userFile, 'r')
    pattern = input("Enter a search pattern:\n")
    matchList = []
    start = False    
    for line in myFile:
        if line.count('START') > 0:
            start = True
        words = line[:line.find("\n")]
        if line.count('\n') == 0:
            words = line
        if start:
            match = False
            if words != 'START':
                if len(pattern) == len(words):
                    match = simplematch.match(pattern, words)
                if pattern == words:
                    match = True
                if match:
                    matchList.append(words)
        
    if len(matchList) != 0:
        print(matchList)
    else:
        print("Sorry, matches for", "'{}'".format(pattern), "could not be found.")
except IOError as erTxt:
    print("Sorry, could not find file", "'{}'".format(userFile)+'.')
finally:
    print(end='')
