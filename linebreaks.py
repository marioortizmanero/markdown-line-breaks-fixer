import pyperclip
import re


def bigBreaks(text):
    return re.sub("\n+", "\n\n", text)


def smallBreaks(text):
    return re.sub("\n+", "  \n", text)


def finalMessage(text):
    print("----------------\n")
    print(text)
    print("\n----------------")
    paste = input("Paste to the clipboard? (Y/n): ")
    if (paste == "Y" or paste == "y"):
        pyperclip.copy(text)
        print("Copied to the clipboard succesfully.")
    else:
        print("Not copied to the clipboard.")


while True:
    print("\nLINE BREAKS FIXER")
    print("   1. Small breaks (two spaces)")
    print("   2. Big breaks (extra enter)")
    mode = str(input("Please select the mode (1 or 2): "))
    text = pyperclip.paste()
    if (mode == "1"):
        text = smallBreaks(text)
    elif (mode == "2"):
        text = bigBreaks(text)
    else:
        print("Mode not recognized!")
        continue
    finalMessage(text)
