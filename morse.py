# morse.py
# pylint: disable=missing-docstring
DICTIONNARY = {
    '.-':   'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..':  'D',
    '.':    'E',
    '..-.': 'F',
    '--.':  'G',
    '....': 'H',
    '..':   'I',
    '.---': 'J',
    '-.-':  'K',
    '.-..': 'L',
    '--':   'M',
    '-.':   'N',
    '---':  'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.':  'R',
    '...':  'S',
    '-':    'T',
    '..-':  'U',
    '...-': 'V',
    '.--':  'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'
}

def decode(message):
    if message == "":
    	return ""
    else:
        message_words = message.split(" / ")
        translated_message = [decode_word(word) for word in message_words]
        return ' '.join(translated_message)

def decode_word(word):
    word_alphabet = word.split(" ")
    translated_word = [DICTIONNARY[alphabet] for alphabet in word_alphabet]
    return ''.join(translated_word)