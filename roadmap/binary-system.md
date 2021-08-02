# BINARY SYSTEM | CODEX
> Blue Cosmo | 08/02/21
---

## Overview:
```
a python shell script to convert numeric values into binary [vice versa]
```

## Resources:
- python3

## Components:
- convert

## Roadmap:

## Extraneous:
- binary, a based-two, alpha-numeric system
- composed of two digits:
	-	1, on or true
	-	0, off or false
- a binary number is one byte, composed of 8 bits
```
Decimal : 28
Binary  : 00011100
```
---
Decimal --> Binary
- each bit in a binary number represents a value form 0-7, being squared by two
```
/----------------------------------------\
|Decimal | 28|   |   | 12| 4 | 0 |   |   |
|--------+---+---+---+---+---+---+---+---|
|Binary  | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
|--------+---+---+---+---+---+---+---+---|
|Exponet |2^7|2^6|2^5|2^4|2^3|2^2|2^1|2^0|
|--------+---+---+---+---+---+---+---+---|
|Value   |128| 64| 32| 16| 8 | 4 | 2 | 1 |
\----------------------------------------/
```
-   find the first value that can go into your decimal [from the left to your right] 
-   place a "1" in the binary section if the value can go into the decimal
-   list the decimal subtracted by the value, set this as your new decimal value 
-   rinse and repeat using your new decimal
---
Binary --> Decimal
- we are given this binary number `01011010`
- add the values under each "1" to get the decimal form
```
/----------------------------------------\
|Decimal |   | 64|   | 16| 8 |   | 2 |   |
|--------+---+---+---+---+---+---+---+---|
|Binary  | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
|--------+---+---+---+---+---+---+---+---|
|Exponet |2^7|2^6|2^5|2^4|2^3|2^2|2^1|2^0|
|--------+---+---+---+---+---+---+---+---|
|Value   |128| 64| 32| 16| 8 | 4 | 2 | 1 |
\----------------------------------------/
```
- 64 + 16 + 8 + 2 = 90