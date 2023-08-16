# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
#test_str = "alternating caps" 
question = input("what is your honest opinion?")
sarcastic_answer = ""
count = 0
for char in question:
    count+=1
    if count % 2 == 0:
        sarcastic_answer += char.lower()
    else:
        sarcastic_answer += char.upper()
print(sarcastic_answer)
#res = ""
#for i in range(len(test_str)):
#    if not i % 2:
#        res = res + test_str[i].upper()
#    else:
#        res = res + test_str[i].lower()
#print("The original string is : " + str(test_str))
#print("The result is : " + str(res))
