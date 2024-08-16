alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.


def ceaser_cipher(original_text, shift, direction):
    cipher_text = "" #empty to store results

    for letter in original_text: # iterate through each char
        if letter in alphabet:
            shift_amount = shift if direction == "encode" else -shift #forwards or backwards
            shift_position = (alphabet.index(letter) + shift_amount) % len(alphabet) #move alphabet index by shift and workout remainder
            cipher_text += alphabet[shift_position] #populate with new letters
        else:
            cipher_text += letter #retain non letters

    return cipher_text


def main():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction not in ["encode", "decode"]:
            print("Invalid direction. Please type encode or decode.")
            continue

        text = input("Type your message:\n").lower()
        try:
            shift = int(input("Type the shift number:\n")) # force int
        except ValueError:
            print("Invalid shift. Please enter a number")
            continue

        result = ceaser_cipher(text, shift, direction)
        print(f"Here is your {direction} result: {result}")

        repeat = input(f"Would you like to go again? Yes or No?   ").lower()
        if repeat != "yes":
            break

main()

