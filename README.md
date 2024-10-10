# Caesar Cipher Program

This program implements a Caesar cipher, which is a type of substitution cipher. It shifts the letters of a given text by a specified number of positions in the alphabet while keeping the case of the letters intact. Any non-alphabetic characters remain unchanged.

## How It Works

1. **Caesar Cipher Function** (`caesar_cipher`):
   - The function `caesar_cipher(text, offset)` takes two parameters:
     - `text`: The string that you want to encrypt.
     - `offset`: The number of positions to shift each letter.
   - It iterates through each character in the input text:
     - If the character is a letter (either lowercase or uppercase), it shifts the letter by the `offset` value, while ensuring that it wraps around the alphabet.
     - Non-alphabetic characters (e.g., spaces, numbers, punctuation) are left unchanged.
   - The function returns the encrypted version of the text.

2. **Main Function**:
   - In the `main()` function, the program prompts the user to input:
     - The shift value (an integer) for the Caesar cipher.
     - The text to be encrypted.
   - The function then calls `caesar_cipher()` to encrypt the input text using the provided offset and prints the encrypted result.

## Example Usage

When you run the program, you will be prompted to enter the shift (offset) and the text to be encrypted:


In this example, the letter `H` becomes `K`, `e` becomes `h`, and so on. Non-alphabetic characters, such as `,` and `!`, remain unchanged.

## Requirements

This is a simple Python program and requires no external libraries. It works with Python 3.x.

## Running the Program

To run the program, simply execute the `caesar_cipher.py` script in your terminal or any Python environment:

```bash
python caesar_cipher.py
