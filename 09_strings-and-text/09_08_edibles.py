# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
#More efficient way of indexing words
test = s.split()
my_list = ["They", "boo", "buttercups", "leggins"]
words_i_want = ""
for index,char in enumerate(test):
    #print(index,char)
    if char in my_list:
        words_i_want += char + " "
print(words_i_want)