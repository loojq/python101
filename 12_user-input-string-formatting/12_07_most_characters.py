# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

question_1 = input("your first sentence: ")
question_2 = input("your second sentence: ")
question_3 = input("your third sentence: ")
if (max(len(question_1),len(question_2),len(question_3))) == len(question_1):
    print(len(question_1), question_1)
elif (max(len(question_1),len(question_2),len(question_3))) == len(question_2):
    print(len(question_2), question_2)
elif (max(len(question_1),len(question_2),len(question_3))) == len(question_3):
    print(len(question_3), question_3)