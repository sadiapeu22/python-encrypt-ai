def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.islower():
            ascii_code = ord(char)
            new_ascii_code = ascii_code + shift
            if new_ascii_code > ord('z'):
                new_ascii_code = new_ascii_code - 26
            new_char = chr(new_ascii_code)
            result += new_char
        elif char .isupper():
            ascii_code = ord(char)
            new_ascii_code = ascii_code + shift
            if new_ascii_code > ord('Z')
                new_ascii_code = new_ascii_code -26
            new_char = chr(new_ascii_code)
            result = result + new_char

        else:
            result = result + char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

text = input("Enter your text: ")
shift = int(input("Enter your shift value: "))

encrypted_text = caesar_encrypt(text, shift)
decrypted_text = caesar_decrypt(text, -shift)