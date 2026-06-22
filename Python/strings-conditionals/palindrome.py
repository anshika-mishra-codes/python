word = input("Enter a word: ")

rev = word[::-1]

if word == rev:
    print("Palindrome")
else:
    print("Not Palindrome")