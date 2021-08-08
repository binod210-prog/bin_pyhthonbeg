#program to check if strings are anagrams

str1 = input(" Enter the first string to check for anagrams : ")
str2 = input("Enter the second string to check for anagrams : ")

#convert strings to lower case

str1 = str1.lower()
str2 = str2.lower()

# check if length are same

if (len(str1) == len(str2)):
    
    #sort the strings
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    
    if (str1_sorted == str2_sorted):
        print(" The strings are anagrams")
        
    else:
        print(" Strings are not anagrams")
        
        
else:
    
    print(" Strings are not anagrams")
