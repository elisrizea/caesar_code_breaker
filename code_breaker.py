import pyperclip
from spellchecker import SpellChecker

spell = SpellChecker()

# Save colors in constants to decorate the console output
GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'


def alphabet():
    # Add chars to alphabet tuple for better results
    # Add chars to alphabet tuple for better results
    alphabet = []
    try:
        with open('alphabet.txt') as txt:
            chars = txt.read().strip().splitlines()
            for char in chars:
                alphabet.append(f'{char}')
            alphabet = tuple(alphabet)
        print(f'{RED}Use custom alphabet from alphabet.txt{END}')

    except Exception:
        print("error loading alphabet from file")
        alphabet = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

    return alphabet
alphabet=alphabet()




# ******************************** class Cipher ******************************************
# Use alphabet tuple to replace every char with another that have index+step
class Cipher:

    def __init__(self, step, alphabet):
        self.alphabet = alphabet
        if step <= 0 or step > len(self.alphabet) - 1:
            # Unreachable line left her for class safety
            self.step = len(self.alphabet) // 2
        else:
            self.step = step
    # Getter alphabet size
    def alphabet_size(self):
        return len(self.alphabet) - 1

    # *********** Encrypt method ***************
    def encrypt(self, c):
        if c in self.alphabet:
            index = self.alphabet.index(c) + self.step
            if index <= len(self.alphabet) - 1:
                return self.alphabet[index]
            else:
                return self.alphabet[index - len(self.alphabet)]
        else:
            return c

    # *********** Decrypt method ***************
    def decrypt(self, c):
        if c in self.alphabet:
            index = self.alphabet.index(c) - self.step
            if index >= 0:
                return self.alphabet[index]
            else:
                return self.alphabet[len(self.alphabet) + index]
        else:
            return c


# *************************** def decrypt(step,  message):**************************
# Return decrypted message
def decrypt_m(step, message):
    op = Cipher(step,alphabet)
    res="".join(map(op.decrypt, message))
    return res


# *************************** def decrypt(step,  message):**************************
# Return decrypted message
def check_word(word):
    if word == spell.correction(word):
        return True
    else:
        return False


# ************** Main menu *********
# Initialise main menu vars
info = Cipher(1,alphabet)
message = input(
    f'Enter the message to {GREEN}decrypt.{END} or press {GREEN}(p){END}paste to past your clipboard content\n> ')
if message in ('p', 'P', 'Paste', 'PASTE', 'paste'):
    message = pyperclip.paste()
    print(f'Your message is:\n {GREEN}{message}{END}')

print('\nDecrypting...\n')

mess_list = message.split(' ')
#print('mess_list ',mess_list)
for_words = " ".join(mess_list[0:4])
#print('for_words= ',for_words)
print('Trying step',end=':')
for i in range(info.alphabet_size()):

    print(i, end='|')
    decrypted = decrypt_m(i, for_words).split(' ')
    #print(alphabet)
    try_count = 0
    score = 0
    for w in decrypted:
        #print('word is : ',w)
        #print('try_count ',try_count,'score = ',score)
        if check_word(w):
            score += 1
            try_count = 0
        else:
            try_count += 1
        if score >= 3 :
            decrypted = decrypt_m(i, message)
            print(f'\nYour decrypted file is : \n>{GREEN}{decrypted}{END}\n STEP found is : {i}')
            exit()
    if i>= info.alphabet_size()-1 and score < 3:
            print(f'\n{RED}Decoded failed. Possible cause the message is not in english or message is less then 4 words{END}')
            exit()



