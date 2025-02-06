"""
Zion King
Comp 163-004
In this program I will take a phrase as input, generates an acronym from it,
and add a period after each letter in the acronym. only the initial letters of words that
start with uppercase letters.
"""

# Take user input for the phrase and splits it
myPhrase = input("Enter a phrase: ")
words = myPhrase.split()

# empty string to store the acronym
placeHolder = ""

for word in words:
    if word[0].isupper():
        # Append the first letter of the word to the acronym
        placeHolder += word[0].upper() + "."

print(placeHolder)
