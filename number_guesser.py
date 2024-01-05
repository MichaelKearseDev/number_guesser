import random

print("Welcome to the Number Guessing Game!")
print("Type in 'q' or 'quit' to exit the program")
top_of_range = input("Please enter a number, this number will allow you to guess between 0 and the number you entered: ").lower()

if top_of_range == 'q' or top_of_range == 'quit':
    print("Thanks for playing!")
    quit()

if not top_of_range.isdigit():
    print("Please type in a number!")
    quit()

top_of_range = int(top_of_range)

if top_of_range <= 0:
    print("Please enter a number greater than 0")
    quit()

random_number = random.randint(0, top_of_range)

while True:
    user_guess = input(f"Please enter your guess between 0 and {top_of_range}: ").lower()
    
    if user_guess == 'q' or user_guess == 'quit':
        print("Thanks for playing!")
        break

    if not user_guess.isdigit():
        print("Please enter a valid number.")
        continue

    user_guess = int(user_guess)

    if user_guess == random_number:
        print("Congrats, you guessed it right!")
        break
    elif user_guess < random_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")
