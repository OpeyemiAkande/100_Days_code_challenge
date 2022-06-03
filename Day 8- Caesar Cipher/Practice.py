# creates function that accepts inputs
# def greet(name, location):
#     print(f'Hello {name}')
#     print(f'what is it like in {location}')


# greet(name='Opeyemi', location='Lagos')

#Paint Area code
# from math import ceil

# height = int(input('Height of wall: '))
# width = int(input('Width of the wall: '))

# def cans(h=height, w=width, cpc=5):

#     num_of_cans = ceil((h * w) / cpc)
#     print(f'You\'ll need {num_of_cans} cans of paint')

    
# cans(height, width)

# prime number checker
def prime_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print('Is prime')
    else:
        print('Is not a prime')


prime_checker(12)





