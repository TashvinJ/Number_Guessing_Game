from time import sleep
from sys import exit

print("Welcome to numebr guessing game")
sleep(1)

print("Ok, lets start the game")

def game():
    number1 = input("Enter a number: ")
    number2 = input("Enter another number to add both numbers: ")
    result = int(number1) + int(number2)
    print(f"The result of your number is: {result}")

if __name__ == "__main__":
    while True:
        doplay = input("Do you want to play the game (yes or no): ")
        if doplay == "yes" or "Yes":
            game()
    
        else:
            exit()
    
        doplayagain = input("Do you want to play the game again (yes or no): ")
        if doplayagain == "yes" or "Yes":
            game()
        
        continue
    