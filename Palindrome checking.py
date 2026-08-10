text = input("Enter text for palindrome checking: ").lower()
palindrome_check1 = list(text)
palindrome_check2 = palindrome_check1[::-1]

if palindrome_check1 == palindrome_check2:
    print("Given text is a Palindrome.")
else:
    print("Given text is not a palindrome.")