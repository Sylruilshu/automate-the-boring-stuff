#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcb_shelf = shelve.open("mcb")

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcb_shelf[sys.argv[2]] = pyperclip.paste()


if len(sys.argv) == 2 and sys.argv[1].lower() != "del_all":
    # List keywords and load content.
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])


# TODO: add del keyword to delete a key from the shelf
if len(sys.argv) == 3 and sys.argv[1].lower() == "del":
    if sys.argv[2] in mcb_shelf:
        del mcb_shelf[sys.argv[2]]


# TODO: add del keyword to delete all keys from the shelf
if len(sys.argv) == 2 and sys.argv[1].lower() == "del_all":
    for keys in list(mcb_shelf.keys()):
        del mcb_shelf[keys]


mcb_shelf.close()
