# Et tu, Brute?
# Matthew Rice
# CSC 444 - Applied Cryptography

# uses Python v3
# to run: 'python3 caesar.py < ciphertext-x.txt'
# requires a dictionary.txt file with all entries seperated by line break to be in the working directory

import sys
import string

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "

# Message helper class for code cleanliness and readability
class Message:
    def __init__(self, _content, _shift_value):
        self.content = _content
        self.shift_value = _shift_value

    def is_valid(self):
        msg_words = self.content.replace('\n', ' ') \
                     .translate(str.maketrans('', '', string.punctuation)) \
                     .split(" ")
        valid_words = 0
        for word in msg_words: 
            if word.lower() in dict_words: valid_words += 1
        return True if valid_words/(len(msg_words)-1) > .70 else False

# decode message for a specific shift value
def decode(text, shift):
    decoded_text = ''
    # iterate through letters in cipher text and decode each
    for letter in text:
        try:
            decoded_index = ALPHABET.index(letter)+(len(ALPHABET) - shift)
            decoded_text += ALPHABET[decoded_index%len(ALPHABET)]
        except:
            decoded_text += letter
    return decoded_text

#########################################################################################
############################# Program Flow Starts Below #################################
#########################################################################################

# get input from std in
input = sys.stdin
letters = list(input.read())

# get words from dictionary and load them into a list
dict_words = []
try:
    dictionary = open('dictionary.txt', 'r')
except:
    print("Oops. Sorry big fella but I need a dictionary.txt file to work.")
    exit()
for line in dictionary:
    dict_words.append(line.lower().replace('\n', ''))

# try all possible values for shift and append messages to list
messages = []
for i in range(1,len(ALPHABET)):
    messages.append(Message(decode(letters, i), i))

# find correctly decoded message and print the msg content and the shift value 
for message in messages:
    if message.is_valid(): print(f'SHIFT={message.shift_value}\n{message.content}')

     
