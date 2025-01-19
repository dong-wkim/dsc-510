# Purpose: To demonstrate the successful creation of a main method function
# DSC510-T302
# Dong Woon Kim
# Week 5 Assignment 5.1 Programming Assignment

def perform_calculation(operator):
    x = int(input('What is the value of the first number? '))
    y = int(input('What is the value of the second number? '))
    
    if operator == '+':
        result_calculation = x + y
    if operator == '-':
        result_calculation = x - y
    if operator == '*':
        result_calculation =  x * y
    if operator == '/':
        result_calculation =  x / y
    print('The calculated value is: ', int(result_calculation))

def calculate_average():
    num_count = int(input('How many numbers do you wish to input? '))
    total_of_all_num = 0
    for x in range(num_count):
        num = float(input('Enter a number: '))
        total_of_all_num = total_of_all_num + num
    average_num = total_of_all_num / num_count

    print("Total of all numbers:", total_of_all_num)
    print("Average of all numbers:", average_num)
        

def main():
    print('Welcome to my week 5 assignment!')
    confirm = str(input("Would you like to perform a calculation of averages, or using operators ? Press 'Y'/'N' ('yes'/'no')." ))

    while confirm != 'Y':
        if confirm == 'N':
            print("Exiting the program. Goodbye.")
            return
        confirm = input("Invalid input. Please press 'Y' to proceed, or 'N' to exit: ")

    method = input("Please enter '1' to run a calculation of averages, and '2' to run a calculation using operators. ")
    if method == '2':
        operator = str(input('Enter the operator (+, -, *, /): '))
        perform_calculation(operator)
    elif method == '1':
        calculate_average()
    else:
        print("Invalid method selected.")

if __name__ == "__main__":
    main()

