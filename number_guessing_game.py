import random

k = 5  
correct_number = random.randint(1, 100)  

print(f"Welcome to the Number Guessing Game! You have {k} tries.")

for i in range(k):  
    try:
        guess = int(input("Enter your number: "))

        if guess > correct_number:
            print(f"The number is less than {guess}")
        elif guess < correct_number:
            print(f"The number is greater than {guess}")
        else:
            print("Congratulations! You guessed the number!")
            break 
    except ValueError:
        print("Please enter a valid number.")

    remaining_tries = k - (i + 1)  
    if remaining_tries > 0:
        print(f"You have {remaining_tries} tries left.")
    else:
        print(f"Game over! The correct number was {correct_number}.")


 