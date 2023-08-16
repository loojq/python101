# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

name = input("please enter your name: ")
#print(f"welcome {name}")
for index,word in enumerate(name.split()):
    if index == 0:
        name = word
        print(f"Welcome {name}")