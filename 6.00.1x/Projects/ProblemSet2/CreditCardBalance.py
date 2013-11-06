#!/usr/bin/python

# Author: Andrew Selzer
# Purpose: calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month. This is for problem set 2, problem 1 of 6.00.1 x


# Variables for testing
balance = float(4213)
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Variable for program
totalPaid = 0

def minPayment(balance, monthlyPaymentRate):
	'''
	balance: should be type float
	monthlyPaymentRate: should be type float
	
	returns: a float
	'''
	return (balance * monthlyPaymentRate)

def interest(unpaidBalance, annualInterestRate):
	'''
	unpaidBalance: should be type float after minPayment is called
	monthlyPaymentRate: should be type float
	
	returns: a float
	'''
	return (balance * (annualInterestRate/12.0))

for x in range(12):
    print ("Month: " + str(x+1))
    print ("Minimum monthly payment: " + str(round(minPayment(balance, monthlyPaymentRate),2)))

    totalPaid += balance * monthlyPaymentRate
    balance -= minPayment(balance, monthlyPaymentRate)
    balance += interest(balance, annualInterestRate)

    print ("Remaining balance: " + str(round(balance,2)))

print ("Total Paid: " + str(round(totalPaid,2)))
print ("Remaining balance: " + str(round(balance,2)))