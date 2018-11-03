# Ormuco tests

All tests were made using Python 3.7 (conda virtual env) and default libraries.


# Question A

A program that accepts two lines (x1, x2) and (x3, x4) on the x-asis and returns whether they overlap. 
Return True if overlap.


## Usage

```bash
python question_a.py -l1 <x1> <x2> -l2 <x3> <x4>
```

# Question B

A software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other.

## Usage
```bash
python question_b.py <str1> <str>
```
## Examples
```bash
python queston_b.py '2.1' '2.1'
2.1 == 2.1
python queston_b.py '1.2' '2.1'
1.2 < 2.1
python queston_b.py '3.9' '3.2'
3.9 > 3.2
```

## Testing
```bash
python tests_question_b.py
```

# Question C
