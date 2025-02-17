import random

words = ['banana', 'orange', 'pear', 'apple', 'kiwi', 'papaya', 'pineapple', 'dragonfruit', 'mango', 'coconut', 'cherry', 'grape', 'grapefruit', 'tangerine', 'lemon']

# Randomly choose a word from the list 
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]  # Create a list of underscores
attempts = 8  # Number of allowed attempts

print("Welcome to Fruit Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("That letter does not appear in the word imbecile.")
        attempts -= 1

# Game Conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(''.join(word_display))  
    print("You survived!")
else:
    print(f"You ran out of attempts. The word was: {chosen_word}")
    print("You lost bitch. Better luck next time.")
