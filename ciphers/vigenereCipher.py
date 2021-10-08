#!/usr/bin/python

# vigenere cipher package for the the codex project
# thanks to Andrew Paul for the ...
# https://github.com/drewp41
# created by : C0SM0

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
            -d = decrypt [known key]
            -u = decrypt [unkown key]

            Additional Arguments:
            -k <string key> = key 
            -i <input file> = input file [.txt is best]
            -t <input text> = input text, one string only
            -l <maximum key length> = maximum guess length for unkown key decryption

            Example:
            main.py -v -e -t hello -k world
            main.py -v -u -i file.txt 
            """

# letters for encryption process
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MAX_KEY_LENGTH = 20
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# symbols that can't be processed through the cipher
SYMBOLS = ['\n', '\t', ' ', '.', '?', '!', ',', '/', '\\', '<', '>', '|',
           '[', ']', '{', '}', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '`', '~', ':', ';', '"', "'", '0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9']

# Array containing the relative frequency of each letter in the English language
english_frequences = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
					  0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
					  0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
					  0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

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
        print('Output written to file sucessfully')

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
        print('Output written to file sucessfully')

# gets index through councidence
def get_index_c(ciphertext):
	
	N = float(len(ciphertext))
	frequency_sum = 0.0

	# using Index of Coincidence formula
	for letter in alphabet:
		frequency_sum += ciphertext.count(letter) * (ciphertext.count(letter)-1)

	# using Index of Coincidence formula
	ic = frequency_sum/(N*(N-1))
	return ic

# returns key length with highest average
def get_key_length(ciphertext):
	ic_table=[]

    # iterates through [possible] key sequences
	for guess_len in range(MAX_KEY_LENGTH):
		ic_sum = 0.0
		avg_ic = 0.0
		for i in range(guess_len):
			sequence = ''
			# breaks the ciphertext into sequences
			for j in range(0, len(ciphertext[i:]), guess_len):
				sequence += ciphertext[i+j]
			ic_sum += get_index_c(sequence)

		if not guess_len == 0:
			avg_ic = ic_sum / guess_len
		ic_table.append(avg_ic)

	# returns the most likeyly key length
	best_guess = ic_table.index(sorted(ic_table, reverse = True)[0])
	second_best_guess = ic_table.index(sorted(ic_table, reverse = True)[1])

	if best_guess % second_best_guess == 0:
		return second_best_guess
	else:
		return best_guess

# get the letter of the key that needs to be shifted
def freq_analysis(sequence):
	all_chi_squareds = [0] * 26

	for i in range(26):
		chi_squared_sum = 0.0

		sequence_offset = [chr(((ord(sequence[j])-97-i)%26)+97) for j in range(len(sequence))]
		v = [0] * 26

		# count the numbers of each letter in the sequence_offset already in ascii
		for l in sequence_offset:
			v[ord(l) - ord('a')] += 1
            
		# divide the array by the length of the sequence to get the frequency percentages
		for j in range(26):
			v[j] *= (1.0/float(len(sequence)))

		# compate frequencies
		for j in range(26):
			chi_squared_sum+=((v[j] - float(english_frequences[j]))**2)/float(english_frequences[j])

		# append it all
		all_chi_squareds[i] = chi_squared_sum

	# return the letter of the key that it needs to be shifted by
	shift = all_chi_squareds.index(min(all_chi_squareds))
	return chr(shift+97)

# gets key
def get_key(ciphertext, key_length):
	key = ''

	# calculate letter frequency table for each letter of the key
	for i in range(key_length):
		sequence = ''

		# breaks the ciphertext into sequences
		for j in range(0,len(ciphertext[i:]), key_length):
			sequence += ciphertext[i+j]

		key += freq_analysis(sequence)

	return key

# decrypts viginere with unkown key
def unkown_key(plain_content, print_cnt):
    ciphertext = ''.join(x.lower() for x in plain_content if x.isalpha())	

    # tries to get key
    try:
        # calculating the key data
        key_length = get_key_length(ciphertext)
        key = get_key(ciphertext, key_length)

        # outputting key data
        print(f'Most Probable Key Length: {key_length}')
        print(f'Key: {key}\n')

        # decrypting vigenere
        decrypt_vigenere(ciphertext, key, print_cnt)
    
    # if the plaintext was too small
    except ZeroDivisionError:
        print('The ciphertext you entered was to small for this algorithm\nPlease add more ciphertext')

# parses arguments
def vigenere_parser():
    opts, args = getopt.getopt(sys.argv[2:], 'k:i:t:o:r:', ['key', 'inputFile', 'inputText', 'outputFile', 'range'])
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
    print(banner)

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
                # tries to read file
                try:
                    inputted_content = open(arguments.get('-i'), 'r').read()

                # file does not exist
                except FileNotFoundError:
                    print('[!!] The attached file does not exist')

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

                # decrypts with unkown key
                if  ciphering_process == '-u':
                    unkown_key(inputted_content, print_content)

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