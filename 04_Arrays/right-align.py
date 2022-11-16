def get_left_aligned_strs(strings):
    """Function generates and returns list of left-aligned words"""
    
    print("Enter strings (end with DONE):")
    print()
    string = ""
    while string != 'DONE': #sentinel loop to list words
        string = input( )
        strings.append(string)
    strings.remove("DONE")
    return strings

def get_longest_string_length(word_list):
    """Function returns the integer length of the longest string in list"""
    longest_word = 0
    for word_pos in range(len(word_list)):
        new_word = len(word_list[word_pos])
        prev_longest = longest_word
        if new_word > prev_longest:
            longest_word = new_word
        else:
            longest_word = prev_longest
    return longest_word

def main():
    strings=[]
    gen_list = get_left_aligned_strs(strings)
    length = get_longest_string_length(gen_list)
    print("Right-aligned list:")
    for string in gen_list:
        if len(string) < length:
            num_spaces = length-len(string)
            print(" "*num_spaces + string)
        else:
            print(string)
    print()

if __name__ == '__main__':
    main()
        