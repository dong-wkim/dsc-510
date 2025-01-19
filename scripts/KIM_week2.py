#The purpose of this program is to print a receipt with the Company name, number of feet of fiber length, and the total cost.
# DSC510-T302
# Dong Woon Kim
# Week 2 Assignment 2.1 Programming Assignment

print('Welcome to my week 2 assignment!')
company_name = input('What is your company name? ')
cable_length = input('How many feet of fiber optic cable do you need? ')
cost = float(cable_length) * 0.95
print('Company Name: ', company_name)
print('Length of fiber optic cable: ', cable_length)
print('Total cost ($0.95 per foot): ', '$',cost)

