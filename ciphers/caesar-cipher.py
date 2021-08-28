#!/usr/bin/python

# caesar cipher package for the the codex project
# created by : C0SM0

# NOTE: if this shit doesn't work, use argparse

# TODO: add colors

# argument parsing
"""
print(sys.argv[0])
print(sys.argv[1])

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg
"""

# arguments
# NOTE: incorportate range into -b or -r
"""

file.py CIPHER[-e,-d,-b] KEY[-k] INPUT[-t,-t] OUTPUT[-o]

-e = encrypt
-d = decrypt
-b = bruteforce 

-k = key

-t = input file [.txt]
-t = input text
-o = output file
"""

# imports
import sys
import getopt
import getpass

banner = """_________                                              _________ .__       .__                  
\_   ___ \_____    ____   ___________ _______         \_   ___ \|__|_____ |  |__   ___________ 
/    \  \/\__  \ _/ __ \ /  ___/\__  \\_  __ \  ______ /    \  \/|  \____ \|  |  \_/ __ \_  __ \\
\     \____/ __ \\  ___/ \___ \  / __ \|  | \/ /_____/ \     \___|  |  |_> >   Y  \  ___/|  | \/
 \______  (____  /\___  >____  >(____  /__|            \______  /__|   __/|___|  /\___  >__|   
        \/     \/     \/     \/      \/                       \/   |__|        \/     \/     """

# argument variables
# key = 0
# input_file = ''
# input_text = ''
# output_file = ''
# output_text = ''


# symbols that can't be processed through the cipher
symbols = ['\n', '\t', ' ', '.', '?', '!', ',', '/', '\\', '<', '>', '|',
           '[', ']', '{', '}', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '`', '~', ':', ';', '"', "'", '0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9']

# generate path
path = f"{getpass.getuser()}@codex $ "

# encrypts text
def encrypt_caesar(plain_content, encryption_key, print_cnt):
    # output variable
    output = ''
    output_text = ''
 
    # encryption process
    for character in plain_content:
        if character in symbols:
            output += character
        elif character.isupper():
            output += chr((ord(character) + int(encryption_key) - 65) % 26 + 65)
        else:
            output += chr((ord(character) + int(encryption_key) - 97) % 26 + 97)
    
    # NOTE: match lengths of ciphertext to see if extra characters exist
    # remove extra character
    # text_length = len(output)
    # for num in range(0, text_length):
    #     if num != text_length -1:
    #         output_text += output[num]

    # output content
    if print_cnt == True:
        print(output)
    else:
        with open(print_cnt, 'w') as f:
            f.write(output)

# parse all arguments
# TODO: fix me, i won't add all of the args
def parser():
    opts, args = getopt.getopt(sys.argv[2:], 'k:f:t:o:', ['key', 'inputFile', 'inputText','outputFile'])
    arg_dict = {}

    # TODO: fix this shit
    # if ('iF' and '-t') in opts:
    #     pass  # end this shit

    for opt, arg in opts:
        if opt == '-k':
            arg_dict['-k'] = int(arg)
        # input options
        if opt == '-f':
            arg_dict['-f'] = arg
        if opt == '-t':
            arg_dict['-t'] = arg
        # output options
        if opt == '-o':
            arg_dict['-o'] = arg

    print(arg_dict)
    return arg_dict

# command line interface
def cli(argument_check):
    # display banner
    print(f'{banner}\n\n')

    # check for arguments
    # TODO: check if args are empty
    if argument_check == True:
        arguments = parser()

        key = arguments.get('-k')
        inputted_content = arguments.get('-t')
        print_content = True
        
        # checks users output type
        if ('-f' in arguments):
            inputted_content = open(arguments.get('-f'), 'r').read()

        # checks if output was specified
        if ('-o' in arguments):
            print_content = arguments.get('-o')

        # check ciphering process
        ciphering_process = sys.argv[1]
        if ciphering_process == '-e':
            encrypt_caesar(inputted_content, key, print_content)

        if ciphering_process == '-d':
            pass  # decrypt caesar

        if ciphering_process == '-b':
            pass  # bruteforce

    else:
        # display options
        print('Options:\n\teF - Encrypt File\n\teT - Encrypt Text\n\tdF - Decrypt File\n\tdT - Decrypt Text\n\tbF Bruteforce File\n\tbT - Bruteforce Text\n')
        option = input(f'{path}[~] Option :')

        # option, encrypt file
        if option == 'eF':
            plainfile_input = input(f'{path}[~] Enter File Name : ')
            shift_key = input(f'{path}[~] Enter Encryption Key : ')
            encrypt_caesar(plainfile_input, int(shift_key))

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
