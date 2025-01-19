# Purpose: to demonstrate the use of conditional statements
# DSC510-T302
# Dong Woon Kim
# Week 3 Assignment 3.2 Programming Assignment

print('Welcome to my week 3 assignment!')
company_name = input('What is your company name? ')
cable_length = round(float(input('How many feet of fiber optic cable do you need? ')),0)
try:
    if cable_length <= 100:
        cost = cable_length * 0.95
    elif 100 < cable_length <= 250:
        cost = cable_length * 0.85
    elif 250 < cable_length <= 500:
        cost = cable_length * 0.75
    elif cable_length > 500:
        cost = cable_length * 0.55
except ValueError:
    print('There is an error executing this code')

print('Company Name: ', company_name)
print('Length of fiber optic cable: ', round(cable_length))
print('Total cost: ', '$',format(cost,',.2f'))