import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print("""Welcome to logic game Bagels.
In this game you will guess secret number from 3 figures.
Rules of this games:
1. If you guess a right figure, then program will print: Pico
2. If your figure is right and on the right place, then program will print: Fermi
3. If there aren`t right figures in your guess, then program will print: Bagels
Good luck!""")

    while True:     # the main cycle
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}")
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            num_guesses += 1

            if guess == secretNum:
                break

            if num_guesses > MAX_GUESSES:
                print("You ran out guesses")
                print(f'The answer was {secretNum}')

        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return "You got it"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # The right figure on the right place
            clues.append('Fermi')

        elif guess[i] in secretNum:
            # the right figure on the wrong place
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'

    else:
        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()