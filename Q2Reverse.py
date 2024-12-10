# Create a program that will accept a word and output the word one letter at a time in reverse.

# Prompt for word
word = input("Enter a word: ")

# loop
for letter in reversed(word):
    print(letter)
