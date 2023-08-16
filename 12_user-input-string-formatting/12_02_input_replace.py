# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

question = input ("phrase?: ")
symbol = input("what symbol pls?: ")
first_letter = ""
new_word = ""
first_letter = question[0]
for letter in question:
    if letter == first_letter:
        letter = symbol
    else:
        letter = letter 
    new_word +=letter
print(new_word)

