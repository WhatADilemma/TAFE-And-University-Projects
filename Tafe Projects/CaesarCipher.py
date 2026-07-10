"""
SYNOPSIS

    Caesar.py
    No command line arguments involved.

DESCRIPTION

    Enter a plaintext message and then the rotation key. The
    plaintext is then converted to cypher text and saved to a file.

EXAMPLES

    User enters 'Hello!' and a key of 13.
    Output should give 'Uryyb!' and write it to a file.

AUTHOR

    Lindsay Coudert <30082098@tafe.wa.edu.au>

LICENSE

    This script is in the public domain, free from copyrights or
    restrictions.

VERSION

    0.2
"""
def rot(text, key):
    # Initialize your cipher_text before your loop
    cipher_text = ''

    # Validate the rotation key
    while not (0 <= key <= 25):
        try:
            key = int(input('Invalid key. Please enter a key between 0 and 25: '))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for char in text:
        # Check if the character is a letter (A-Z/a-z).
        if char.isalpha():
            num = ord(char)

            if char.isupper():
                # If the rotated value exceeds 'Z', calculate the correct position
                if (num + key) > 90:
                    x = (num + key) - 90
                    cipher_text += chr(x + ord('A') - 1)
                else:
                    cipher_text += chr(num + key)

            elif char.islower():
                # If the rotated value exceeds 'z', calculate the correct position
                if (num + key) > 122:
                    x = (num + key) - 122
                    cipher_text += chr(x + ord('a') - 1)
                else:
                    cipher_text += chr(num + key)
        else:
            # If the character is not a letter, simply add it as is.
            # This way, we don't change symbols or spaces.
            cipher_text += char

    # Return the final result of the processed characters for use.
    return cipher_text

# Ask the user for their message
plain_input = input('Input the text you want to encode: ')

# Ask the user for the rotation key and validate it
while True:
    try:
        rot_key = int(input('Input the key you want to use from 0 to 25: '))
        if 0 <= rot_key <= 25:
            break
        else:
            print("Invalid key. Please enter a key between 0 and 25.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

secret_message = rot(plain_input, rot_key)

# Print out message for feedback
print('Writing the following cipher text to file:', secret_message)

# Write the message to file
with open('EncryptedText.txt', 'w+') as file:
    file.write(secret_message)