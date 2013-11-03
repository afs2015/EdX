#s = 'azcbobobegghakl' # should output beggh
#s = 'duwhwzpneqlhwxoyxd' # should output duw
#s = 'zyxwvutsrqponmlkjihgfedcba' # should output z
#s = 'niazqowgkhsw' # should output hsw
#s = 'kjdkwsnvxeucty' # should output dkw
s = 'igoalhmhdqtqwd' # should output dqt

s1 = ''
testString = ''
ansString = ''

for char in s:
    print "s1 is " + s1
    if (char >= s1):
        s1 = char
        testString += s1
    else:
        s1 = char
        if (len(ansString) < len(testString)):
            ansString = testString
            testString = char
        else:
            testString = s1
    print "char is " + char + " test string is " + testString + " answer string is " + ansString
    
if (len(ansString) == 0):
    print "Longest substring in alphabetical order is: " + testString
elif (len(ansString) < len(testString)):
    print "Longest substring in alphabetical order is: " + testString
else:
    print "Longest substring in alphabetical order is: " + ansString