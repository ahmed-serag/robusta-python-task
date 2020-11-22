import sys

def shiftEncryption(text: str) -> str:
    '''encrypt text using shiftEncrypting algorithm with base 3'''
    encryptedWords = []
    words = text.split(' ')
    for word in words:
        encrypted = ''
        for c in word:
            asciiValue = ord(c) # ascii value of the char
            encrypted += chr(asciiValue + 3) # shift it by 3 and return it
        encryptedWords.append(encrypted)
    return ' '.join(encryptedWords)

def decryptShiftEncryption(text: str) -> str:
    '''decrypt message encrypted by shiftEncryption'''
    decryptedWords = []
    words = text.split(' ')
    for word in words:
        decrypted = ''
        for c in word:
            asciiValue = ord(c) # ascii value of the char
            decrypted += chr(asciiValue - 3) # shift it by 3 and return it
        decryptedWords.append(decrypted)
    return ' '.join(decryptedWords)

if __name__ == "__main__":
    '''ask user for a text to encrypt in case of main'''
    args = sys.argv[1:]
    encryptedArgs = [] # array of encrypted values of the provided args
    for arg in args:
        encryptedValue = shiftEncryption(arg)
        encryptedArgs.append(encryptedValue)
    for i in range(len(encryptedArgs)):
        print(args[i], "->",encryptedArgs[i])
