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