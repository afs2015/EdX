#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: A program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months This is for problem set 2, problem 2 of 6.00.1 x


# Variables for testing
balance = float(3926)
annualInterestRate = 0.2

def interest(unpaidBalance, annualInterestRate):
	'''
	unpaidBalance: should be type float after minPayment is called
	monthlyPaymentRate: should be type float
	
	returns: a float
	'''
	return (unpaidBalance * (annualInterestRate/12.0))

payment = 0
newBalance = balance

while (newBalance > 0):
    newBalance = balance
    payment += 10
    monthsPassed = 0
    while (monthsPassed <= 11):
        newBalance -= payment
        newBalance += interest(newBalance, annualInterestRate)
        monthsPassed += 1
    
print ("Lowest Payment: "+ str(payment))
