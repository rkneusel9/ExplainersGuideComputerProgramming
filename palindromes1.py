done = False
while (not done):
    word = input("Word? ")
    if (word.lower() == "quit"):
        done = True
    elif (word == word[::-1]):
        print("Palindrome!")
    else:
        print("nope")

