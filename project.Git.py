def caesar_cipher(text, offset):
    encrypted_text = ""

    for character in text:
        if character.isalpha():
            base = 'a' if character.islower() else 'A'
            encrypted_text += chr((ord(character) - ord(base) + offset) % 26 + ord(base))
        else:
            encrypted_text += character

    return encrypted_text


def main():
    offset = int(input("Введите число смещения: "))
    text = input("Введите текст: ")

    encrypted_text = caesar_cipher(text, offset)
    
    print("Зашифрованный текст:", encrypted_text)


if __name__ == "__main__":
    main()
