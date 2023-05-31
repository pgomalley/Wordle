# Wordle - Guess the Word Game
Author: Patrick OMalley
Version: 2
Finished on: Oct 10th, 2022

# Problem Description
Wordle is a Python script that runs a guessing game. The game randomly selects a word from a predefined list and users have to guess that word. The game provides feedback to guide the user towards the correct answer.

# Dataset Description
The word list used in this game is stored in 'words.dat', which contains 5757 lines with one word per line.

# Functions
The script contains several functions to facilitate the game:

readWords(filename='words.dat'): This function reads words from the given file and appends them to a list.

evalGuess(guess, target): This function provides feedback to the user about how close their guess is to the target word.

consistent(feedback, word): This function checks if the feedback is consistent with the word guessed by the player.

calcSize(S, feedback): This function calculates the number of words in a list that are consistent with the feedback provided.

wordle(S): This is the main game management function. It selects a target word from a list, manages game play, and returns True or False based on whether the user wants to play another round or not.

# Getting Started
Clone the repository.
Ensure you have the necessary Python environment and libraries installed.
Download the 'words.dat' file and ensure it's in the correct directory.
Run the wordle.py file to start the game.
Follow the on-screen prompts to guess the target word.
Modify the scripts for your own requirements, if needed.
Please note that modifying one function may disrupt the whole system as they are interconnected. Please thoroughly test the game after any modifications.
