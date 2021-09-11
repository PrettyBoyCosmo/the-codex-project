#!/usr/bin/python

# vigenere cipher package for the the codex project
# created by : C0SM0

# TODO: get key through cipher
    # auto decrypt [-a], show key
    # hard brute key length [pick range]
# TODO: document code
# TODO: clean up code

# imports
import sys
import getopt

# banner
banner = """
____   ____.__                                                    _________ .__       .__                  
\\   \\ /   /|__| ____   ____   ____   ___________   ____           \\_   ___ \\|__|_____ |  |__   ___________ 
 \\   Y   / |  |/ ___\\_/ __ \\ /    \\_/ __ \\_  __ \\_/ __ \\   ______ /    \\  \\/|  \\____ \\|  |  \\_/ __ \\_  __ \\
  \\     /  |  / /_/  >  ___/|   |  \\  ___/|  | \\/\\  ___/  /_____/ \\     \\___|  |  |_> >   Y  \\  ___/|  | \\/
   \\___/   |__\\___  / \\___  >___|  /\\___  >__|    \\___  >          \\______  /__|   __/|___|  /\\___  >__|   
             /_____/      \\/     \\/     \\/            \\/                  \\/   |__|        \\/     \\/       
"""

# help menu
help_menu = """
            Vigenere Cipher Arguments:

            First Argument:
            -e = encrypt
            -d = decrypt

            Additional Arguments:
            -k <string key> = key 
            -i <input file> = input file [.txt is best]
            -t <input text> = input text, one string only

            Example:
            main.py -v -e -t hello -k world           
            """

# letters for encryption process
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# symbols that can't be processed through the cipher
SYMBOLS = ['\n', '\t', ' ', '.', '?', '!', ',', '/', '\\', '<', '>', '|',
           '[', ']', '{', '}', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '`', '~', ':', ';', '"', "'", '0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9']

# encrypt vigenere
def encrypt_vigenere(plain_content, encryption_key, print_cnt):
    # output variable
    output = [] 
    index = 0

    # format key
    key = encryption_key.upper()
   
    # ciphering process
    for character in plain_content:
        num = LETTERS.find(character.upper())

        # starts encryption
        if num != -1:
            num += LETTERS.find(key[index])
            num %= len(LETTERS)
            
            # check for symbols
            if character in SYMBOLS:
                output.append(character)

            # check for uppercase
            elif character.isupper():
                output.append(LETTERS[num])

            # check for lowercase and others
            else:
                output.append(LETTERS[num].lower())

            # update index
            index += 1
            
            # stop process when ciphering is done
            if index == len(key):
                index = 0

        # adds character in case of error
        else:
            output.append(character)
    
    # outputs content to cli
    if print_cnt == True:
        print(f'Encrypted Content:\n{("".join(output))}\n')

    # outputs content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(''.join(output))

# decryption process
def decrypt_vigenere(plain_content, encryption_key, print_cnt):
    # output variable
    output = [] 
    index = 0

    # format key
    key = encryption_key.upper()
   
    # ciphering process
    for character in plain_content:
        num = LETTERS.find(character.upper())

        # starts encrypiton
        if num != -1:
            num -= LETTERS.find(key[index])
            num %= len(LETTERS)
            
            # check for symbols
            if character in SYMBOLS:
                output.append(character)

            # check for uppercase
            elif character.isupper():
                output.append(LETTERS[num])

            # check for lowercase and others
            else:
                output.append(LETTERS[num].lower())

            # update index
            index += 1
            
            # stop process when ciphering is done
            if index == len(key):
                index = 0

        # adds character in case of error
        else:
            output.append(character)
    
    # outputs content to cli
    if print_cnt == True:
        print(f'Decrypted Content:\n{("".join(output))}\n')

    # outputs content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(''.join(output))

# parses arguments
def vigenere_parser():
    opts, args = getopt.getopt(sys.argv[2:], 'k:f:t:o:r:', ['key', 'inputFile', 'inputText', 'outputFile', 'range'])
    arg_dict = {}

    # loop through arguments, assign them to dict [arg_dict]
    for opt, arg in opts:
        # processing options
        if opt == '-k':
            arg_dict['-k'] = arg
        # input options
        if opt == '-i':
            arg_dict['-i'] = arg
        if opt == '-t':
            arg_dict['-t'] = arg
        # output options
        if opt == '-o':
            arg_dict['-o'] = arg

    return arg_dict
    
# command line interface
def cli(argument_check):

    # display banner
    print(f'{banner}\n\n')

    # one liners
    if argument_check == True:
        
        # trying to get all args
        try:
            arguments = vigenere_parser()

        # catches arguments with no value
        except getopt.GetoptError:
            print(f'[!!] No value was given to your argument\n{help_menu}')

        # continues with recieved arguments
        else:    
            # getting variables for ciphering process
            key = arguments.get('-k')
            inputted_content = arguments.get('-t')
            print_content = True
            
            # checks users output type
            if ('-i' in arguments):
                inputted_content = open(arguments.get('-i'), 'r').read()

            # checks if output was specified
            if ('-o' in arguments):
                print_content = arguments.get('-o')

            # check ciphering process
            ciphering_process = sys.argv[1]

            # attempts to run cipher
            try:
                # encrypts vigenere
                if ciphering_process == '-e':
                    encrypt_vigenere(inputted_content, key, print_content)

                # decrypts vigenere
                if ciphering_process == '-d':
                    decrypt_vigenere(inputted_content, key, print_content)

            # catches unspecified arguments
            except TypeError:
                print(f'[!!] No Key or Argument was specified\n{help_menu}')

    # help menu
    else:
        print(help_menu)

# main code
def vigenere_main():
    # checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True

    cli(arguments_exist)

# runs main code when ran
if __name__ == '__main__':
    vigenere_main()