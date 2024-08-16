alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


def decrypt(original_text, shift_amount):
    decrypted_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        decrypted_text += alphabet[shifted_position]
    print(f"Here is your decrypted result: {decrypted_text}")


def ceaser_cipher():
    repeat = False
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)
    else:
        print("Error")

    repeat = input(f"Would you like to go again? Yes or No?   ").lower()
    if repeat == "yes":
        ceaser_cipher()

ceaser_cipher()

