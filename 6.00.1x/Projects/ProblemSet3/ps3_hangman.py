# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/Apache/Documents/GitHub/EdX/6.00.1x/Projects/ProblemSet3/words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedString = ''
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessedString += '_ '
        else:
            guessedString += letter
    return guessedString



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    guessedString = string.ascii_lowercase
    guessedString = list(guessedString)
    
    for letter in lettersGuessed:
        guessedString.remove(letter)
    
    guessedString = ''.join(guessedString)
    
    return guessedString
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    numOfGuesses = 8
    lettersGuessed = []
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long."
    ''.format(len(secretWord)))
    print "------------"
    
    while numOfGuesses != 0:
        
        # Checks to see if word is guessed
        if isWordGuessed(secretWord, lettersGuessed):
            print ("Congratulations, you won!")
            numOfGuesses = 0
            break
        
        # Prints number of guesses
        print("You have {} guesses left."
        ''.format(numOfGuesses))
        
        # Provides letters to choose from
        print("Available letters: {}"
        ''.format(getAvailableLetters(lettersGuessed)))
        
        # Prompt user for a guess
        guess = raw_input("Please guess a letter: ")
        guess = guess.lower()
        
        # Parse guess
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: {}"
            ''.format(getGuessedWord(secretWord, lettersGuessed)))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print ("Good guess: {}"
            ''.format(getGuessedWord(secretWord, lettersGuessed)))
            # print (lettersGuessed)
        else:
            print ("Oops! That letter is not in my word: {}"
            lettersGuessed.append(guess)
            ''.format(getGuessedWord(secretWord, lettersGuessed)))    
            numOfGuesses -= 1
        
        print "------------"
        
        
    # If user loses
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print ("Sorry, you ran out of guesses. The word was {}."
    ''.format(secretWord)) 






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
