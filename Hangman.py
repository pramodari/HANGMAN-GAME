import random

def choose_word():
    words = ["python", "java", "kotlin", "javascript", "hangman", "developer"]
    return random.choice(words)

def display_hangman(attempts):
    stages = [
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
               |
               |
               |
               |
        ---------
        '''
    ]
    return stages[attempts]

def hangman():
    word = choose_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_hangman(attempts))
    print(word_completion)

    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")

        print(display_hangman(attempts))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats! You guessed the word:", word)
    else:
        print("Sorry, you ran out of attempts. The word was " + word + ". Better luck next time!")

if __name__ == "__main__":
    hangman()