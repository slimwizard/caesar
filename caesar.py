# Et tu, Brute?
# Matthew Rice
# CSC 444 - Applied Cryptography

import sys
import string

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "

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
        return True if valid_words/(len(msg_words)-1) > .90 else False

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

# get words from dictionary
dict_words = []
dictionary = open('dictionary.txt', 'r')
for line in dictionary:
    dict_words.append(line.lower().replace('\n', ''))

# try all possible values for shift and append messages to list
messages = []
for i in range(1,len(ALPHABET)):
    # messages.append({'message': decode_message(letters, i), 'shift': i})
    messages.append(Message(decode(letters, i), i))

# find correctly decoded message 
for message in messages:
    if message.is_valid(): print(f'SHIFT={message.shift_value}\n{message.content}')
        
