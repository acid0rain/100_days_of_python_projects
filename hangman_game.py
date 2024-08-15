import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



word_list = ["aardvark", "baboon", "camel"]

# pick word at random and print it
chosen_word = random.choice(word_list)
print(chosen_word)


# function for display word in hashes for hint
def dashes(chosen_word):
    return "_" * len(chosen_word)


# get user guess
def user_input():
    while True:
        guess = input("Guess a letter: ").lower()
        if guess.isalpha() and len(guess) == 1:
            return guess
        else:
            print("Invalid input. Please enter a single letter")

# game logic
def letter_check(display, guess, chosen_word):
    new_display = "" # reset display to start fresh
    for index in range(len(chosen_word)): # check through every char
        if guess == chosen_word[index]:  #checks if a match
            #print("Match found!")
            new_display += guess    # add correct guess to new display
            #print(f"new display: {new_display}")
        else:
            new_display += display[index] #retain guess and populate rest with _

    return new_display


user_lives = 6

# game loop to handle multiple guesses
def game_loop(display, chosen_word):
    while display != chosen_word and user_lives != 0:
        print(f"Current guesses: {display}")
        guess = user_input()
        display = letter_check(display, guess, chosen_word)

        if guess not in display:
            user_lives -= 1
            print(f"Wrong guess! Lives remaining: {user_lives}")
            if user_lives == 0:
                print("You have run out of lives. Game over")
        elif guess in display:
            print("Thats a match!")
            if display == chosen_word:
                print(f"Congratulation you solved it! The word is: {display}")
    return display, user_lives


display, user_lives = dashes(chosen_word)
print(f"Hint: {display}")
game_loop(display, chosen_word)
