# Name: Hunter
# Date: 06/14/2017


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
word = choose_word(wordlist)
#word = "hello"
length = len(word)
guesses = 10
letters = 0
h = "_ "
letter_keeper = length * [h]
# your code begins here!
print "The length of this word is", length, "letters long."
while guesses > 0:
    l = raw_input("Please guess a letter: ")
    p_guess = guesses - 1
    print "you have", p_guess, "guesses left."

    check = False
    counter = 0
    for letter in word:

        if l == letter:
            letter_keeper[counter] = letter

            letters += 1
            check = True
        counter += 1
    if check == True:
        print "Good job! You guessed the letter correctly!"
    else:
        guesses -= 1
    print letter_keeper

    if letters == length:
            guesses = 0
            print "Sike! You won!"
            break
    if l == word:
        print "Good job, you won"
        break

print "the word is", word


