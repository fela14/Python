import base64

# Encode
text = "developer:C1sco12345"
encoded = base64.b64encode(text.encode()).decode()
print(encoded)  # clean string

# Decode
decoded = base64.b64decode(encoded.encode()).decode()
print(decoded)  # clean string
