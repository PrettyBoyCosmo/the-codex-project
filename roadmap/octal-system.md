# OCTAL SYSTEM | CODEX
> Blue Cosmo | 08/02/21
---

## Overview:
```
a python shell script to convert numeric values into octal [vice versa]
```

## Resources:
- python3

## Components:
- convert

## Roadmap:

## Extraneous:
- octal, a based-8, numeric system
- composed of eight digits:
	-	0, 1, 2, 3, 4, 5, 6, 7
```
Decimal : 28
Octal   : 00000034 [34]
```
---
Decimal --> Octal
```markdown
| Decimal |    132    |         |        |       |     | 4   |     | 0   |
|---------|-----------|---------|--------|-------|-----|-----|-----|-----|
| Octal   | 0         | 0       | 0      | 0     | 0   | 2   | 0   | 4   |
| Base    | 8^7       | 8^6     | 8^5    | 8^4   | 8^3 | 8^2 | 8^1 | 8^0 |
| Value   | 2,097,152 | 262,144 | 32,768 | 4,096 | 512 | 64  | 8   | 1   |
```
-   find the first value that can go into your decimal [from the left to your right] 
-   list the number of times taht value can go into your decimal in the octal section
-   list the decimal subtracted by the (decimal\*octal) sections, set this as your new decimal value 
-   rinse and repeat using your new decimal
---
Octal --> Decimal
```markdown
| Decimal |    132    |         |        |       |     | 128 |     | 4   |
|---------|-----------|---------|--------|-------|-----|-----|-----|-----|
| Octal   | 0         | 0       | 0      | 0     | 0   | 2   | 0   | 4   |
| Base    | 8^7       | 8^6     | 8^5    | 8^4   | 8^3 | 8^2 | 8^1 | 8^0 |
| Value   | 2,097,152 | 262,144 | 32,768 | 4,096 | 512 | 64  | 8   | 1   |
```
- multiply each value to the octal above it
- add these new values together to get the decimal
	- 128 + 4 = 132