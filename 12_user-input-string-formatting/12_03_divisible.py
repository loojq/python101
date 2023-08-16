# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

math_question = int(input("give me a number from 1 to 1 bil: "))
if math_question % 3 == 0:
    print("it is divisible by 3!")
else:
    print("it is not divisible by 3")
