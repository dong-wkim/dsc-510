# Purpose: To demonstrate the successful creation of a main method function
# DSC510-T302
# Dong Woon Kim
# Week 4 Assignment 4.1 Programming Assignment

def costCalc(cable_length):
    if cable_length <= 100:
        price = 0.95
    elif 100 < cable_length <= 250:
        price = 0.85
    elif 250 < cable_length <= 500:
        price = 0.75
    elif cable_length > 500:
        price = 0.55
    return cable_length * price

def main():
    print('Welcome to my week 4 assignment!')
    company_name = input('What is your company name? ')
    cable_length = round(float(input('How many feet of fiber optic cable do you need? ')),0)
    cost = costCalc(cable_length)
    print('Company Name: ', company_name)
    print('Length of fiber optic cable: ', round(cable_length))
    print('Total cost: ', '$',format(cost,',.2f'))

if __name__ == "__main__":
    main()