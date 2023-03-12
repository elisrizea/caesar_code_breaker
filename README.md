
# **Caesar's Cipher Code Breaker**
    The Caesar cipher, also referred to as the shift cipher, Caesar's code, or Caesar shift, is one of 
    the most widely known and simplest ciphers. My code-breaking algorithm can successfully decipher messages
    encoded with the Caesar cipher as long as the encryption script uses the same alphabet as the code-breaking 
    script and does not encrypt spaces.


# **Description:**
    I have implemented a code-breaking algorithm that attempts to guess the encryption key by trying 
    one step at a time and decrypting the first four words of an encoded message. I then use the pyspellchecker 0.7.1
    module to check if at least three of the decrypted words are valid English. The alphabet used in the algorithm 
    can be modified or extended, as long as it matches the encrypted alphabet. To test the algorithm, 
    one can use the encoder_decoder.py script to prepare encoded messages. For accesibility use scripts build in 
    copy/paste utility

# **Require:**
    pyperclip 1.8.2
    https://pypi.org/project/pyperclip/
    pyspellchecker 0.7.1
    https://pypi.org/project/pyspellchecker/

# **Installation:**
    pip install pyperclip
    pip install pyspellchecker
    Edit alphabet.txt and ad 1 character per line to enlarge it. Delete or rename it to use the default
    alphabet (If one use a custom alphabet bount scripts will use alphabet.txt)

# **Running:**
    code_breaker.py (to breack a cipher)
    encrypt_decrypt. (to prepare a sample)

# **Credits:**
    Alin Rizea
https://www.linkedin.com/in/alin-rizea-b10368104/


