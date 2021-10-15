#!/usr/bin/python

# reverse cipher package for the the codex project
# created by : C0SM0

# imports
import sys
import getopt

# banner
banner = """
__________                                                 _________ .__       .__                  
\\______   \\ _______  __ ___________  ______ ____           \\_   ___ \\|__|_____ |  |__   ___________ 
 |       _// __ \\  \\/ // __ \\_  __ \\/  ___// __ \\   ______ /    \\  \\/|  \\____ \\|  |  \\_/ __ \\_  __ \\
 |    |   \\  ___/\\   /\\  ___/|  | \\/\\___ \\\\  ___/  /_____/ \\     \\___|  |  |_> >   Y  \\  ___/|  | \\/
 |____|_  /\\___  >\\_/  \\___  >__|  /____  >\\___  >          \\______  /__|   __/|___|  /\\___  >__|   
        \\/     \\/          \\/           \\/     \\/                  \\/   |__|        \\/     \\/      
"""

# help menu for ciphering process
help_menu = """
        Reverse-Cipher Arguments:

        Additional Arguments:
        -t <plaintext>   = input file [.txt]
        -i <input file>  = input text
        -o <output file> = output file [output will be printed to screen by default]

        Example:
        main.py -t hello 
"""

# encrypt reverse
def reverse(plain_content, print_cnt):
    output = plain_content[::-1]

    # output content to cli
    if print_cnt == True:
        print(f'Reversed Content:\n{output}\n')

    # output content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(output)
        print('Output written to file sucessfully')

# parse all arguments
def reverse_parser():
    opts, args = getopt.getopt(sys.argv[1:], 'i:t:o:', ['inputFile', 'inputText', 'outputFile'])
    arg_dict = {}

    # loop through arguments, assign them to dict [arg_dict]
    for opt, arg in opts:
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
            arguments = reverse_parser()

        # catches arguments with no value
        except getopt.GetoptError:
            print(f'[!!] No value was given to your argument\n{help_menu}')

        # continues with recieved arguments
        else:    
            # getting variables for ciphering process
            inputted_content = arguments.get('-t')
            print_content = True
            
            # checks users output type
            if ('-i' in arguments):
                # tries to read file
                try:
                    inputted_content = open(arguments.get('-i'), 'r').read()
                    inputted_content = inputted_content[2::2]

                # file does not exist
                except FileNotFoundError:
                    print('[!!] he attached file does not exist')

            # checks if output was specified
            if ('-o' in arguments):
                print_content = arguments.get('-o')

            # attempts to run cipher
            try:
                reverse(inputted_content, print_content)

            # catches unspecified arguments
            except TypeError:
                print(f'[!!] No Key or Argument was specified\n{help_menu}')

    # help menu 
    else:
        print(help_menu)

# main code
def reverse_main():

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
    reverse_main()
