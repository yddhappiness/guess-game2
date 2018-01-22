from random import randint
i = randint(1,10)
count = 0
while count<5:
    guess = input("What is your guess number is between 1 and 10?")
    count += 1
    if int(guess) == i:
        print("good job")
        break
    else:
        print("you have {} times left.".format(5-count))
        
