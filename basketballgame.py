from tkinter import *
import random
root=Tk()
root.title("Basketball_Game")
root.geometry("500x500")

# Game settings
timeout_duration = 60  # in seconds
game_duration = 600  # in seconds
max_fouls = 5
max_score = 100

# Game variables
score = 0
fouls = 0
timeouts = 3
game_over = False

print("Welcome to the basketball game!")
time.sleep(1)

# Game loop
while not game_over:
    print("\nCurrent score: ", score)
    print("Current fouls: ", fouls)
    print("Remaining timeouts: ", timeouts)
    print("Time remaining: ", game_duration)

    # User input for action
    action = input("\nWhat would you like to do? (shoot, foul, timeout): ")

    if action == "shoot":
        # User input for shooting
        shooting_option = input("Select your shooting option - 1, 2 or 3: ")

        if shooting_option not in ["1", "2", "3"]:
            print("Invalid input, try again.")
            continue

        shooting_option = int(shooting_option)
        # 1 represents a free throw, 2 represents a 2-point shot, and 3 represents a 3-point shot.

        # Probability of successful shot
        if shooting_option == 1:
            success_probability = 0.85
        elif shooting_option == 2:
            success_probability = 0.6
        else:
            success_probability = 0.35

        # Check if shot is successful
        if random.random() <= success_probability:
            print("Shot successful!")
            score += shooting_option
        else:
            print("Shot missed!")

        game_duration -= 10

    elif action == "foul":
        if fouls >= max_fouls:
            print("You have reached the maximum number of fouls. Game over!")
            game_over = True
            break

        print("Foul committed!")
        fouls += 1
        score -= 1

    elif action == "timeout":
        if timeouts == 0:
            print("You have used all your timeouts!")
            continue

        print("Taking a timeout...")
        time.sleep(timeout_duration)
        timeouts -= 1

    else:
        print("Invalid input, try again.")
        continue

    # Check game over conditions
    if score >= max_score:
        print("You have won the game with a score of ", score)
        game_over = True

    if game_duration <= 0:
        print("Game over! You lost with a score of ", score)
        game_over = True

print("Thank you for playing the basketball game!")

root.mainloop()



