# Name: Hunter
# Date: 6/12/2017


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
user_input = int(raw_input("Guess a number, one through nine!: "))
#user_input2 = raw_input("Ding ding ding!!! You guessed right! ")
#user_input3 = raw_input("Gotta guess a little higher than that! Try again: ")
#user_input4 = raw_input("Guess lower next time! Try again: ")

import random
var = random.randint(1, 9)
print user_input

guess = 3
while guess > 0:
    guess -= 1
    if guess == 0:
        print "You failed :<("
        break

    if user_input == var:
        print "Home Run! You win!!"#user_input2
        break

    if user_input > var:
        print "Airball! Too high!"#user_input3

    if user_input < var:
        print "Nothing but dirt! Too low!"#user_input4
    user_input = int(raw_input("Guess a number, one through nine!: "))

print "The correct answer is..."
print var

