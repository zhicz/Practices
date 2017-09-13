# simple passcode generator
import random

def generate(strength:str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    symbol = "!@#$%^&*()-+=<>?/.,:\"';`~\\"
    elist = ["password","passcode","simple","secret","random","cat","dog","bird"]
    password = ""
    
    if strength.lower() == "easy":
        #generates 2 word passcode
        password = elist[random.randint(0,7)] + elist[random.randint(0,7)]       
        return password

    elif strength.lower() == "medium":
        #generates passcode with numbers and alphabet letters
        for i in range(10):
            rand = random.randint(0,25)
            p = alphabet[rand]
            if rand%2 == 0:
                password += p.upper()
            else:
                password += p
                password += str(random.randint(0,24))
        return password

    elif strength.lower() == "strong":
        #generates passcode with numbers, alphabet letters, and symbols
        for i in range(10):
            rand = random.randint(0,25)
            p = alphabet[rand]
            if rand%2 == 0:
                password += p.upper()
                password += symbol[random.randint(0,27)]
            else:
                password += p
                password += str(random.randint(0,9))
        return password
    else:
        return "INVALID STRENGTH (Easy, Medium, Strong)"

def c_play():
    while True:
        cont = input("Continue Generating Passcode? ")
        if cont.lower() == "yes":
            return True
        elif cont.lower() == "no":
            return False
        else:
            print("Yes or No")

def main():
    check = 1
    while check == 1:
        random.seed()
        ask = input("Enter strength for password (Easy, Medium, Strong):")
        print(generate(ask))
        #ask if more passcode needed
        if c_play():
            check = 1
        else:
            check = 0
        
    
main()
        
