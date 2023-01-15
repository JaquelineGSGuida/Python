
def vowel(letter):
    if letter == "a" or letter == "A" or letter == "e" or letter == "E" or letter == "i" or letter == "I" or letter == "o" or letter == "O" or letter == "u" or letter == "U":
        return True
    else:
        return False

inpLetter = (input("Enter a letter:"))
print(vowel(inpLetter))