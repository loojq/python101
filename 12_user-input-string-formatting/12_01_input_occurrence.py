# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4
string_input = input("write a word: ")
letter_input = input("what letter do you want to find in the word?: ")
for index, letter in enumerate(string_input):
    if letter == letter_input:
        print ("result: ",index)