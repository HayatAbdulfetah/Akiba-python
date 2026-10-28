text = input("Enter a word: ")
word = text.lower()

if word == word[::-1]:
    print(f"The word '{text}' is a palindrome!")
else:
    print(f"'{text}' is NOT a palindrome.")
