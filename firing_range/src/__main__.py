import random
import global_coordinates


def roll_dice(sides, dice):
    return list(random.randint(1, sides) for _ in range(dice))


def print_hi():
    name = input("What's your name? ")
    print(f"Hi, {name}")
    dice_list = roll_dice(6, 6)
    print(dice_list)
    input()
    longitude = global_coordinates.GlobalCoordinates.longitude.getter


def main():
    print_hi()


if __name__ == "__main__":
    main()
