# print ("Hello World")
from random import randrange
magic_number = randrange(1,11)
print(magic_number)
guess = ''
while True:
    guess = int(input('Try to guess the number\nInsert the number here: '))
    if guess < magic_number:
        print('Nope, number is higher')
        continue
    elif guess > magic_number:
        print('Nope, number is lower')
        continue
    elif guess == magic_number:
        print("Correct! You won a piece of cake!")
        break
    else:
        print('Invalid number or character')