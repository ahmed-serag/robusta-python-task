import sys
from shift_encryption_algorithm import shiftEncryption, decryptShiftEncryption
from matrix_encryption_algorithm import matrixEncryptionAlgorithm, decryptMatrixEncryptionAlgorithm

def validateAlgorithm(algorithm: str) -> bool:
    return algorithm.lower() == 'shift_encryption' or algorithm.lower() == 'matrix_encryption'

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
        else:
            if method.lower() == 'encrypt':
                modifiedText = matrixEncryptionAlgorithm(originalText)
            else:
                modifiedText = decryptMatrixEncryptionAlgorithm(originalText)

    if modifiedText:
        print(originalText, '->', modifiedText)
    