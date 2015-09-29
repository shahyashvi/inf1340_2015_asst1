#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs: yes and no questions

    Expected Outputs: more questions or solutions

    Errors: if something else is inserted other than yes or no, send error message

    """
silent_car = raw_input('Is the car silent when you turn the key?')
if silent_car == "yes":
    terminals_corroded = raw_input('Are the battery terminals corroded?')
    if terminals_corroded == "yes":
        print "Please clean terminals and try starting again."
    elif terminals_corroded == "no":
        print("The battery cables may be damaged. Replace cables and try again.")
    else:
        print ("Please enter either yes or no.")
elif silent_car == "no":
    clicking_noise = raw_input('Does the car make a clicking noise?')
    if clicking_noise == "yes":
        print("Replace the battery.")
    elif clicking_noise == "no":
        crank_up = raw_input('Does the car crank up but fail to start?')
        if crank_up == "yes":
            print("Check spark plug connections.")
        elif crank_up == "no":
            engine_die = raw_input('Does the engine start and then die?')
            if engine_die == "yes":
                fuel_injection = raw_input("Does your car have fuel injection?")
                if fuel_injection == "yes":
                    print("Get it in for service.")
                elif fuel_injection == "no":
                    print("Check to ensure the chock is opening and closing.")
                else:
                    print ("Please enter either yes or no.")
            elif engine_die == "no":
                print("Engine is not getting enough fuel. Clean fuel pump.")
            else:
                print ("Please enter either yes or no.")
        else:
            print ("Please enter either yes or no.")
    else:
        print ("Please enter either yes or no.")
else:
    print ("Please enter either yes or no.")
diagnose_car()