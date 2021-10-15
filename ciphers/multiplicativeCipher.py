#!/usr/bin/python

# reverse cipher package for the the codex project
# created by : C0SM0

# imports
import sys
import getopt

# banner
banner = """
   _____        .__   __  .__          _________ .__       .__                  
  /     \\  __ __|  |_/  |_|__|         \\_   ___ \\|__|_____ |  |__   ___________ 
 /  \\ /  \\|  |  \\  |\\   __\\  |  ______ /    \\  \\/|  \\____ \\|  |  \\_/ __ \\_  __ \\
/    Y    \\  |  /  |_|  | |  | /_____/ \\     \\___|  |  |_> >   Y  \\  ___/|  | \\/
\\____|__  /____/|____/__| |__|          \\______  /__|   __/|___|  /\\___  >__|   
        \\/                                     \\/   |__|        \\/     \\/      
"""

# help menu for ciphering options
help_menu = """
        Multiplicative-Cipher Arguments:

        First Argument: Ciphering Process
        -e = encrypt
        -d = decrypt

        Additional Arguments:
        -k <integer key> = key 
        -t <plaintext>   = input text 
        -i <input file>  = input file [.txt]
        -o <output file> = output file [output will be printed to screen by default]

        Example:
        main.py -m -e -k 7 -t hello 
        """

# symbols that can't be processed through the cipher
symbols = ['\n', '\t', ' ', '.', '?', '!', ',', '/', '\\', '<', '>', '|',
           '[', ']', '{', '}', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '`', '~', ':', ';', '"', "'", '0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9']

index_dict = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25,
}

# gets index from letter
def get_index(letter):
    for l, i in index_dict.items():
        if letter == l:
            return i

# gets letter from index
def get_letter(index):
    for l, i in index_dict.items():
        if index == i:
            return l

# gets inverse for decryption
def inverse(a):
    for x in range(1, 26):
        if (((a%26) * (x%26)) % 26 == 1):
            return x
    return -1

# encrypts multiplicative cipher
def encrypt_multiplicative(plain_content, encryption_key, print_cnt):
    # output variable
    output = ''

    # encryption process
    for character in plain_content:

        if character in symbols:
            output += character

        elif character.isupper():
            index = get_index(character.lower())
            new_index = (index * encryption_key) % 26
            cipher_character = get_letter(new_index)
            output += cipher_character.upper()

        else:
            index = get_index(character)
            new_index = (index * encryption_key) % 26
            cipher_character = get_letter(int(new_index))
            output += cipher_character

    # output content to cli
    if print_cnt == True:
        print(f'Encrypted Content:\n{output}\n')

    # output content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(output)
        print('Output written to file sucessfully')


# decrypts multiplicative cipher
def decrypt_multiplicative(plain_content, decryption_key, print_cnt):
    # output variable
    output = ''
    inverse_key = inverse(decryption_key)
 
    # decryption process
    for character in plain_content:

        if character in symbols:
            output += character

        elif character.isupper():
            index = get_index(character.lower())
            new_index = (index * inverse_key) % 26
            cipher_character = get_letter(new_index)
            output += cipher_character.upper()

        else:
            index = get_index(character)
            new_index = (index * inverse_key) % 26
            cipher_character = get_letter(new_index)
            output += cipher_character

    # output content to cli
    if print_cnt == True:
        print(f'Decrypted Content:\n{output}\n')

    # output content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(output)
        print('Output written to file sucessfully')

# parses arguments for ciphering process
def multiplicative_parser():
    opts, args = getopt.getopt(sys.argv[2:], 'k:i:t:o:r:', ['key', 'inputFile', 'inputText', 'outputFile', 'range'])
    arg_dict = {}

    # loop through arguments, assign them to dict [arg_dict]
    for opt, arg in opts:
        # processing options
        if opt == '-k':
            arg_dict['-k'] = int(arg)
        if opt == '-r':
            arg_dict['-r'] = arg.split(',')
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
    print(banner)

    # one liners
    if argument_check == True:

        # tries to get all arguments
        try:
            arguments = multiplicative_parser()

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
                # tries to read file
                try:
                    inputted_content = open(arguments.get('-i'), 'r').read()

                # file does not exist
                except FileNotFoundError:
                    print('[!!] The attached file does not exist')

            # checks if output was specified
            if ('-o' in arguments):
                print_content = arguments.get('-o')

            # checks if range was specified
            if '-r' in arguments:   
                range = arguments.get('-r', False)

            # check ciphering process
            ciphering_process = sys.argv[1]

            # attempts to run cipher
            try:
                # encrypts caesar
                if ciphering_process == '-e':
                    encrypt_multiplicative(inputted_content, key, print_content)

                # decrypts caesar
                if ciphering_process == '-d':
                    decrypt_multiplicative(inputted_content, key, print_content)

                # bruteforce caesar
                if ciphering_process == '-b':
                    range = range if '-r' in arguments else False
                    if range == False:
                        bruteforce_caesar(inputted_content, print_content)
                    else:
                        bruteforce_caesar(inputted_content, print_content, int(range[0]), int(range[1])+1)

            # catches unspecified arguments
            except TypeError:
                print(f'[!!] No Key or Argument was specified\n{help_menu}')

    # help menu 
    else:
        print(help_menu)

# main code
def multiplicative_main():

    # checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True

    cli(arguments_exist)

# runs main function if file is not being imported
if __name__ == '__main__':
    multiplicative_main()

