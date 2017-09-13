#rock paper scissor game

r = "rock"
p = "paper"
s = "scissor"


def compare(p1,p2):
    if p1.lower() == r and p2.lower() == r:
        print("Tied")
    elif p1.lower() == r and p2.lower() == p:
        print("Player 2 wins")
    elif p1.lower() == r and p2.lower() == s:
        print("Player 1 wins")
    elif p1.lower() == p and p2.lower() == p:
        print("Tied")
    elif p1.lower() == p and p2.lower() == r:
        print("Player 1 wins")
    elif p1.lower() == p and p2.lower() == s:
        print("Player 2 wins")
    elif p1.lower() == s and p2.lower() == s:
        print("Tied")
    elif p1.lower() == s and p2.lower() == r:
        print("Player 2 wins")
    elif p1.lower() == s and p2.lower() == p:
        print("Player 1 wins")
    else:
        print("Invalid Inputs")

def ask():
    while True:
        cont = input("Continue Play?")
        if cont.lower() == "yes":
            return True
        elif cont.lower() == "no":
            return False
        else:
            print("Yes or No")

def main():
    m = 1
    while m == 1:
        p1 = input("Player 1:")
        p2 = input("Player 2:")
        compare(p1,p2)
        if ask():
            m = 1
        else:
            m = 0
    print("Thanks for playing")
main()
