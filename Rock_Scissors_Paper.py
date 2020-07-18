                              ###Rock, Paper, Scissors Game
from numpy import random

x = 0
win = 0
los = 0
while x < 3:
    computer_choice = ['rock', 'paper', 'scissors']
    random.shuffle(computer_choice)
    #print(computer_choice[0])


    user_input = str(input("Enter your choice: "))
    user_input = user_input.lower()
    #print(user_input)

    if user_input == 'rock' and computer_choice[0] == 'scissors':
        win = win + 1
        print("You have won. Score: ", win, ":", los)

    elif user_input == 'scissors' and computer_choice[0] == 'paper':
        win = win + 1
        print("You have won. Score: ", win, ":", los)

    elif user_input == 'paper' and computer_choice[0] == 'rock':
        win = win + 1
        print("You have won. Score: ", win, ":", los)

    elif user_input == computer_choice[0]:
        print("Draw")
    else:
        los = los + 1
        print("You have lost. Score: ", win, ":", los)
    x = x + 1
