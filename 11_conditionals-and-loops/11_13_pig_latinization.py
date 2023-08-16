# Fetch the text of the CodingNomads collaborative story from:
# https://raw.githubusercontent.com/CodingNomads/collaborative-story/master/story.txt
# Save it to a variable in this script and remember to use triple-double quotes
# for creating a multi-line string.
#
# Use a `for` loop to iterate over the story text
# and string slicing to translate it to ~pig latin.
# For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# You'll need to use conditional statements to decide when a word is over.
#
# For example: You would never guess --> ouyay ouldway evernay uessgay

first_line = """You would never guess""".lower()
translated_text = ""
for word in first_line.split():
    new_word = word[1:]+word[0]+"ay"+ " "
    translated_text += new_word    
print(translated_text)

#word = "hello"
#
#for char in word:
#    if char in "aeiou":
#        continue
#    print(char)
#
#print("done")