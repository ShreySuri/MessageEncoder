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

prime = None

while prime == None:
    prime = int(input(print("Please choose a prime number. ")))
    if factor(prime) == 2:
        prime = prime
    else:
        prime = None



code = str(input(print("Please type your message. Leave one (1) space between each character, and disregard punctuation. ")
code_list = code.split()

i = 0 
code_list.append("counter")
while code_list[i] != "counter":
    i = i + 1
code_list.remove("counter")
print(code_list)
print(i)






                 
