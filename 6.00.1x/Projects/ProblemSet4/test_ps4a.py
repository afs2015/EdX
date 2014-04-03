from ps4a import *
<<<<<<< HEAD
=======
import unittest
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979

#
# Test code
# You don't need to understand how this test code works (but feel free to look it over!)

# To run these tests, simply run this file (open up in IDLE, then run the file as normal)

def test_getWordScore():
    """
    Unit test for getWordScore
    """
    failure=False
    # dictionary of words and scores
    words = {("", 7):0, ("it", 7):4, ("was", 7):18, ("scored", 7):54, ("waybill", 7):155, ("outgnaw", 7):127, ("fork", 7):44, ("fork", 4):94}
    for (word, n) in words.keys():
        score = getWordScore(word, n)
        if score != words[(word, n)]:
            print "FAILURE: test_getWordScore()"
            print "\tExpected", words[(word, n)], "points but got '" + str(score) + "' for word '" + word + "', n=" + str(n)
            failure=True
    if not failure:
        print "SUCCESS: test_getWordScore()"

# end of test_getWordScore


def test_updateHand():
    """
    Unit test for updateHand
    """
    # test 1
    handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'l':1, 'm':1}
    expectedHand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
        print "\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2

        return # exit function
    if handCopy != handOrig:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
        print "\tOriginal hand was", handOrig
        print "\tbut implementation of updateHand mutated the original hand!"
        print "\tNow the hand looks like this:", handCopy
<<<<<<< HEAD
        
        return # exit function
        
=======

        return # exit function

>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
    # test 2
    handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    handCopy = handOrig.copy()
    word = "evil"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'v':1, 'n':1, 'l':1}
    expectedHand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
<<<<<<< HEAD
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"        
=======
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
        print "\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2

        return # exit function

    if handCopy != handOrig:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
        print "\tOriginal hand was", handOrig
        print "\tbut implementation of updateHand mutated the original hand!"
        print "\tNow the hand looks like this:", handCopy
<<<<<<< HEAD
        
=======

>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
        return # exit function

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "hello"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {}
    expectedHand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
<<<<<<< HEAD
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"                
        print "\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2
        
=======
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
        print "\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2

>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
        return # exit function

    if handCopy != handOrig:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
        print "\tOriginal hand was", handOrig
        print "\tbut implementation of updateHand mutated the original hand!"
        print "\tNow the hand looks like this:", handCopy
<<<<<<< HEAD
        
=======

>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
        return # exit function

    print "SUCCESS: test_updateHand()"

# end of test_updateHand

def test_isValidWord(wordList):
    """
    Unit test for isValidWord
    """
    failure=False
    # test 1
    word = "hello"
    handOrig = getFrequencyDict(word)
    handCopy = handOrig.copy()

    if not isValidWord(word, handCopy, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected True, but got False for word: '" + word + "' and hand:", handOrig

        failure = True

    # Test a second time to see if wordList or hand has been modified
    if not isValidWord(word, handCopy, wordList):
        print "FAILURE: test_isValidWord()"

        if handCopy != handOrig:
            print "\tTesting word", word, "for a second time - be sure you're not modifying hand."
            print "\tAt this point, hand ought to be", handOrig, "but it is", handCopy

        else:
            print "\tTesting word", word, "for a second time - have you modified wordList?"
            wordInWL = word in wordList
            print "The word", word, "should be in wordList - is it?", wordInWL

        print "\tExpected True, but got False for word: '" + word + "' and hand:", handCopy

        failure = True


    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "rapture"

    if  isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected False, but got True for word: '" + word + "' and hand:", hand

<<<<<<< HEAD
        failure = True        
=======
        failure = True
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected True, but got False for word: '"+ word +"' and hand:", hand

<<<<<<< HEAD
        failure = True                        
=======
        failure = True
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected False, but got True for word: '" + word + "' and hand:", hand
<<<<<<< HEAD
        
=======

>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
        failure = True

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "evil"
<<<<<<< HEAD
    
    if  not isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected True, but got False for word: '" + word + "' and hand:", hand
        
        failure = True
        
=======

    if  not isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected True, but got False for word: '" + word + "' and hand:", hand

        failure = True

>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
    # test 6
    word = "even"

    if  isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected False, but got True for word: '" + word + "' and hand:", hand
<<<<<<< HEAD
        print "\t(If this is the only failure, make sure isValidWord() isn't mutating its inputs)"        
        
        failure = True        
=======
        print "\t(If this is the only failure, make sure isValidWord() isn't mutating its inputs)"

        failure = True
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979

    if not failure:
        print "SUCCESS: test_isValidWord()"


wordList = loadWords()
print "----------------------------------------------------------------------"
print "Testing getWordScore..."
test_getWordScore()
print "----------------------------------------------------------------------"
print "Testing updateHand..."
test_updateHand()
print "----------------------------------------------------------------------"
print "Testing isValidWord..."
test_isValidWord(wordList)
print "----------------------------------------------------------------------"
print "All done!"
<<<<<<< HEAD
=======

class Test_testProblemSet(unittest.TestCase):
    def test_A(self):
        self.test = calculateHandlen({'b': 1, 'i': 2, 'k': 1, 'j': 1, 'o': 1, 'w': 1})
        self.assertEqual(7, self.test)

    def test_2(self):
        self.test = calculateHandlen({'a': 1, 'f': 1, 'i': 2, 'h': 1, 'n': 1, 'p': 1, 'r': 1})
        self.assertEqual(8, self.test)

    def test_3(self):
        self.test = calculateHandlen({'a': 0, 'f': 0, 'i': 0, 'h': 0, 'n': 0, 'p': 0, 'r': 0})
        self.assertEqual(0, self.test)

if __name__ == '__main__':
    unittest.main()
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
