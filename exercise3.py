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
    Yes (Is the car silent when you turn the key?)
        Yes (Are the battery terminals corroded?)
        or No (Are the battery terminals corroded?)
        Neither yes or no (Are the battery terminals corroded?)

    No (Is the car silent when you turn the key?)
        Yes (Does the car make a clicking noise?)
        No (Does the car make a clicking noise?)
        Neither yes or no (Does the car make a clicking noise?)
            Yes (Does the car crank up but fail to start?)
            No (Does the car crank up but fail to start?)
            Neither yes or no (Does the car crank up but fail to start?)
                Yes (Does the engine start and then die?)
                No (Does the engine start and then die?)
                Neither yes or no (Does the engine start and then die?)
                    Yes (Does your car have fuel injection?)
                    No (Does your car have fuel injection?)
                    Neither yes or no (Does your car have fuel injection?)

    Neither yes or no (Is the car silent when you turn the key?)


    Expected Outputs: more questions or solutions
    Are the battery terminals corroded?
        Please clean terminals and try again.
        The battery cables may be damaged. Replace cables and try again.
        Please enter either yes or no.

    Does the car make a clicking noise?
        Replace the battery.
        Does the car crank up but fail to start?
        Please enter either yes or no.
            Check spark plug connections.
            Does the engine start and then die?
            Please enter either yes or no.
                Does your car have fuel injection?
                Engine is not getting enough fuel. Clean fuel pump. (YASHVI: this line is not found in the A1 instructions sheet)
                Please enter either yes or no.
                    Get it in for service.
                    Check to ensure the choke is opening and closing.
                    Please enter either yes or no.

    Please enter either yes or no.


    Errors: if something else is inserted other than yes or no, send error message
    0
        0
        0

    0
        0
        0
        0
            0
            0
            0
                0
                0
                0
                    0
                    0
                    0

    0
#SHOULD WE JUST WRITE an error statemnt here
#DO you mean the error statement, "Please enter either yes or no" for every line?
    """


silent_car = raw_input('Is the car silent when you turn the key?')
if silent_car == "Y":
    terminals_corroded = raw_input('Are the battery terminals corroded?')
    if terminals_corroded == "Y":
        print "Please clean terminals and try starting again."
    elif terminals_corroded == "N":
        print("The battery cables may be damaged. Replace cables and try again.")
    else:
        print ("Please enter either yes or no.")
elif silent_car == "N":
    clicking_noise = raw_input('Does the car make a clicking noise?')
    if clicking_noise == "Y":
        print("Replace the battery.")
    elif clicking_noise == "N":
        crank_up = raw_input('Does the car crank up but fail to start?')
        if crank_up == "Y":
            print("Check spark plug connections.")
        elif crank_up == "N":
            engine_die = raw_input('Does the engine start and then die?')
            if engine_die == "Y":
                fuel_injection = raw_input("Does your car have fuel injection?")
                if fuel_injection == "N":
                    print("Get it in for service.")
                elif fuel_injection == "N":
                    print("Check to ensure the choke is opening and closing.")
                else:
                    print ("Please enter either yes or no.")
            elif engine_die == "N":
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