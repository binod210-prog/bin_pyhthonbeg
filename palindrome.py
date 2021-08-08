""" String to check palindrome or not
Run a loop from starting to length/2 and check the first character to
the last character of the string and second to second last one and so on """

#Program



def isPalindrome(text):
    for i in range(0, int(len(text)/2)):
        if text[i] != text[len(text) -i -1]:
            return False
        else:
            return True

text = input(" Enter a string to check if it a palindrome :")

a = isPalindrome(text)

if (a):
    print("String is a palindrome")
else:
    print("String is not a palindrome")

          
    
