#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:
    number_sides = 4
    number_sides = 2
    number_sides = 11
    number_sides = 8

    Expected Outputs:
    quadrilateral.
    Error.
    Error.
    octagon.

    Errors:
    No error
    Error
    Error


    """
    number_sides = raw_input('How many sides does your shape have? Please enter a number between 3 and 10. ')
    if number_sides == "3":
            print "triangle"
    elif number_sides == "4":
            print "quadrilateral"
    elif number_sides == "5":
            print "pentagon"
    elif number_sides == "6":
            print "hexagon"
    elif number_sides == "7":
            print "heptagon"
    elif number_sides == "8":
            print "octagon"
    elif number_sides == "9":
            print "nonagon"
    elif number_sides == "10":
            print "decagon"
    else:
        print("Error")


#name_that_shape()