print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

        
import random
number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Have you guessed the correct answer: ")
    if int(guess) == number:
        print("You guessed {}. That is correct!. exit the loop!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. continue the loop.".format(guess))

