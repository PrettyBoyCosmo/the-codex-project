# VIGENER CIPHER | CODEX
> Blue Cosmo | 08/02/21
---

## Overview:
```
a python shell script to encrypt and decrypt vigenere
```

## Resources:
- python3

## Components:
- encryption
- decryption
- advanced
	- encryption
	- decryption
- key decoding
	- advanced key decoding

## Roadmap:

## Extraneous:
- aka polyalphabetic cipher
- invented by Giovan Battisa Bellaso in 1553
	- a more advanced version was published byBlaise de Vigenere
- relies on the index of the letter withing the key
---

### Example:
we start with our indexing chart, a little different than the one for the caesar cipher
```
Indexing:
/---------------------------------------------------\
| A | B | C | D | E | F | G | H | I | J | K | L | M |
|---+---+---+---+---+---+---+---+---+---+---+---+---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12|
|---+---+---+---+---+---+---+---+---+---+---+---+---|
| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---+---+---+---+---+---+---+---+---+---+---+---+---|
| 13| 14| 15| 16| 17| 18| 19| 20| 21| 22| 23| 24| 25|
\---------------------------------------------------/
```
for this example, we will be using "KEY" as our key
	- our key has the following indexes [these will be important]
```
/-----------\
| K | E | Y |
|---+---+---|
| 10| 4 | 24|
\-----------/
```
- now we can start to encrypt some plaintext, we will choose the text "ENCRYPT"
- we must first find the indexes of the plaintext's characters
```
/---------------------------\
| E | N | C | R | Y | P | T |
|---+---+---+---+---+---+---|
| 4 | 13| 2 | 17| 24| 15| 19|
\---------------------------/
```
we can now comibne them to the respective index's of our key
```
/---------------------------\
| E | N | C | R | Y | P | T | <-- PLAINTEXT
|---+---+---+---+---+---+---| 
| 4 | 13| 2 | 17| 24| 15| 19| <-- PLAINTEXT INDEXES
|---+---+---+---+---+---+---|
|+10| +4|+24|+10| +4|+24|+10| <-- KEY
|---+---+---+---+---+---+---|
| 14| 17| 0 | 1 | 2 | 13| 3 | <-- CIPHERTEXT INDEXES
|---+---+---+---+---+---+---|
| O | R | A | B | C | N | D | <-- CIPHERTEXT
\---------------------------/
```
now we can just reverse the process by subtracting the key values from the plaintext
```
/---------------------------\
| O | R | A | B | C | N | D | <-- CIPHERTEXT
|---+---+---+---+---+---+---| 
| 14| 17| 0 | 1 | 2 | 13| 3 | <-- CIPHERTEXT INDEXES
|---+---+---+---+---+---+---|
|-10| -4|-24|-10| -4|-24|-10| <-- KEY
|---+---+---+---+---+---+---|
| 4 | 13| 2 | 17| 24| 15| 19| <-- PLAINTEXT INDEXES
|---+---+---+---+---+---+---|
| E | N | C | R | Y | P | T | <-- PLAINTEXT
\---------------------------/
```