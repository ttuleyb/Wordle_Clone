import random
from turtle import back

#main codes
reset = "\033[0m"
escape = "\033["
#styles
normal = "0;"
bold = "1;"
underline = "2;"
#colours
black = 30
red = 31
green = 32
yellow = 33
blue = 34
magenta = 35
cyan = 36
white = 37
#background colours
background = "40m"

bg_black = 40
bg_red = 41
bg_green = 42
bg_yellow = 43
bg_blue = 44
bg_purple = 45
bg_cyan = 46
bg_white = 47
bg_grey = 7

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

qwerty = ["q","w","e","r","t","y","u","i","o","p", "a","s","d","f","g","h","j","k","l", "z", "x", "c", "v", "b", "n", "m"]

# for i in range(40):
#     print(f"{escape}{bold}{i};{background}Text " + str(i))

# print(f"\033[{bold};{black};{bg_black}m A \033[0m", end="")
# print(f"\033[{bold};{black};{bg_red}m B \033[0m", end="")
# print(f"\033[{bold};{black};{bg_green}m C \033[0m", end="")
# print(f"\033[{bold};{black};{bg_yellow}m D \033[0m", end="")
# print()

file = open("/Users/user/dictionary.txt", "r")
dictionary = file.read()
file.close()

dictionary = dictionary.split("\n")
sorteddictionary = sorted(dictionary)

answer = dictionary[random.randint(0, len(dictionary))]
#answer = "AGENT"
splitanswer = [char for char in answer]
#print(answer)
line = ""

unknown = 0
non_existant = 1
wrong_spot = 2
correct_spot = 3

knowledge = []

for character in qwerty:
    knowledge.append([character.upper(),unknown])

trycount = 0

def guess(word, output):
    word = word.upper()
    if word in dictionary:
        global trycount
        trycount += 1
    else: 
        print("Not in dictionary")
        return False
    splitword = [char for char in word]
    count = 0
    for a_character in splitanswer: #Check for letters in correct spot
        b_character = splitword[count]
        if a_character == b_character:
            for i in range(len(knowledge)):
                if knowledge[i][0] == b_character:
                    knowledge[i][1] = correct_spot
        count += 1

    for b_character in splitword: #Check for matching letters in wrong spot
        if b_character in answer:
            for i in range(len(knowledge)):
                if knowledge[i][0] == b_character:
                    if knowledge[i][1] == correct_spot:
                        break
                    knowledge[i][1] = wrong_spot 

    for b_character in splitword:
        for i in range(len(knowledge)):
            if knowledge[i][0] == b_character:
                if knowledge[i][1] == unknown:
                    knowledge[i][1] = non_existant
                    break

    colourful_write(word, output)

    if word == answer:
        return True

guesses = ""

def colourful_write(word, guessing):
    word = word.upper()
    splitword = [char for char in word]

    line = ""

    for i in range(len(splitword)):
        for x in range(len(knowledge)):
            if knowledge[x][0] == splitword[i]:
                background_color = determine_background(x)
                if background_color == bg_grey:
                    line += f"\033[{bold};{background_color};{background_color}m {splitword[i]} \033[0m"
                else:
                    line += f"\033[{bold};{black};{background_color}m {splitword[i]} \033[0m"
    global guesses
    if guessing:
        guesses += line + "\n"
        print(guesses)
    else:
        print(line)

def determine_background(position):
    if knowledge[position][1] == unknown:
        background_color = 47
    elif knowledge[position][1] == non_existant:
        background_color = bg_grey
    elif knowledge[position][1] == wrong_spot:
        background_color = bg_yellow
    elif knowledge[position][1] == correct_spot:
        background_color = bg_green
    return background_color

def print_keyboard():
    line = ""
    for i in range(10):
        background_color = determine_background(i)
        line += f"\033[{bold};{black};{background_color}m {qwerty[i]} \033[0m "

    print(line)
    line = ""

    for i in range(9):
        background_color = determine_background(i+10)
        line += f"\033[{bold};{black};{background_color}m {qwerty[i+10]} \033[0m "

    print(line)
    line = ""

    for i in range(7):
        background_color = determine_background(i+19)
        line += f"\033[{bold};{black};{background_color}m {qwerty[i+19]} \033[0m "

    print(line)
    line = ""

# for i in range(100):
#      print(f"\033[{bold};{i};{7}m HELLOWORLD \033[0m {i}")

while True:
    print_keyboard()
    tryhard = input("Take a guess:")
    if trycount == 5:
        print("You couldn't guess it lmao it was")
        guess(answer, False)
        break
    if len(tryhard) == 5:
        print("Checking...")
        if guess(tryhard, True) == True:
            print("Damn son you got this")
            break
    else:
        print("Try a 5 letter word")