# Pattern matching module using recursion functions only
# Bonga Njamela
# 23/06/20

def match(pattern, word):
    """Recursive function returns true if patterns match and false otherwise""" 
    if len(pattern) != len(word): 
        return False
    if len(pattern) == 0 or len(word) == 0: 
        return False       
    #if pattern[pattern.find('?'):len(pattern)] == word[pattern.find('?'):len(word)]:
     #   return True
    if len(pattern) == 1 and len(word) == 1:
        if pattern == '?' or pattern == word:
            return True
    if pattern[0] == '?':
        if pattern[1] == word[1]:
            if ('?' in pattern) == False:
                return True
    if pattern[0] != '?':
        if pattern[0] != word[0]:
            return False
    if len(pattern) > 2 and pattern[-1] != word[-1] and pattern[-1] != '?':
        return False
    return match(pattern[1:len(pattern)], word[1:len(word)])