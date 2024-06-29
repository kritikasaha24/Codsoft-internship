#!/usr/bin/env python
# coding: utf-8

# # ROCK-PAPER-SCISSOR GAME
# The Rock Paper Scissors game is a classic hand game typically played between two people, but here it's played between a user and a computer. Each player simultaneously chooses one of three options: rock, paper, or scissors. The winner is determined by the rules:
# 
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

# In[ ]:


import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or          (user_choice == 'scissors' and computer_choice == 'paper') or          (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    user_score = 0
    computer_score = 0
    play_again = True
    
    while play_again:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, winner)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        print(f"\nScore: You {user_score} - Computer {computer_score}")
        
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'
    
    print("\nThanks for playing!")

# Run the game
play_game()


# Imports the random module to generate random choices for the computer.
# 
# get_user_choice():
# Prompts the user to enter their choice (rock, paper, or scissors).
# Validates the user input to ensure it is one of the valid choices.
# Returns the user's choice.
# 
# 
# get_computer_choice():
# Uses the random.choice() function to randomly select rock, paper, or scissors for the computer.
# Returns the computer's choice.
# 
# 
# determine_winner(user_choice, computer_choice):
# Compares the user's choice with the computer's choice to determine the winner.
# Returns 'user' if the user wins, 'computer' if the computer wins, or 'tie' if it's a draw.
# 
# 
# display_result(user_choice, computer_choice, winner):
# Prints the choices made by the user and the computer.
# Prints the result of the game based on who won or if it was a tie.

# In[ ]:




