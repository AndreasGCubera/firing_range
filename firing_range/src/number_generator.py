import random
import logging
import sys


def generate_puzzle(low=1, high=100):
    print(f"I'm thinking a number between {low} and {high}")
    return random.randint(low, high)


def make_guess(target):
    guess = None
    while guess is None:
        try:
            guess = int(input("Guess: "))
        except ValueError as e:
            print("Enter an integer")
            logging.info(e)
            sys.exit(0)
        finally:
            print("Program closing")
    if guess == target:
        return True
    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")
    return False


def play(tries=8):
    target = generate_puzzle()
    while tries > 0:
        if make_guess(target):
            print("You win!")
            return
        tries -= 1
        print(f"You have {tries} left")

    print(f"Game over! The answer was {target}")


if __name__ == '__main__':
    logging.basicConfig(filename="log.txt", level=logging.INFO)
    play()
