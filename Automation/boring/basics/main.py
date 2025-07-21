import pyperclip

# Copy text to clipboard
pyperclip.copy("This was copied!")

# Paste text from clipboard
text = pyperclip.paste()
print("Clipboard contains:", text)
