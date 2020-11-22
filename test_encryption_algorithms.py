import unittest
from shift_encryption_algorithm import shiftEncryption, decryptShiftEncryption
from matrix_encryption_algorithm import matrixEncryptionAlgorithm, decryptMatrixEncryptionAlgorithm

class TestEncryptionAlgorithms(unittest.TestCase):
    def test_shiftEncryptionAlgorithm(self):
        '''test shift encryption algorithm'''
        # Test adding spaces in the middle 
        self.assertEqual(shiftEncryption('Hello World'), 'Khoor Zruog')
        # Test Various number of spaces
        self.assertEqual(shiftEncryption('Hello  World'), 'Khoor  Zruog')
        # Test adding spaces at the begining of the string
        self.assertEqual(shiftEncryption(' Hello World'), ' Khoor Zruog')
        # Test adding spaces at the end of the string
        self.assertEqual(shiftEncryption('Hello World '), 'Khoor Zruog ')
        # Test adding spaces at both ends
        self.assertEqual(shiftEncryption(' Hello World '), ' Khoor Zruog ')
        # Test sending empty string
        self.assertEqual(shiftEncryption(''), '')

    def test_decryptShiftEncryptedAlgorithm(self):
        '''test decryption for  shift encryption algorithm'''
        # Test adding spaces in the middle 
        self.assertEqual(decryptShiftEncryption('Khoor Zruog'), 'Hello World')
        # Test Various number of spaces
        self.assertEqual(decryptShiftEncryption('Khoor  Zruog'), 'Hello  World')
        # Test adding spaces at the begining of the string
        self.assertEqual(decryptShiftEncryption(' Khoor Zruog'), ' Hello World')
        # Test adding spaces at the end of the string
        self.assertEqual(decryptShiftEncryption('Khoor Zruog '), 'Hello World ')
        # Test adding spaces at both ends
        self.assertEqual(decryptShiftEncryption(' Khoor Zruog '), ' Hello World ')
        # Test sending empty string
        self.assertEqual(decryptShiftEncryption(''), '')
    
    def test_matrixEncryptionAlgorithm(self):
        self.assertEqual(
            matrixEncryptionAlgorithm('h'),
            [
                [6.0, 13.0, 6.0, 17.0, 11.0, 15.0, 11.0, 14.0, 18.0, 7.0, 12.0,
                 12.0, 15.0, 19.0, 15.0, 22.0]
            ]
        )
        # Test sending empty string
        self.assertEqual(
            matrixEncryptionAlgorithm(''),
            []
        )
    
    def test_decryptMatrixEncryptionAlgorithm(self):
        encrypted = matrixEncryptionAlgorithm('Hello World')
        self.assertEqual(
            decryptMatrixEncryptionAlgorithm(encrypted),
            'Hello World'
        )

if __name__ == '__main__':
    unittest.main()
