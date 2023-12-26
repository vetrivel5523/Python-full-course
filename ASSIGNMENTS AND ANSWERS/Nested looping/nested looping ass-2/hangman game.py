import random
print("WELCOME TO HANGMAN GAME")
def name():
    a = (input("Enter The Name :"))

def choose_word():
    words = ["vetri","tamil","vijay","laksh"]

    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word_to_guess = choose_word()
    a=name
    guessed_letters = []
    attempts = 6
    while True:
        print("\nAttempts left:", attempts)
        print(display_word(word_to_guess, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("\nCongratulations! ")
            print("You guessed the word:", word_to_guess)
            break

        if attempts == 0:
            print("\nYou've run out of attempts. The word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()
