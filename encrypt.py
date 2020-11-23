import sys
from shift_encryption_algorithm import shiftEncryption, decryptShiftEncryption
from matrix_encryption_algorithm import matrixEncryptionAlgorithm, decryptMatrixEncryptionAlgorithm
from reverse_encryption_algorithm import reverseEncryption, decryptReverseEncryption

validAlgorithms = ['shift_encryption', 'matrix_encryption', 'reverse_encryption']

def validateAlgorithm(algorithm: str) -> bool:
    return algorithm.lower() in  validAlgorithms

def validateMethod(method: str) -> bool:
    return method.lower() == 'encrypt' or method.lower() == 'decrypt'

if __name__ == "__main__":
    '''ask user for a text to encrypt in case of main'''
    args = sys.argv[1:]
    originalText = sys.argv[1]
    algorithm = sys.argv[2]
    method = sys.argv[3]
    valid = True
    modifiedText = None
    
    if not validateAlgorithm(algorithm):
        print("Please enter a valid algorithm")
        valid = False
    if not validateMethod(method):
        print("Please enter a valid method")
        valid = False

    if valid:
        if algorithm.lower() == 'shift_encryption':
            if method.lower() == 'encrypt':
                modifiedText = shiftEncryption(originalText)
            else:
                modifiedText = decryptShiftEncryption(originalText)
        elif algorithm.lower() == 'matrix_encryption':
            if method.lower() == 'encrypt':
                modifiedText = matrixEncryptionAlgorithm(originalText)
            else:
                modifiedText = decryptMatrixEncryptionAlgorithm(originalText)
        else:
            if method.lower() == 'encrypt':
                modifiedText = reverseEncryption(originalText)
            else:
                modifiedText = decryptReverseEncryption(originalText)
    if modifiedText:
        print(originalText, '->', modifiedText)
    