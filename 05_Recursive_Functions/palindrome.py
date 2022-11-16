# Program uses recursive function to calculate if a string is palindrome
# Bonga Njamela
# 22/06/20

def palindrome(string, gnirts):
    """This recursive function takes in a string and returns 1 if it is a
    palindrome and 0 if it is not a palindrome""" 
    
    if string == []: 
        return False     
    if string[0] == gnirts[-1] and string[1:2] == gnirts[len(gnirts)-2:len(gnirts)-1] and string[2:3] == gnirts[len(gnirts)-3:len(gnirts)-2]: 
        return True    
    else:
        return palindrome(string[:len(string)-1],string[1:])

def main():
    
    user_str = input("Enter a string:\n")
    user_str = user_str.lower()
    user_arr = list(user_str)
    
    if palindrome(user_arr, user_arr) == True:
        print("Palindrome!")
    else:
        print("Not a palindrome!")

main()
    