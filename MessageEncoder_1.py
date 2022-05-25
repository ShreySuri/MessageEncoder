import math
import random

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
    print("Please choose a prime number. For further protection, this prime should be greater than 10,000.")
    prime = int(input(print("If you would like a randomly generated prime, please type '0'. ")))
    if prime == 0:
        prime_found = False
        rand_int = random.randint(10000, 99900)
        while prime_found == False:
            if factor(rand_int) == 2:
                prime = rand_int
                prime_found = True
                print("")
                print("Your prime is %s" % prime)
            else:
                rand_int = rand_int + 1
    elif factor(prime) == 2 and prime > 10000:
        prime = prime
    else:
        prime = None

print("")
print("Please type your message. Leave one (1) space between each character. ")
code = input(print("Words can be denoted by using the '/' symbol. "))
code_list = code.split()
code_list.append("placeholder")
counter = 0
while code_list[counter] != "placeholder":
    counter = counter + 1

print("")
print("Your message has %s characters" % counter)

counter = counter
code_number = 0
place_value = counter - 1

for i in range (0, counter):
    code_list[i] = code_list[i].lower()
    if code_list[i] == "0":
        code_number = code_number + 10 * 100 ** place_value
    elif code_list[i] == "1":
        code_number = code_number + 11 * 100 ** place_value
    elif code_list[i] == "2":
        code_number = code_number + 12 * 100 ** place_value
    elif code_list[i] == "3":
        code_number = code_number + 13 * 100 ** place_value
    elif code_list[i] == "4":
        code_number = code_number + 14 * 100 ** place_value
    elif code_list[i] == "5":
        code_number = code_number + 15 * 100 ** place_value
    elif code_list[i] == "6":
        code_number = code_number + 16 * 100 ** place_value
    elif code_list[i] == "7":
        code_number = code_number + 17 * 100 ** place_value
    elif code_list[i] == "8":
        code_number = code_number + 18 * 100 ** place_value
    elif code_list[i] == "9":
        code_number = code_number + 19 * 100 ** place_value

    elif code_list[i] == "a":
        code_number = code_number + 20 * 100 ** place_value
    elif code_list[i] == "b":
        code_number = code_number + 21 * 100 ** place_value
    elif code_list[i] == "c":
        code_number = code_number + 22 * 100 ** place_value
    elif code_list[i] == "d":
        code_number = code_number + 23 * 100 ** place_value
    elif code_list[i] == "e":
        code_number = code_number + 24 * 100 ** place_value
    elif code_list[i] == "f":
        code_number = code_number + 25 * 100 ** place_value
    elif code_list[i] == "g":
        code_number = code_number + 26 * 100 ** place_value
    elif code_list[i] == "h":
        code_number = code_number + 27 * 100 ** place_value
    elif code_list[i] == "i":
        code_number = code_number + 28 * 100 ** place_value
    elif code_list[i] == "j":
        code_number = code_number + 29 * 100 ** place_value
    elif code_list[i] == "k":
        code_number = code_number + 30 * 100 ** place_value
    elif code_list[i] == "l":
        code_number = code_number + 31 * 100 ** place_value
    elif code_list[i] == "m":
        code_number = code_number + 32 * 100 ** place_value
    elif code_list[i] == "n":
        code_number = code_number + 33 * 100 ** place_value
    elif code_list[i] == "o":
        code_number = code_number + 34 * 100 ** place_value
    elif code_list[i] == "p":
        code_number = code_number + 35 * 100 ** place_value
    elif code_list[i] == "q":
        code_number = code_number + 36 * 100 ** place_value
    elif code_list[i] == "r":
        code_number = code_number + 37 * 100 ** place_value
    elif code_list[i] == "s":
        code_number = code_number + 38 * 100 ** place_value
    elif code_list[i] == "t":
        code_number = code_number + 39 * 100 ** place_value
    elif code_list[i] == "u":
        code_number = code_number + 40 * 100 ** place_value
    elif code_list[i] == "v":
        code_number = code_number + 41 * 100 ** place_value
    elif code_list[i] == "w":
        code_number = code_number + 42 * 100 ** place_value
    elif code_list[i] == "x":
        code_number = code_number + 43 * 100 ** place_value
    elif code_list[i] == "y":
        code_number = code_number + 44 * 100 ** place_value
    elif code_list[i] == "z":
        code_number = code_number + 46 * 100 ** place_value

    elif code_list[i] == "A":
        code_number = code_number + 47 * 100 ** place_value
    elif code_list[i] == "B":
        code_number = code_number + 48 * 100 ** place_value
    elif code_list[i] == "C":
        code_number = code_number + 49 * 100 ** place_value
    elif code_list[i] == "D":
        code_number = code_number + 50 * 100 ** place_value
    elif code_list[i] == "E":
        code_number = code_number + 51 * 100 ** place_value
    elif code_list[i] == "F":
        code_number = code_number + 52 * 100 ** place_value
    elif code_list[i] == "G":
        code_number = code_number + 53 * 100 ** place_value
    elif code_list[i] == "H":
        code_number = code_number + 54 * 100 ** place_value
    elif code_list[i] == "I":
        code_number = code_number + 55 * 100 ** place_value
    elif code_list[i] == "J":
        code_number = code_number + 56 * 100 ** place_value
    elif code_list[i] == "K":
        code_number = code_number + 57 * 100 ** place_value
    elif code_list[i] == "L":
        code_number = code_number + 58 * 100 ** place_value
    elif code_list[i] == "M":
        code_number = code_number + 59 * 100 ** place_value
    elif code_list[i] == "N":
        code_number = code_number + 60 * 100 ** place_value
    elif code_list[i] == "O":
        code_number = code_number + 61 * 100 ** place_value
    elif code_list[i] == "P":
        code_number = code_number + 62 * 100 ** place_value
    elif code_list[i] == "Q":
        code_number = code_number + 63 * 100 ** place_value
    elif code_list[i] == "R":
        code_number = code_number + 64 * 100 ** place_value
    elif code_list[i] == "S":
        code_number = code_number + 65 * 100 ** place_value
    elif code_list[i] == "T":
        code_number = code_number + 66 * 100 ** place_value
    elif code_list[i] == "U":
        code_number = code_number + 67 * 100 ** place_value
    elif code_list[i] == "V":
        code_number = code_number + 68 * 100 ** place_value
    elif code_list[i] == "W":
        code_number = code_number + 69 * 100 ** place_value
    elif code_list[i] == "X":
        code_number = code_number + 70 * 100 ** place_value
    elif code_list[i] == "Y":
        code_number = code_number + 71 * 100 ** place_value
    elif code_list[i] == "Z":
        code_number = code_number + 72 * 100 ** place_value

    elif code_list[i] == "'":
        code_number = code_number + 73 * 100 ** place_value
    elif code_list[i] == ",":
        code_number = code_number + 74 * 100 ** place_value
    elif code_list[i] == "/":
        code_number = code_number + 75 * 100 ** place_value
    elif code_list[i] == ".":
        code_number = code_number + 76 * 100 ** place_value
    elif code_list[i] == "!":
        code_number = code_number + 77 * 100 ** place_value
    elif code_list[i] == "?":
        code_number = code_number + 78 * 100 ** place_value

    elif code_list[i] == "placeholder":
        code_number = code_number + 99 * 100 ** place_value
    else:
        print("")
        print("You have typed an unrecognized symbol. Please refresh the program, follow directions, and try again. ")
        
    place_value = place_value - 1

composite = code_number * prime

print("")
print("Your code number is %s. Send this number to the recipient." % composite)
print("Detailed instructions can be found on the README page.")


