#Task 2: Number Guessing Game
import random
def guessing_game():
    random_number=random.randint(1,100)
    print("Random Number Generated!")
    
    counter=0
    while True:
        counter+=1
        guess=int(input("Guess the Number:"))
        if(guess==random_number):
            print(f"Congratulations! You guessed the number in {counter} attempts.")
            break;
        elif(guess>random_number):
            print("Too High! Try again.")
        elif(guess<random_number):
            print("too Low! Try again.")
        else:
            print("Invalid Input!")
    
guessing_game()