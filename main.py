#!/usr/bin/python

# main file for the the codex project
# created by : C0SM0

# imports
import sys
import getopt
import getpass
import os
from ciphers import caesarCipher  # imports caesar

# NOTE: '--' for long args

# help menu
help_menu = """
        The Codex Project oneliners

        First argument: Ciphers
        -c = caesar

        Caesar Cipher:
            Second Argument: Ciphering Process
            -e = encrypt
            -d = decrypt
            -b = bruteforce [bruteforces using all possible keys by default]

            Additional Arguments:
            -k <integer key> = key [not required for bruteforcing '-b']
            -r <start,end>   = choose a range of keys to start and end the bruteforce
            -t <plaintext>   = input file [.txt]
            -i <input file>  = input text
            -o <output file> = output file [output will be printed to screen by default]
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