def to_pig_latin(sentence):
    
  sep_word = sentence.split(" ")
  
  for word_pos in range(0, len(sep_word)): #accesses each word
    eng_word = sep_word[word_pos]
    for letter_pos in range(0, len(eng_word)-1): #access each alphabet in each word
      eng_letter = eng_word[letter_pos]
      if letter_pos == 0: #checks if first letter is vowl
        if ord(eng_letter) == 97:
          pig_word = eng_word + "way "
        elif ord(eng_letter) == 101:
          pig_word = eng_word + "way "  
        elif ord(eng_letter) == 105:
          pig_word = eng_word + "way "
        elif ord(eng_letter) == 111:
          pig_word = eng_word + "way "
        elif ord(eng_letter) == 117:
          pig_word = eng_word + "way "
        else:
          if ord(eng_word[letter_pos+1])!=97 and ord(eng_word[letter_pos+1])!=101 and ord(eng_word[letter_pos+1])!=105 and ord(eng_word[letter_pos+1])!=111 and ord(eng_word[letter_pos+1])!=117:
            two_cons = eng_word[:letter_pos+2]
            end_cons = "a" + two_cons + "ay "
            null_cons = eng_word[letter_pos+2:]
            pig_word = null_cons + end_cons
          else:  
            two_cons = eng_word[:letter_pos+1]
            end_cons = "a" + two_cons + "ay "
            null_cons = eng_word[letter_pos+1:]
            pig_word = null_cons + end_cons
    sep_word[word_pos] = pig_word
    pig_sentence = "".join(sep_word) 
  return pig_sentence 

def to_english(sentence):
  
  sep_latin = sentence.split(" ")
  
  for latin_pos in range(0, len(sep_latin)): #accesses each latin word
    pig_word = sep_latin[latin_pos]
    for way_pos in range(len(pig_word)-1, 0, -1): #search for w in each latin word
      pig_letter = pig_word[way_pos]
      if way_pos == (len(pig_word)-3): #checks if first letter is vowl
        if ord(pig_letter) == 119:
          eng_word = pig_word[:len(pig_word)-3] + " "
        else:
          minus_ay = pig_word[:len(pig_word)-2]
          if ord(minus_ay[len(minus_ay)-2:len(minus_ay)-1])==97:
            minus_cons_ay = minus_ay[:len(minus_ay)-2]
            eng_word = minus_ay[len(minus_ay)-1:len(minus_ay)]+minus_cons_ay+" "
          else:
            minus_cons_ay = minus_ay[:len(minus_ay)-3]
            eng_word = minus_ay[len(minus_ay)-2:len(minus_ay)]+minus_cons_ay+" "  
            
    sep_latin[latin_pos] = eng_word
    eng_sentence = "".join(sep_latin) 
  return eng_sentence 

