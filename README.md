## RSA Algorithm
> The algorithm implemented in this repository is based loosely on
the RSA algorithm's implementation in the book `Introduction to Algorithms`, section 31.7

This implementation of RSA Algorithm can be used in *three* ways
* As a package
* For just generating public, private key pairs
* As a testing tool for RSA algorithm  

All of the above three use cases are detailed below

***
##### Using as a package
From any other python script use import via `import RSA`, then
* `RSA.generate(bits)` will generate new public, private key pair  
   bits is the maximum size of the compounded bits to be used. Leave default if unsure.

* `RSA.encrypt(key, text)` will encrypt the given text according to the key pair provided  
   key is the pair (e, n)  

* `RSA.decrypt(key, ciphertext)` will decrypt the cipher text provided  
   key is the pair (d, n)  

***
##### Using as key generation
Run `RSA.py` and it shall give public, private key pair on the stdout  

***
##### Using as a testing tool
Run `test_RSA.py` and it will print
* the text before encryption

* the ciphertext after encryption

* the original text after decryption (if successful)

> Change the `text` parameter in `test_RSA.py` to change the text to be tested
