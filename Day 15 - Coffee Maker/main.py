# This is the coffee maker machine code
# Todo: Prompt user for the type of coffee they want
# Todo: Write separate functions to make the different coffee variants
# Todo: Turn off the coffee machine by entering  off
# Todo: Print a report of the coffee resources
# Todo: check sufficiency of the resources
# Todo: Process coins
# Todo: Check that transaction is succesful
# Todo: Make coffee

def make_coffee(coffee_type, total):
    print(process_payment(coffee_type, total))
    print('Here is your coffee, enjoy!')

def make_latte():
    print('Yeah I am Latte!')

def make_cappucino():
    print('Yeah I am cappucino')

def print_report(water, milk, coffee):
    print(f'Water: {water}ml')
    print(f'Milk: {milk}ml')
#     print(f'Coffee: {coffee}g')
#
# def is_sufficient(coffee_type, water, milk, coffee,):
#     if coffee_type == 'espresso':
#         if water >= 50 and coffee >= 18:
#             return True
#         else:
#             return False
#     elif coffee_type == 'latte':
#         if water >= 200 and milk >= 150 and coffee >= 24:
#             return True
#         else:
#             return False
#     elif coffee_type == 'cappucino':
#         if water >= 250 and milk >= 100 and coffee >= 24:
#             return True
#         else:
#             return False
#
# def money_is_sufficient(coffee_type, total):
#     if coffee_type == 'espresso' and total >= 1.50:
#         return True
#     elif coffee_type == 'latte' and total >= 2.50:
#         return True
#     elif coffee_type == 'cappucino' and total >= 3.0:
#         return True
#     else:
#         return False
#
#
#
#
# def process_payment(coffee_type, total):
#
#     if coffee_type == 'espresso':
#         if money_is_sufficient(coffee_type, total):
#             change = total - 1.50
#             return f'Your change is ${change}'
#         # else:
#         #     return f'Your money is insufficient. Your refund is ${total}'
#
#     elif coffee_type == 'latte':
#         if money_is_sufficient(coffee_type, total):
#             change = total - 2.50
#             return f'Your change is ${change}'
#         # else:
#         #     return f'Your money is insufficient. Your refund is ${total}'
#
#     elif coffee_type == 'cappucino':
#         if money_is_sufficient(coffee_type, total):
#             change = total - 3.0
#             return f'Your change is ${change}'
#         # else:
#         #    return f'Your money is insufficient. Your refund is ${total}'
#
# def user_money():
#     quater = 0.25
#     dime = 0.10
#     nickle = 0.05
#     penny = 0.01
#
#     print('Please insert coins')
#
#     n_quaters = int(input('How many quaters? '))
#     n_dimes = int(input('How many dimes '))
#     n_nickles = int(input('How many nickles? '))
#     n_pennies = int(input('How many pennies? '))
#     total = quater * n_quaters + dime * n_dimes + nickle * n_nickles + penny * n_pennies
#     return total
#
# type_prompt = input('What would you like? (espresso/latte/cappuccino) ').lower()
#
# # print(process_payment('cappucino'))
# water = 300
# milk = 200
# coffee = 100
#
#
#
#
# turn_off = False
# while not turn_off:
#     if type_prompt == 'report':
#         print_report(water, milk, coffee)
#
#     total = user_money()
#     if type_prompt == 'espresso':
#         if is_sufficient(type_prompt, water, milk, coffee):
#             if money_is_sufficient(type_prompt, total):
#                 make_coffee(type_prompt)
#                 water -= 50
#                 coffee -= 18
#             else:
#               print(f'Your money is insufficient. Your refund is ${total}')
#
#         else:
#             print('Insufficient resources')
#
#
#     elif type_prompt == 'latte':
#         if is_sufficient(type_prompt, water, milk, coffee):
#             make_coffee(type_prompt)
#             water -= 200
#             milk -= 150
#             coffee -= 24
#         else:
#             print('Insufficient resources')
#
#     elif type_prompt == 'cappucino':
#         if is_sufficient(type_prompt, water, milk, coffee):
#             make_coffee(type_prompt)
#             water -= 250
#             milk -= 100
#             coffee -= 24
#         else:
#             print('Insufficient resources')
#
#
#
#
#     type_prompt = input('What would you like? (espresso/latte/cappuccino) ').lower()
#     if type_prompt == 'off':
#         turn_off = True
#         print('Bye Bye 👋')







