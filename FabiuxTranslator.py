print("Welcome to the Fabiux Translator!")
# Starting coding
suffix = 'ay'
myword = input("Enter a word:")
if len(myword) > 0 and myword.isalpha():
    word = myword.lower()
    first = word[0]
    new_word = word + first + suffix
    new_word = new_word[1:]
    print(new_word)
else:
    print("You didn't enter a word")
# End Coding
