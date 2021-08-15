# HEXADECIMAL SYSTEM | CODEX
> Blue Cosmo | 08/02/21
---

## Overview:
```
a python shell script to convert numeric values into hexadecimal [vice versa]
```

## Resources:
- python3
- functions
```python
# function for hex conversion
hex()

# function for integer conversion
int(hexadecimal, 16)
```
## Components:
- convert

## Roadmap:

## Extraneous:
- binary, a based-sixteen, alpha-numeric system
- composed of sixteen digits:
	- 0-9 - integers
	- 10-15 - alphanumeric [prevents confusion] 
		- 10 - A
		- 11 - B
		- 12 - C
		- 13 - D
		- 14 - E
		- 15 - F
```
Decimal      : 28
Hexadecimal  : 1C
```
---
Decimal --> Hexadecimal
```markdown
| Decimal     |      39     |            |           |        |       |      | 7    | 0    |
|-------------|-------------|------------|-----------|--------|-------|------|------|------|
| Hexadecimal | 0           | 0          | 0         | 0      | 0     | 0    | 2    | 7    |
| Base        | 16^7        | 16^6       | 16^5      | 16^4   | 16^3  | 16^2 | 16^1 | 16^0 |
| Value       | 268,435,456 | 16,777,216 | 1,048,576 | 65,536 | 4,096 | 256  | 16   | 1    |
```
-   find the first value that can go into your decimal [from the left to your right] 
-   list the number of times that value can go intor the decimal in the hexadecimal section
-   list the decimal subtracted by (decimal\*hexadecimal) sections, set this as your new decimal value 
-   rinse and repeat using your new decimal
---
Hexadecimal --> Decimal
```markdown
| Decimal     |     350     |            |           |        |       | 256  | 80   | 14   |
|-------------|-------------|------------|-----------|--------|-------|------|------|------|
| Hexadecimal | 0           | 0          | 0         | 0      | 0     | 1    | 5    | E    |
| Base        | 16^7        | 16^6       | 16^5      | 16^4   | 16^3  | 16^2 | 16^1 | 16^0 |
| Value       | 268,435,456 | 16,777,216 | 1,048,576 | 65,536 | 4,096 | 256  | 16   | 1    |
```
- multiply each value by its respective hexadecimal and add the results together