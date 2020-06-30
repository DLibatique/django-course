###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
# print(digits[:3])
computer_number = ''
for i in digits[:3]:
    computer_number += str(i)
print(computer_number)

# Another hint:
guess = input("What is your guess? ")

win = False

while win == False:

    for x in guess:
        if guess[guess.index(x)] != computer_number[guess.index(x)] and x in computer_number:
            guess = input("You guessed a correct number in the wrong position! Guess another number! ")
        elif guess[guess.index(x)] == computer_number[guess.index(x)] and guess != computer_number:
            guess = input("You guessed a correct number in the right position! Guess another number! ")
        elif guess == computer_number:
            win = True
        else:
            guess = input("No matches! Guess another number! ")


# if guess == computer_number:
#     print("Correct!")
# else:
#     print("Nope.")
#
# def compare_numbers(a, b):


# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
