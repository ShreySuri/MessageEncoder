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


code = str(input(print("Please type your message. Leave one (1) space between each character, and disregard punctuation. ")))
code_list = code.split()

letter_count = 0 
code_list.append("counter")
while code_list[i] != "counter":
    letter_count = letter_count + 1
code_list.remove("counter")
letter_count = letter_count - 1

code_number = 0
place_value = letter_count

for i in range (0, letter_count):
    code_list[i] = code_list[i].lower()
    if code_list[i] == "a":
        code_number = code_number + 11 * 100 ** place_value
    elif code_list[i] == "b":
        code_number = code_number + 12 * 100 ** place_value
    elif code_list[i] == "c":
        code_number = code_number + 13 * 100 ** place_value
    elif code_list[i] == "d":
        code_number = code_number + 14 * 100 ** place_value
    elif code_list[i] == "e":
        code_number = code_number + 15 * 100 ** place_value
    elif code_list[i] == "f":
        code_number = code_number + 16 * 100 ** place_value
    elif code_list[i] == "g":
        code_number = code_number + 17 * 100 ** place_value
    elif code_list[i] == "h":
        code_number = code_number + 18 * 100 ** place_value
    elif code_list[i] = "i":
        code_number = code_number + 19 * 100 ** place_value
    elif code_list[i] = "j":
        code_number = code_number + 20 * 100 ** place_value
    elif code_list[i] = "k":
        code_number = code_number + 20 * 100 ** place_value
    elif code_list[i] = "l":
        code_number = code_number + 22 * 100 ** place_value
    elif code_list[i] = "m":
        code_number = code_number + 23 * 100 ** place_value
    elif code_list[i] = "n":
        code_number = code_number + 24 * 100 ** place_value
    elif code_list[i] = "o":
        code_number = code_number + 25 * 100 ** place_value
    elif code_list[i] = "p":
        code_number = code_number + 26 * 100 ** place_value
    elif code_list[i] = "q":
        code_number = code_number + 27 * 100 ** place_value
    elif code_list[i] = "r":
        code_number = code_number + 28 * 100 ** place_value
    elif code_list[i] = "s":
        code_number = code_number + 29 * 100 ** place_value
    elif code_list[i] = "t":
        code_number = code_number + 30 * 100 ** place_value
    elif code_list[i] = "u":
        code_number = code_number + 31 * 100 ** place_value
    elif code_list[i] = "v":
        code_number = code_number + 32 * 100 ** place_value
    elif code_list[i] = "w":
        code_number = code_number + 33 * 100 ** place_value
    elif code_list[i] = "x":
        code_number = code_number + 34 * 100 ** place_value
    elif code_list[i] = "y":
        code_number = code_number + 35 * 100 ** place_value
    elif code_list[i] = "z":
        code_number = code_number + 36 * 100 ** place_value
    else:
        print("You have typed an unrecognized symbol. Please refresh the program, follow directions, and try again. ")
    place_value = place_value - 1

print(code_number)


