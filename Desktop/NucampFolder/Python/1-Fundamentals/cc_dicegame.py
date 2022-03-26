import random

high_score = 0


def dice_game():
    dice1 = [1, 2, 3, 4, 5, 6]
    dice2 = [1, 2, 3, 4, 5, 6]
    roll1 = random.choice(dice1)
    roll2 = random.choice(dice2)
    new_score = roll1 + roll2
    print("\nYou rolled a", str(roll1), "and a", str(roll2) + ".")
    print("\nYou have rolled a total of: ", new_score)
    global high_score
    if new_score > high_score:
        print("\nNew highscore!")
        high_score = new_score


while True:
    print("\nCurrent High Score:", high_score)
    print("1) Roll Dice")
    print("2) Leave Game")
    choice = input("Enter your choice: ")
    if choice == "1":
        dice_game()
    else:
        print("Goodbye!")
        break
