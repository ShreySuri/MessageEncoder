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

a = "01"
b = "02"
c = "03"
d = "04"
e = "05"
f = "06"
g = "07"
h = "08"
i = "09"
j = "10"
k = "11"
l = "12"
m = "13"
n = "14"
o = "15"
p = "16"
q = "17"
r = "18"
s = "19"
t = "20"
u = "21"
v = "22"
w = "23"
x = "24"
y = "25"
x = "26"

code
