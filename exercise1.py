#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


money = 1000.00
print(money)

print("Lakshmi bought 2000 shares for $900 per share")
print("2000 shares * $900 per share =", 2000*900)
print("$1800000 was the total amount paid for the stock")

print("Lakshmi had to pay the 3% commission to the stockbroker")
print("$1800000 share purchase * 0.03 percent for stockbroker =", 1800000*0.03)
print("$54000 was the 3% commission paid to the stockbroker")

print("2 weeks later, Lakshmi sold 2000 shares for $942.75 per share")
print("$1800000 stock purchase + $54000 owed to stockbroker=", 1800000+54000)
print("$1854000 was the total stock purchase")

print("2 weeks later, Lakshmi sold 2000 shares for $942.75 per share")
print("2000 shares * $942.75 per share =", 2000*942.75)
print("$1885500.00 was the total amount sold for the stock")

print("Lakshmi had to pay the 3% commission to the stockbroker")
print("$1885500.00 share purchase * 0.03 percent for stockbroker =", 1885500*0.03)
print("$56565.00 was the 3% commission paid to the stockbroker")

print("$1885500.00 stock sell - $56565.00 owed to stockbroker =", 1885500.00-56565.00)
print("$1828935.00 was the amount Lakshmi made from the stock sold")

print("$1828935.00 total amount for stock sold -$1854000.00 total amount for stock bought  =", 1828935-1854000)

print("Lakshmi lost $25065.00 from the stock transaction")
