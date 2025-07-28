 #! python3
# adder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()
# Break the text into a list of lines (one item per line)
lines = text.split('\n')  # split() converts the string into a list, splitting at each newline

for i in range(len(lines)):     # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]  # add star to each string in "lines" list

# Combine the modified list back into a single string with line breaks
text = '\n'.join(lines)  # join() merges the list back into a single string, adding newlines between items

pyperclip.copy(text)

