

import hashlib

# function to encode a string with SHA256
def sha256_encoder(string):
    return hashlib.sha256(string.encode()).hexdigest()

# User input
input_string = input('Please enter a string to be encoded: ')

# Encoding
encoded_string = sha256_encoder(input_string)

# Output
print('The encoded string is: ', encoded_string)
