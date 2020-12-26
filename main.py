import random
import time
import ctypes
import os
print("------------------")
ctypes.windll.kernel32.SetConsoleTitleW("Pattern Generator | Made By Safeer Abbas")

with open(f'{os.getcwd()}/assets/numbers.txt') as file:
    numbers = [number.strip() for number in file]
    file.close()

with open(f'{os.getcwd()}/assets/symbols.txt') as file:
    symbols = [symbol.strip() for symbol in file]
    file.close()

with open(f'{os.getcwd()}/assets/lowercase_letters.txt') as file:
    lowerCaseLetters = [lowercase_letter.strip() for lowercase_letter in file]
    file.close()

with open(f'{os.getcwd()}/assets/uppercase_letters.txt') as file:
    upperCaseLetters = [uppercase_letter.strip() for uppercase_letter in file]
    file.close()

def startup():
    print("Starting ...")
    time.sleep(1)
    print("""The format is :
    
N = Random Number
S = Random Symbol
L = Lowercase letter
U = Uppercase Letter
""")

    time.sleep(2)
    pattern = input("Please enter the pattern using the format: ")
    total = input("How many codes will you like to gen: ")
    fileClear = (input("Would you like to clear the current codes.txt in assets? (T/F): ")).upper()
    if fileClear not in "TF":
        raise Exception("Only T and F are accepted.")
        

    if fileClear == "T":
        with open(f'{os.getcwd()}/assets/codes.txt', 'r+') as file:
            file.truncate()
            file.close()
            
    fileWriting = (input("Would you like to save it to a file? (T/F): ")).upper()
    if fileWriting not in "TF":
        raise Exception("Only T and F are accepted.")

    display = (input("Would you like to display the codes? (T/F): ")).upper()
    
    if display not in "TF":
        raise Exception("Only T and F are accepted.")

    pattern_generator(pattern, total, fileWriting, display)

def pattern_generator(pattern, total, fileWriting, display):
    whitelist = ['N', 'S', 'L', 'U']
    for _ in range(1, int(total) + 1):
        code = []
        for char in pattern:
            randomNumber = random.choice(numbers)
            randomSymbol = random.choice(symbols)
            randomLowerCaseLetter = random.choice(lowerCaseLetters)
            randomUpperCaseLetter = random.choice(upperCaseLetters)
            if char not in whitelist:
                raise Exception(f"Character \"{char}\" is an unspecified character. Please look at the manual.")
    
            elif char == "N" :
                code.append(randomNumber)  
            elif char == "S":
                code.append(randomSymbol)
            elif char == "L":
                code.append(randomLowerCaseLetter)
            elif char == "U":
                code.append(randomUpperCaseLetter)
        code = "".join(code)
        if display == "T":
            print(code)
        if fileWriting == "T":
            with open(f'{os.getcwd()}/assets/codes.txt', 'a') as file:
                file.write(code + '\n')
    file.close()
            










startup()