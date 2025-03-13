alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:  # Check if the letter is in the alphabet
            shifted_position = (alphabet.index(letter) + shift) % len(alphabet)
            encrypted_text += alphabet[shifted_position]
        else:
            encrypted_text += letter  # Non-alphabetic characters are added as-is
    print("The encoded text is: " + encrypted_text)

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:  # Check if the letter is in the alphabet
            shifted_position = (alphabet.index(letter) - shift) % len(alphabet)
            decrypted_text += alphabet[shifted_position]
        else:
            decrypted_text += letter  # Non-alphabetic characters are added as-is
    print("The decoded text is: " + decrypted_text)

# Main loop to allow retrying
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    else:
        # Handle invalid input
        print("Invalid input. Please type 'encode' or 'decode'.")
        continue  # Restart the loop
    
    # Ask the user if they want to try again
    try_again = input("Would you like to try again? Type 'yes' to continue or 'no' to exit:\n").lower()
    if try_again != "yes":
        print("Goodbye!")
        break