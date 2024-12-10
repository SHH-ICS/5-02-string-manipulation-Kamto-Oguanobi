# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.

while True:
    # Prompt 
    word = input("Enter a word or type quit to exit ")

    # check for if user wants to quit
    if word.lower() == 'quit':
        print("byebye👋😿")
        break
    
    # Calculate the length of the word
    word_length = len(word)
    
    # Display the result
    print(f"The length of the word '{word}' is: {word_length}")
