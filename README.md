# BackEnd Python Tasks

## Pre-requisites

- [python 3.8 or higher](https://www.python.org)

## Shift encrypted algorithm

shift every character in the provided string by 3 characters so if word contains letter “A” in the
encrypted string, “A” will be replaced by “D”.


### Usage

- run the python script `shift-encryption-algorithm.py` with the text you need to run as arguments

```bash
python shift-encryption-algorithm.py 'Hello world'
```

- pass multiple arguments for multiple text

```bash
python shift-encryption-algorithm.py 'Hello world' 'encrypt me'
```

the script is expected to print the encrypted text for each argument as the following:

```bash
python shift-encryption-algorithm.py 'Hello world' 'encrypt me'
Hello world -> Khoor zruog
encrypt me -> hqfu|sw ph
```

## Matrix Encryption Algorithm

Convert each character of the string to the Binary representation of ASCII character (16
characters) and multiply it by the key matrix

### Usage

- run the python script `matrix-encryption-algorithm.py` with the text you need to run as arguments

```bash
python shift-encryption-algorithm.py 'Hello world'
```

- pass multiple arguments for multiple text

```bash
python shift-encryption-algorithm.py 'Hello world' 'encrypt me'
```

the script is expected to print the encrypted matrix value for each argument.
