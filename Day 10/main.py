# A function that receives inputs from the user and performs calculations with them
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {'+': add, '-': subtract, '*': multiply, '/': divide} 




def calculator():
    n1 = int(input('Enter the first number '))
    exit = False 
    while not exit: 
        
        for symbol in operations:
            print(symbol)
        
        symbol_prompt = input('Enter an operation symbol from the listed ones above ')

        n2 = int(input('Enter next number '))

        
        calculation_function = operations[symbol_prompt]
        result = calculation_function(n1, n2)
        print(f'{n1} {symbol_prompt} {n2} = {result}')
        
        response = input('To continue another operation with the result press "y" ').lower()

        if response == 'y':
            n1 = result
        else:
            exit_res = input('Do you want to perform a new calculation or exit? Enter y for new calculation or n to exit ').lower()
            
            if exit_res == 'y':
                return calculator()
            else:
                exit = True

calculator()

        





