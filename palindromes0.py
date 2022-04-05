while (True):
    word = input("Word? ")
    if (word.lower() == "quit"):
        break
    if (word == word[::-1]):
        print("Palindrome!")
    else:
        print("nope")

