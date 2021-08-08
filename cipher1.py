""" Caesar Cipher encryption rule as
 c = (x + n) % 26
Where c is the encoded character, x is the actual character, and n is the number of positions we want to shift the character x by.
We’re taking mod with 26 because there are 26 letters in the English alphabet."""

# Caesar cipher advanced

text = input(" Enter a text data to be encrypted : ")
shiftVal = input(" Enter the encrypted code shift from 1.....25 : ")
cipher = ''

for char in text:
    if  char.isupper():   #True if all characters in upper case
        code = ord(char) - ord('A')    # gives unicode value
        # shift current characters by position
        c_shifted = (code + int(shiftVal)) % 26 + ord('A')
        c_new = chr(c_shifted)
        cipher += c_new

    elif char.lower():   #check if in lower case

        # subtract uincode of 'a' to get indec in [0-25] range

        code = ord(char) -ord('a')
        c_shifted = (code + int(shiftVal)) % 26 + ord('a')
        c_new = chr(c_shifted)
        cipher += c_new

    else:

        cipher += char

print("Plain text :" + text)
print("Shift value : " + shiftVal)
print("Encrypted Text :" + cipher)        
    


