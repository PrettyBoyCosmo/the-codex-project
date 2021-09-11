#!/usr/bin/python

# main file for the the codex project
# created by : C0SM0

# TODO: beautify
# TODO: clean up
# TODO: import new ciphers

# imports
import sys
import os

# NOTE: '--' for long args

# help menu
help_menu = """
        The Codex Project oneliners

        First argument: Ciphers
        -c = caesar
        -v = vigenere

        Caesar Cipher:
            Second Argument: Ciphering Process
            -e = encrypt
            -d = decrypt
            -b = bruteforce [bruteforces using all possible keys by default]

            Additional Arguments:
            -k <integer key> = key [not required for bruteforcing '-b']
            -r <start,end>   = choose a range of keys to start and end the bruteforce
            -t <plaintext>   = input text, one string only
            -i <input file>  = input file [.txt is best]
            -o <output file> = output file [output will be printed to screen by default]

            Example:
            main.py -c -e -t hello -k 5

        Vigener Cipher:
            Second Argument:
            -e = encrypt
            -d = decrypt

            Additional Arguments:
            -k <string key> = key 
            -i <input file> = input file [.txt is best]
            -t <input text> = input text, one string only

            Example:
            main.py -v -e -t hello -k world
        """

# command line interface
def cli(argument_check):
    # one liners
    if argument_check == True:

        # check ciphering option
        ciphering_option = sys.argv[1]
        remaining_arguments = sys.argv[2:]
        string_args = ' '.join(remaining_arguments)

        # attempts to run caesar
        try:
            if ciphering_option == '-c':
                os.system(f'python3 ./ciphers/caesarCipher.py {string_args}')

            elif ciphering_option == '-v':
                os.system(f'python3 ./ciphers/vigenereCipher.py {string_args}')

            else:
                print('no ciphering option was added')

        # catches unspecified arguments
        except TypeError:
            print(f'[!!] No Key or Argument was specified\n{help_menu}')

    # help menu
    else:
        print(help_menu)

# main code
def codex_main():
    # checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True

    cli(arguments_exist)

# run main code
if __name__ == '__main__':
    codex_main()