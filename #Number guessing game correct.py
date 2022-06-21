#Number guessing game

import random
n = random.randrange(1, 10)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too Low")
        guess = int(input("Enter Number Again: "))
    elif guess > n:
        print("Too High")
        guess = int(input("Enter Number Again: "))
    else:
        break
    print("You Guessed It Right!!")

    

