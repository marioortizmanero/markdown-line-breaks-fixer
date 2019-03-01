import pyperclip
import re


def bigBreaks(text):
    return re.sub("\n", "\n\n", text)


def smallBreaks(text):
    return re.sub("\n", "  \n", text)


def finalMessage(text):
    print("----------------")
    print("\n" + text + "\n")
    print("----------------")
    paste = input("Paste to keyboard? (Y/n): ")
    if (paste == "Y" or paste == "y"):
        pyperclip.copy(text)
        print("Copied to clipboard succesfully.")
    else:
        print("Not copied to clipboard.")


while True:
    print("\nLINE BREAKS FIXER")
    print("   1. Small breaks (two spaces)")
    print("   2. Big breaks (extra enter)")
    mode = str(input("Input the mode you want to use: "))
    text = pyperclip.paste()
    if (mode == "1"):
        text = smallBreaks(text)
    elif (mode == "2"):
        text = bigBreaks(text)
    else:
        print("Mode not recognized!")
        continue
    finalMessage(text)
