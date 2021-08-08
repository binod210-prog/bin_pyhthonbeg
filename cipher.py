# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1    # gives unicode value
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)     # string representation of a character

print(cipher)
