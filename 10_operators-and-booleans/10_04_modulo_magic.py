# Use the modulo operator to confirm which of the values
# shown below are divisible by seven.

num_1 = 42
num_2 = 137
num_3 = 455
num_4 = 1997
my_list = num_1,num_2,num_3,num_4
for number in my_list:
    if number%7 == 0:
        print(number, "is Divisible by 7!")
    else:
        print(number, "is not divisible by 7")
    