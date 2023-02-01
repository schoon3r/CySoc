# Author: Jim Labilles
# Date: 27 Dec 2022

# For ROT-13 convertion please reference:
# >>> https://gchq.github.io/CyberChef/
# or
# >>> https://www.dcode.fr/rot-13-cipher

#########################################################
##                    CTF Challenge                    ##
#########################################################

# 1. Original Message is encoded with ROT-13 cipher
# 2. ROT-13 output is then converted to its decimal value
# 3. decimal values are finally encoded to morse code

CODE = {
    ' ': '_',
    "'": '.----.',
    '(': '-.--.-',
    ')': '-.--.-',
    ',': '--..--',
    '-': '-....-',
    '.': '.-.-.-',
    '/': '-..-.',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ':': '---...',
    ';': '-.-.-.',
    '?': '..--..',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '_': '..--.-'
}


def morseEncode(message):
    '''
    Converts a string passed in the function into morse code
    '''
    morseCode = ""
    for char in message:
        morseCode += CODE[char] + " "
    return morseCode


def ascii2Decimal(message):
    '''
    Converts an ASCII string (each character) passed in the function into its decimal equivalent.
    Returns a string equivalent of the decimal value separated by a space character
    '''
    message = message.upper()
    decimalMessage = ""
    for character in message:
        decimalMessage += str(ord(character)) + " "
    return decimalMessage

#########################################################
##                    CTF Solution                     ##
#########################################################


def morseDecode(message):
    '''
    Converts morse code to ASCII
    '''
    # Get a reverse mapping of the variable CODE
    reversed_Code = {}
    for key in CODE:
        val = CODE[key]
        reversed_Code[val] = key
    # Spit each morse code
    message = message.split(' ')
    # Start decoding
    decoded = ""
    for code in message:
        if code == '':
            pass
        else:
            decoded += reversed_Code[code]
    return decoded


def decimal2ASCII(message):
    '''
    Converts decimal to ASCII.
    '''
    message = message.split(" ")
    asciiMessage = ""
    for character in message:
        # print(type(character))
        if character == '':
            asciiMessage += chr(32)
        else:
            asciiMessage += chr(int(character))
    return asciiMessage


if __name__ == "__main__":
    # Encode
    flag = 'PlFBP_Synt{yhpx4f_vf_4a_vaf4a3_u4px3e}'
    encodedFlag = morseEncode(ascii2Decimal(flag))
    print(encodedFlag)

    # Decode
    decimalList = morseDecode(encodedFlag)
    decodedFlag = decimal2ASCII(decimalList)
    print(decodedFlag)
