# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.
question = input("type any sentence:")
vowels = "aeiou"
#number_of_a = ""
#number_of_e = ""
#number_of_i = ""
#number_of_o = ""
#number_of_u = ""
#vowel_count = ""
#for char in question:
#    if char in vowels:
#        vowel_count+=char 
##print(vowel_count)
#for char in vowel_count:
#    if char == "a":
#        number_of_a+=char
#    elif char == "e":
#        number_of_e+=char
#    elif char == "i":
#        number_of_i+=char
#    elif char == "o":
#        number_of_o+=char
#    elif char == "u":
#        number_of_u+=char
#print("number of a: ",int(len(number_of_a)))
#print("number of e: ",int(len(number_of_e)))
#print("number of i: ",int(len(number_of_i)))
#print("number of o: ",int(len(number_of_o)))
#print("number of u: ",int(len(number_of_u)))


for char in vowels:
    n = question.count(char)
    print(char,n)