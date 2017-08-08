"""
This script is only a testing script for our RSA algorithm.py
"""
from RSA import generate, encrypt, decrypt


key_pair = generate(1024)
print "Generated Key pairs"
public_key = key_pair["public"]
private_key = key_pair["private"]

text = "Hello World! Testing the first RSA implementation."
print "Input Text:"
print text

# Now encrypt
ciphertext = encrypt(public_key, text)
print "Ciphertext is: "
print ciphertext

# Now decrypt
output_text = decrypt(private_key, ciphertext)
print "The encrypted text was:"
print output_text
