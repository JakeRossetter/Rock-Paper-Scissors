import random
import time

choices = ["rock", "paper", "scissors"]
c_choice = ""
p_choice = ""
p_score = 0
c_score = 0
p_name = input("Player name: ")

while True:

    # Scorekeeping and choice input
    c_choice = random.choice(choices)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", "\n")
    print(p_name, "has", p_score, "points.")
    print("Computer has", c_score, "points", "\n")
    time.sleep(2)
    print('Type "exit" to quit.', "\n")
    time.sleep(2)
    p_choice = input("rock, paper or scissors? ")

    # win, lose, tie, exit, error functions
    def computer_win():
        print("Computer picked", c_choice)
        print("Computer wins!", "\n")
        time.sleep(3)

    def player_win():
        print("Computer picked", c_choice)
        print(p_name, "wins!", "\n")
        time.sleep(3)

    def tie():
        print("Computer picked", c_choice)
        print("Tie game.", "\n")
        time.sleep(3)

    def exit():
        print(p_name, "has", p_score, "points.")
        print("Computer has", c_score, "points", "\n")
        if p_score > c_score:
            print("You won!")
        elif p_score < c_score:
            print("You lost!")
        elif p_score == c_score:
            print("Tie game.")

    def error_message():
        print("Input error", "\n")
        time.sleep(3)

    # win/loss logic
    if p_choice == "rock" or "paper" or "scissors" or "exit":
        if p_choice == "exit":
            exit()
            break

        elif p_choice == c_choice:
            tie()

        elif p_choice == "rock":
            if c_choice == "paper":
                c_score += 1
                computer_win()
            elif c_choice == "scissors":
                p_score += 1
                player_win()

        elif p_choice == "paper":
            if c_choice == "scissors":
                c_score += 1
                computer_win()
            elif c_choice == "rock":
                p_score += 1
                player_win()

        elif p_choice == "scissors":
            if c_choice == "rock":
                c_score += 1
                computer_win()
            elif c_choice == "paper":
                p_score += 1
                player_win()
    else:
        error_message()
