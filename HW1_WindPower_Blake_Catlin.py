#######################################################################
# Program Filename: HW1_Windpower
# Author: Blake Catlin
# Date: 4/11/2022
# Description: This script will ask for individual components of an equation, this equation will then use those
# to give the user the maximum power of a wind turbine as well as the expected output with the given numbers
# Input: Average wind speed, operating efficiency, and radius of blades
# Output: Maximum power output and expected output
#######################################################################
AWS = input("Enter the average wind speed in m/s: ")
# This asks the user for the average wind speed that will be effecting the turbine
OE = input("Enter the operating efficiency as a percent: ")
# This asks the user for the operating efficiency of the wind turbine
R = input("Enter the radius of the blades: ")
# This asks the user for the radius of the blades of the turbine
A = 3.141592 * float(R)**2
# This stores the area of the wind turbines blades
Pmax = 0.5 * 1.2 * float(A) * float(AWS)**3
# Pmax calculates the maximum power output of the wind turbine using the Area and the Average wind speed from the user
ATP = float(Pmax) * (float(OE)/100)
# ATP is the actual total power of the turbine from the given inputs from the user
print("The maximum power that this turbine can output is", Pmax, "W")
# This will print the maximum power to the user
print("The power that will be output by this turbine is", ATP, "W")
# This will print the power that the wind turbine generates based on all given inputs