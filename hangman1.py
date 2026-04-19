import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    return all(letter in letters_guessed for letter in secret_word)


def get_guessed_word(secret_word, letters_guessed):
    letter=""
    for i in secret_word:
        if i in letters_guessed:
            letter=letter+i
        else :
            letter=letter+"-"
    return letter


def get_available_letters(letters_guessed):
    return ''.join(letter for letter in string.ascii_lowercase if letter not in letters_guessed)


def hangman(secret_word):
    guesses_remaining = 6
    letters_guessed = []

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()

        if guess in letters_guessed:
            print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            guesses_remaining -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

    print("-------------")
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word + ".")


def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] != "_":
            if my_word[i] != other_word[i]:
                return False
        else:
            if other_word[i] in my_word:
                return False
    return True


def show_possible_matches(my_word):
    matches = [word for word in wordlist if match_with_gaps(my_word, word)]
    if matches:
        print("Possible word matches are:", ' '.join(matches))
    else:
        print("No matches found")


def hangman_with_hints(secret_word):
    guesses_remaining = 6
    letters_guessed = []

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()

        if guess == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:
            print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            guesses_remaining -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

    print("-------------")
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word + ".")


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    # Uncomment one of the following lines depending on which version you want to test:
    hangman_with_hints(secret_word)
    # hangman_with_hints(secret_word)
