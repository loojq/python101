import random   

num = random.randint(1,10)
guess = int(input("any number from 1 to 10: "))
count_guesses = 0
flag_if_wrong = False

while flag_if_wrong == False:
    if 0<guess<11 and count_guesses<4:
        if guess == num:
            flag_if_wrong == True
            print("congrats! you got the right number!")
            break
        else:
            print("sorry try again")
            count_guesses +=1
            guess =int(input("any number from 1 to 10: "))
            print(guess)
    else:
        print("sorry, too many tries. game over")
        break