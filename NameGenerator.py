import random,string


letter_input1=input('Choose the Letter1,"v"for Vowels,"c"for consonants,"z"for any other letters:')
letter_input2=input('Choose the Letter2,"v"for Vowels,"c"for consonants,"z"for any other letters:')
letter_input3=input('Choose the Letter3,"v"for Vowels,"c"for consonants,"z"for any other letters:')
letter_input4=input('Choose the Letter4,"v"for Vowels,"c"for consonants,"z"for any other letters:')
letter_input5=input('Choose the Letter5,"v"for Vowels,"c"for consonants,"z"for any other letters:')

vowels='aeiou'
consonants='bcdfghjklmnpqrstvwxyz'
letters=string.ascii_lowercase

def name():


   if letter_input1 == "v":
       print(random.choice(vowels))
   elif letter_input1 =="c":
       print(random.choice(consonants))
   elif letter_input1 =="z":
       print(random.choice(letters))
   else:
        print(letter_input1)

   if letter_input2 == "v":
       print(random.choice(vowels))
   elif letter_input2 == "c":
       print(random.choice(consonants))
   elif letter_input2 == "z":
       print(random.choice(letters))
   else:
       print(letter_input2)

   if letter_input3 == "v":
       print(random.choice(vowels))
   elif letter_input3 == "c":
       print(random.choice(consonants))
   elif letter_input3 == "z":
       print(random.choice(letters))
   else:
       print(letter_input3)

   if letter_input4 == "v":
       print(random.choice(vowels))
   elif letter_input4 == "c":
       print(random.choice(consonants))
   elif letter_input4 == "z":
       print(random.choice(letters))
   else:
       print(letter_input4)

   if letter_input5 == "v":
       print(random.choice(vowels))
   elif letter_input5 == "c":
       print(random.choice(consonants))
   elif letter_input5 == "z":
       print(random.choice(letters))
   else:
        print(letter_input5)
   generator = letter_input1+letter_input2+letter_input3+letter_input4+letter_input5
   return (generator)

for babynames in range(20):
    print(name())



