import random
import math

def factor(x):
    a = int(math.sqrt(x)) + 1
    factors = 0
    for i in range (1, a):
        if (x/i) % 1 == 0:
            factors = factors + 2
        else:
            factors = factors + 0
    if math.sqrt(x) % 1 == 0:
        factors = factors - 1
    else:
        factors = factors - 0
    return(factors)


user_given_prime = int(input(print("If you would like to encode with a certain prime, plese enter it now. If not, please enter '0'. ")))

if user_given_prime % 1 == 0 and user_given_prime > 0:
    # prime check
elif user_given_prime == 0:
    user_given_prime = False
    prime = None
else:
    print("Please reload the program and type either a prime number or '0' ")


if user_given_prime == False:
    while prime == None:
        

