#RANDOM NUMBER GENERATOR
from numpy import random
rn = random.randint(0, 20)

#print(rn)
while 1:
    user_input = int(input("Enter guessed number: "))


    if user_input > rn:
        print("Nope, random number is lower, try again")
    elif user_input < rn:
        print("Nope, random number is higher, try again")
    else:
        print("Congrats, you guessed a number")
        break