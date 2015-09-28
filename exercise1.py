#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


number_shares_bought = 2000
#pricepershare
price_shares_bought = 900
stocks_price_bought_total = (price_shares_bought*number_shares_bought)
commission_bought = stocks_price_bought_total*0.03

number_shares_sold = 2000
price_shares_sold = 942.75
stocks_price_sold_total = price_shares_sold*number_shares_sold
commission_sold = stocks_price_sold_total*0.03
money = ((stocks_price_sold_total-commission_sold) - (stocks_price_bought_total+commission_bought))
print ("Lakshmi has made a loss of because she has " + str(money) + " dollars left")