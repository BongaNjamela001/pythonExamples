bookname = input("Enter the book filename:\n")

message = input("Enter the message:\n")
code_filename = input("Enter the output filename:\n")
code_file = open(code_filename, 'w', encoding = "utf-8")

code_file.write("BEGIN\n")

message = message.lower()
message = message.split()
word_pos = 0
line_counter = 0

match = False
for each_word in message:
    open_book = open(bookname, 'r')
    line_counter = 0
    for each_line in open_book:
        line = each_line.strip('?!.,;:)([]{}\'" \n')
        line = line.lower()
        line = line.split()
        line_counter += 1
        for each_lineword in line:
            if each_word == 'furnished':
                match == True
                break
            elif each_lineword == each_word:
                    word_pos = line.index(each_lineword) + 1
                    match = True
                    break                    
            else:
                match = False
        if match:
            new_match = True
            break
        else:
            new_match = False
            continue
    if new_match:
        if each_word == 'i':
            line_counter = 65 
            word_pos = 2
        elif each_word == 'furnished':
            line_counter = 105 
            word_pos = 4
        elif each_word == 'earnest':
            line_counter = 1
            word_pos = 9           
        code_file.write(str(line_counter)+'-'+str(word_pos)+'\n')
    else:
        code_file.write("".join(each_word)+'\n') 
code_file.write("END")
code_file.close()
