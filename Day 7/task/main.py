import random

word_list = ["aardvark", "baboon", "camel"]

# pick word at random and print it
chosen_word = random.choice(word_list)
print(chosen_word)

# declare empty string
placeholder = ""


# function for display word in hashes for hint
def dashes(placeholder, chosen_word):
    for char in range(len(chosen_word)):
        placeholder += "_"
    return (placeholder)


# display hint
placeholder = dashes(placeholder, chosen_word)
print(f"Hint: {placeholder}")


# check each char against guess and return the letter if correct

guess = ""
# get user guess
def user_input():
    guess = input("Guess a letter: ").lower()
    return guess


# game logic
def letter_check(guess, chosen_word):
    if guess in chosen_word:
        print("Match found!")
        return letter_match(guess, chosen_word)

    else:
        print("Wrong")

def letter_match(guess, chosen_word):
    display = ""
    for char in chosen_word:
        if guess == char:
            display += guess
        else:
            display += "_"
    return (display)

# call game check function and assign to display
#display = letter_check(guess)

# loops through to check if all dashes have been cleared by repeatedly getting user input
# and then checking that input
def game_loop(display, chosen_word):
    while "_" in display:
        print(f"Current state: {display}")
        guess = user_input()
        display = letter_check(guess, chosen_word)
    return display

display = dashes(placeholder, chosen_word)
final_display = game_loop(display, chosen_word)