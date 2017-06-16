# Name: Hunter
# Date: 6/13/2017

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

user_input1 = raw_input("Enter a word, and I will tell you if it is a palindrome! : ")
print user_input1

reverse = reversed(user_input1)

stringList = []
for letter in user_input1:
    stringList.append(letter)

print stringList

print user_input1

while user_input1:

    if user_input1[0:-1] == user_input1[-1:0]:
        print "This word is a palindrome!"
        break
    else:
        print "This word is not a palindrome :4("
        break
