# CAESAR CIPHER | CODEX
> Blue Cosmo | 08/02/21
---

## Overview:
```
a python shell script to encrypt, decrypt, and bruteforce the caesar cipher
```

## Resources:
- python3

## Components:
- encryption
- decryption
- bruteforcing
- file and text input

## Roadmap:
- 

## Extraneous:
- named after Julius Caesar
- works through an index change down the alphabet
---

### Example:
Without Cipher - [shift of 0]
```markdown
| A | B | C | D |
|---|---|---|---|
| 1 | 2 | 3 | 4 |
```

With Cipher - [shift of 1]
```markdown
| B | C | D | E |
|---|---|---|---|
| 1 | 2 | 3 | 4 |
```

- Plaintext - "Hello, World!"
- Ciphertext - "Ifmmp, Xpsme!"
---

### Algorithms:
- Encryption - `C = (X + N) % 26`
- Decryption - `C = (X - N) % 26`
---
- C - plaintext or ciphertext character
- X - index of character
- N - number of indexes we need to replace [the encryption key]
---

### Unicode:
- computer don't understand english alphabet indexing, but they do understand unicode
- A - 64
- a - 97
```
ord() - matches character to unicode index
chr() - matches index to unicode character
```

### Python Algorithms:
Encryption:
```python
# uppercase
plaintext += chr((ord(letter) + shift - 65) % 26 + 65)

# lowercase
plaintext += chr((ord(letter) + shift - 97) % 26 + 97)
```
Decryption:
```python
# uppercase
ciphertext += chr((ord(letter) - shift - 65) % 26 + 65)

# lowercase
ciphertext += chr((ord(letter) - shift - 97) % 26 + 97)
```