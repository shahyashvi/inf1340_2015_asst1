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
    ***TEST CASES***
    Inputs
    Outputs

    Y, Y
    Clean terminals and try starting again.

    Y, N
    Replace cables and try again.

    N, Y
    Replace the battery.

    N, N, Y
    Check spark plug connections.

    N, N, N, N
    Engine is not getting enough fuel. Clean fuel pump.

    N, N, N, Y, N
    Check to ensure the choke is opening and closing.

    N, N, N, Y, Y
    Get it in for service.

    """

    silent_car = raw_input('Is the car silent when you turn the key?')
    if silent_car == "Y":
        terminals_corroded = raw_input('Are the battery terminals corroded?')
        if terminals_corroded == "Y":
            print "Clean terminals and try starting again."
        elif terminals_corroded == "N":
            print("Replace cables and try again.")
        else:
            print ("Enter Y or N.")
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
                    if fuel_injection == "Y":
                        print("Get it in for service.")
                    elif fuel_injection == "N":
                        print("Check to ensure the choke is opening and closing.")
                    else:
                        print ("Enter Y or N.")
                #taken from announcement on Blackboard - NOT originally in A1
                elif engine_die == "N":
                    print("Engine is not getting enough fuel. Clean fuel pump.")
                #illegal inputs should lead to errors
                else:
                    print ("Enter Y or N.")
            else:
                print ("Enter Y or N.")
        else:
            print ("Enter Y or N.")
    else:
        print ("Enter Y or N.")

#diagnose_car()