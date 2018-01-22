from random import randint
i = randint(1,10)
while True:
    guess = input("What is your guess number is between 1 and 10?")
    if int(guess) == i:
        print("good job")
        break
    else:
        print("go on")
        
