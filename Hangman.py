import random

def hangman():
    list_words = ["physics", "math", "chemistry", "english"]
    word = random.choice(list_words).lower()
    turns = 10
    guessed_counts = {letter: 0 for letter in word}  
    valid_entries = set('abcdefghijklmnopqrstuvwxyz')

    print("\nWelcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    hangman_graphics = [
        "------------",
        "     O      ",
        "     O      \n     |      ",
        "     O      \n     |      \n    /       ",
        "     O      \n     |      \n    / \\    ",
        "   \\O      \n     |      \n    / \\    ",
        "   \\O/     \n     |      \n    / \\    ",
        "   \\O/ |   \n     |      \n    / \\    ",
        "   \\O/_|   \n     |      \n    / \\    ",
        "   \\O/_|   \n     |      \n    / \\    \n---     ----"
    ]

    while turns > 0:
        revealed_counts = {letter: 0 for letter in word}
        main_word = ""

        for letter in word:
            if revealed_counts[letter] < guessed_counts[letter]:  
                main_word += letter
                revealed_counts[letter] += 1  
            else:
                main_word += "_"

        if main_word == word:
            print(main_word)
            print("Congratulations! You won!")
            return

        print("\nGuess the word:", main_word)
        guess = input("Enter a letter: ").lower()

        if guess not in valid_entries:
            turns -= 1
            print(f"Invalid input! You lost an attempt. {turns} attempts left.")
            print(hangman_graphics[min(9, 10 - turns)])
            continue

        if guess in word:
            total_occurrences = word.count(guess)
            if guessed_counts[guess] < total_occurrences:
                guessed_counts[guess] += 1  
            else:
                turns -= 1
                print(f"You already revealed all occurrences of '{guess}'. {turns} attempts left.")
                print(hangman_graphics[min(9, 10 - turns)])
        else:
            turns -= 1
            print(f"Wrong guess! {turns} attempts left.")
            print(hangman_graphics[min(9, 10 - turns)])

        if turns == 0:
            break  
    print("\nYou lost the game! The correct word was:", word)

name = input("Enter your name: ")
print("Welcome,", name)
print("Guess the word in less than 10 attempts.")
hangman()
