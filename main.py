import random
low = 1
high = 100
number = random.randint(low, high)
guessesAtempt = 0
while True:
    guess = int(input(f"Enter Number Between {low}-{high}: "))
    guessesAtempt += 1
    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print(f"You guess it correctly. The number was {guess}")
        print("-----------------------------")
        print(f"To guess correct number you took {guessesAtempt} times")
        break