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


win = False

while win == False:

    checks = []

    guess = input("What is your guess? ")

    for x,y in enumerate(guess):
        if y != computer_number[x] and y in computer_number:
            checks.append("close")
        elif y == computer_number[x] and guess != computer_number:
            checks.append("match")
        elif guess == computer_number:
            win = True
            print("Congrats! You guessed correctly!")
            break
        else:
            checks.append("nope")

    if "close" in checks and "match" not in checks:
        print("You've guessed a correct number but in the wrong position!")
    elif "match" in checks and "close" not in checks:
        print("You've guessed a correct number in the correct position!")
    elif "match" in checks and "close" in checks:
        print("You've guessed a correct number in the correct position and a correct number but in the wrong position!")
    elif checks == ['nope', 'nope', 'nope']:
        print("You haven't guess any of the numbers correctly!")

# if guess == computer_number:
#     print("Correct!")
# else:
#     print("Nope.")
#
# def compare_numbers(a, b):


# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
