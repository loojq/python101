# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
file_ext = ""
flag = False
for index,char in enumerate(filename):
    if flag:
        print("now we start to add characters", char)
        file_ext += char
    if char == ".":
        print("now we turn the flag true",index)
        flag = True
    print ("we are in iteration number", index)
if file_ext == "pdf":
    print("SUCCESS")



#create a variable called extension, then append char after the dot 

    #print(type(char),char,index)

#number = 0
#for char in filename:
#    print(char,number)
#    number = number + 1
    

