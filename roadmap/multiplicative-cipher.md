# MULTIPLICATIVE CIPHER | CODEX
> Blue Cosmo | DATE
---

## Overview:
```
a python shell script for the multiplicative cipher
```

## Resources:
- python3

## Components:
- encryption
- decryption
- bruteforcing
- file and text input
- one liners

## Roadmap:

## Extraneous:
- uses multiplication to create cipher text
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
---

### Algorithms:
- Encryption - `(index * key) % 26 = CIPHER-INDEX`
- Decryption - ``
- Bruteforcing - `iterate through each key to find the new index`