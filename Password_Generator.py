#PASSWORD GENERATOR
from numpy import random

set_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
set_upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
set_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
set_symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '/', '?']

random.shuffle(set_alphabet)
random.shuffle(set_upper_alphabet)
random.shuffle(set_number)
random.shuffle(set_symbol)

user_input1 = input("How long they want their password to be?. Minimum 6 characters: ")
print("The password is", user_input1, "characters long")

user_input_alphabet = input("How many letters you want in your password? ")
user_input_upper_alphabet = input("How many upper letters you want in your password? ")
user_input_number = input("How many digits you want in your password? ")
user_input_symbol = input("How many symbols you want in your password? ")

password = set_alphabet[0:int(user_input_alphabet)] + set_upper_alphabet[0:int(user_input_upper_alphabet)] + set_number[0:int(user_input_number)] + set_symbol[0:int(user_input_symbol)]
random.shuffle(password)
strPassword = ''.join(password)
print(strPassword)