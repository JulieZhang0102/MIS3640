import random
a = random.randint(1,20)
i = 1
name = input("Hello! What is your name?")
print(f'Well, {name}, I am thinking of a number between 1 and 20.')
while i <= 6:
    n = int(input("> "))
    if n == a:
        print(f"Good job, {name}. You guessed my number in {i} guesses!")
        break
    else:
        if n > a:
            print(f"Take another guess, your number is too high. You have {6-i} times left.")
        else:
            print(f'Take another guess, your number is too low. You have {6-i} times left.')
        i += 1
print(f"You lose the game. The number is {a}.")