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