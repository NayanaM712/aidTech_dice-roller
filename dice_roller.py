import random
def roll_dice(num_dice):
    dice_rolls = []
    for a in range(num_dice):
        roll = random.randint(1, 6)
        dice_rolls.append(roll)
    return dice_rolls

def display_result(dice_rolls):
    total=0
    print("Dice rolls: ")
    for roll in dice_rolls:
        print(roll)
        total+=roll    
    print(f"total : {total}")    
    print()


print("Welcome to the Dice Rolling App!")
while True:
    num_dice = int(input("How many dice would you like to roll? "))
    dice_rolls = roll_dice(num_dice)
    print("Rolling dice..")
    display_result(dice_rolls)
    # print(total)
    choice = input("Roll again? (y/n): ")
    if choice.lower() != 'y':
        break

print("Thank you for using the Dice Rolling App!")


