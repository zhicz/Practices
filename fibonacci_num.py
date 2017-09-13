#return fibonacci number

def fibo(ask:int):
    #while loop method, takes less time when calculating higher indices
    num1 = 1
    num2 = 1
    fibo = num1
    while ask > 2:
        fibo = num1 + num2
        num1 = num2
        num2 = fibo
        ask -= 1
    return fibo

'''
def fibo(ask:int):
    #recursion method, less lines of codes
    if ask <= 2:
        return 1
    else:
        return fibo(ask-1) + fibo(ask-2)
'''

def main():
    ask = int(input("Enter the index of fibonacci number:"))
    print(fibo(ask))

main()
