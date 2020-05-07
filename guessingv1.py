import random

# numbers 1-10 randint is INCLUSIVE (ranges are exclusive)
random_number = random.randint(1, 10)

# print(random_number)

guess = input("Pick a number from 1 to 10: ")  # now need to convert to int
guess = int(guess)

# if guess == random_number:
#     print("NAILED IT!")

while guess != random_number:
    guess = input("Pick a number from 1 to 10: ")  # now need to convert to int
    guess = int(guess)
    if guess > random_number:
        print("too high, sorry")
    elif guess < random_number:
        print("too low")
    else:
        print("NAILED IT!")

print(random_number)

# handle user guesses
# if they guess correctly, tell them they won
# otherwise tell them if they are too high or two low

# BONUS - let player play again if they want!

# If we don't know how long something will run for, a while loop is more ideal than a for loop.
