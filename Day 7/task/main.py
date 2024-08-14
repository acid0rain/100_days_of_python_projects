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
#placeholder = dashes(placeholder, chosen_word)



# check each char against guess and return the letter if correct

guess = ""
# get user guess
def user_input():
    guess = input("Guess a letter: ").lower()
    return guess

display = ""
# game logic
def letter_check(display, guess, chosen_word):
    new_display = "" # reset display to start fresh
    for index in range(len(chosen_word)):
        if guess == chosen_word[index]: # check through every char
            #print("Match found!")
            new_display += guess    # add correct guess to display
            #print(f"new display: {new_display}")
        else:
            new_display += display[index] #retain char and populate rest with _

    return new_display



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
    while display != chosen_word:
        print(f"Current guesses: {display}")
        guess = user_input()
        display = letter_check(display, guess, chosen_word)
        #print(f"curent display: {display}")
        if display == chosen_word:
            print(f"Congratulation you solved it! The word is: {display}")
        if guess not in display:
            print(f"Wrong guess!")
        else:
            print("Thats a match!")
    return display


display = dashes("", chosen_word)
print(f"Hint: {display}")
final_display = game_loop(display, chosen_word)






