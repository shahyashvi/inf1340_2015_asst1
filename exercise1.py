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
shares_purchase_price = 900
stock_purchase_price = (number_shares_bought*shares_purchase_price)
commission_bought = (stock_purchase_price*0.03)
total_stock_purchase_price = (stock_purchase_price+commission_bought)

number_shares_sold = 2000
shares_sold_price = 942.75
stock_sold_price = (number_shares_sold*shares_sold_price)
commission_sold = (stock_sold_price*0.03)
total_stock_sold_price = (stock_sold_price-commission_sold)

Profit = (total_stock_sold_price-total_stock_purchase_price)
print("Lakshmi has " + str(Profit) + "dollars left.")

