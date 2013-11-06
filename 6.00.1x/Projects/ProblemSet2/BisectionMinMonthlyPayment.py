#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: A program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months This is for problem set 2, problem 2 of 6.00.1 x


# Variables for testing
balance = float(999999)
annualInterestRate = 0.18

def interest(unpaidBalance, annualInterestRate):
	'''
	unpaidBalance: should be type float after minPayment is called
	monthlyPaymentRate: should be type float
	
	returns: a float
	'''
	return (unpaidBalance * (annualInterestRate/12.0))

monthlyInterestRate = (annualInterestRate)/12.0
low = balance/12.0
hi = (balance * ((1+monthlyInterestRate)**12))/12.0

guess = (low + hi)/2

newBalance = balance

while (abs(newBalance) >= 0.01):
    newBalance = balance
    monthsPassed = 0
    for month in range(12):
        newBalance -= guess
        newBalance += interest(newBalance, annualInterestRate)
        monthsPassed += 1

    if (newBalance < 0):
        hi = guess
        guess = ((low + hi)/2)
    else:
        low = guess
        guess = ((low + hi)/2)

print ("Lowest Payment: "+ str(round(guess,2)))
