import pyperclip
import re


def bigBreaks(text):
    return re.sub("\n+", "\n\n", text)


def smallBreaks(text):
    return re.sub("\n+", "  \n", text)


def finalMessage(text):
    print("### START OF TEXT ###\n"
          f"{text}\n"
          "### END OF TEXT ###")
    paste = input("Paste to the clipboard? [Y/n]: ")
    if paste in ("y", "Y", ""):
        pyperclip.copy(text)
        print("Copied to the clipboard succesfully.")
    else:
        print("Not copied to the clipboard.")


while True:
    print("\nLINE BREAKS FIXER\n"
          "   1. Small breaks (two spaces)\n"
          "   2. Big breaks (extra newline)")
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
