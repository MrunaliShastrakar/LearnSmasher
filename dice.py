import random

def roll_dice(num_dice, num_sides):
    results = []
    for _ in range(num_dice):
        roll_result = random.randint(1, num_sides)
        results.append(roll_result)
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        num_dice = int(input("Enter the number of dice to roll: "))
        num_sides = int(input("Enter the number of sides on each die: "))
        
        if num_dice <= 0 or num_sides <= 0:
            print("Number of dice and sides must be greater than 0. Please try again.")
            continue
        
        results = roll_dice(num_dice, num_sides)
        print("Rolling...")
        print("Results:", results)
        
        play_again = input("Do you want to roll again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for using the Dice Rolling Simulator!")
            break

if __name__ == "__main__":
    main()
