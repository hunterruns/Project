# Name: Hunter
# Date: 6/12/2017

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

user_input = int(raw_input("Enter a number: "))

prevnum = 0
fibnum = 1

#while user_input > 0:
    #print user_input
    #print fibnum
    #newnum = prevnum + fibnum
    #prevnum = fibnum
    #fibnum = newnum
    #user_input -= 1

for number in range(user_input):
    print fibnum
    newnum = prevnum + fibnum
    prevnum = fibnum
    fibnum = newnum

