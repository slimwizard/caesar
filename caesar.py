# Et tu, Brute?
# Matthew Rice
# CSC 444 - Applied Cryptography

import sys
import string

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "

# decode message for a specific shift value
def decode_message(message, shift):
    decoded_text = ''
    # iterate through letters in cipher text and decode each
    for letter in message:
        try:
            decoded_index = ALPHABET.index(letter)+(len(ALPHABET) - shift)
            decoded_text += ALPHABET[decoded_index%len(ALPHABET)]
        except:
            decoded_text += letter
    return decoded_text

# check validity of decoded message by checking words against a dictionary
def is_valid(message, word_list):
    message = message.replace('\n', ' ') \
                     .translate(str.maketrans('', '', string.punctuation)) \
                     .split(" ")
    valid_words = 0
    for word in message: 
        if word.lower() in word_list: valid_words += 1
    return True if valid_words/len(message) > .65 else False

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
    dict_words.append(line.lower() \
                          .replace('\n', ''))

# try all possible values for shift and append messages to list
messages = []
for i in range(1,len(ALPHABET)):
    messages.append({'message': decode_message(letters, i), 'shift': i})

# find correctly decoded message 
for i in range(0, len(messages)):
    if is_valid(messages[i]['message'], dict_words):
        print(f'SHIFT={messages[i]["shift"]}')
        print(messages[i]['message'])
        
