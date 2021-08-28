#!/usr/bin/python

# caesar cipher package for the the codex project
# created by : C0SM0

# TODO: check if args are empty [try: code, except getopt.GetoptError]
# TODO: bruteforcing [range, 26]
# TODO: add colors
# TODO: cleanup code

# imports
import sys
import getopt
import getpass

# banner for cli
banner = """_________                                              _________ .__       .__                  
\_   ___ \_____    ____   ___________ _______         \_   ___ \|__|_____ |  |__   ___________ 
/    \  \/\__  \ _/ __ \ /  ___/\__  \\_  __ \  ______ /    \  \/|  \____ \|  |  \_/ __ \_  __ \\
\     \____/ __ \\  ___/ \___ \  / __ \|  | \/ /_____/ \     \___|  |  |_> >   Y  \  ___/|  | \/
 \______  (____  /\___  >____  >(____  /__|            \______  /__|   __/|___|  /\___  >__|   
        \/     \/     \/     \/      \/                       \/   |__|        \/     \/     """

# help menu for displaying argument options
help_menu = """
        Caesar-Cipher oneliners

        First Argument: Ciphering Process
        -e = encrypt
        -d = decrypt
        -b = bruteforce 

        Additional Arguments:
        -k <integer key> = key
        -t <plaintext>   = input file [.txt]
        -i <input file>  = input text
        -o <output file> = output file [output will be printed to screen by default]

        Example:
        file.py -e -k 5 -t hello 
        """

# symbols that can't be processed through the cipher
symbols = ['\n', '\t', ' ', '.', '?', '!', ',', '/', '\\', '<', '>', '|',
           '[', ']', '{', '}', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '`', '~', ':', ';', '"', "'", '0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9']

# generate path
path = f"{getpass.getuser()}@caesar-cipher $ "

# NOTE: determine whether extra characters are going through
# encrypts content
def encrypt_caesar(plain_content, encryption_key, print_cnt):
    # output variable
    output = ''
 
    # encryption process
    for character in plain_content:
        if character in symbols:
            output += character
        elif character.isupper():
            output += chr((ord(character) + int(encryption_key) - 65) % 26 + 65)
        else:
            output += chr((ord(character) + int(encryption_key) - 97) % 26 + 97)

    # output content to cli
    if print_cnt == True:
        print(f'Encrypted Content:\n{output}\n')

    # output content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(output)

# decrypts content
def decrypt_caesar(plain_content, encryption_key, print_cnt):
    # output variable
    output = ''
 
    # encryption process
    for character in plain_content:
        if character in symbols:
            output += character
        elif character.isupper():
            output += chr((ord(character) - int(encryption_key) - 65) % 26 + 65)
        else:
            output += chr((ord(character) - int(encryption_key) - 97) % 26 + 97)

    # outputs content to cli
    if print_cnt == True:
        print(f'Decrypted Content:\n{output}\n')

    # outputs content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(output)

# parse all arguments
def parser():
    opts, args = getopt.getopt(sys.argv[2:], 'k:f:t:o:', ['key', 'inputFile', 'inputText','outputFile'])
    arg_dict = {}

    # loop through arguments, assign them to dict [arg_dict]
    for opt, arg in opts:
        if opt == '-k':
            arg_dict['-k'] = int(arg)
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

    # check for arguments

    # one liners
    if argument_check == True:
        arguments = parser()

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

        try:
            # encrypts caesar
            if ciphering_process == '-e':
                encrypt_caesar(inputted_content, key, print_content)

            # decrypts caesar
            if ciphering_process == '-d':
                decrypt_caesar(inputted_content, key, print_content)

            # bruteforce caesar
            if ciphering_process == '-b':
                pass  # bruteforce
        
        except TypeError:
            print(f'[!!] No Key or Input was specified\n{help_menu}')

    # help menu 
    else:
        print(help_menu)

# main code
def caesar_main():

    # checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True

    cli(arguments_exist)

if __name__ == '__main__':
    caesar_main()
