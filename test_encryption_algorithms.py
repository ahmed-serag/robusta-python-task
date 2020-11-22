import unittest
from shift_encryption_algorithm import shiftEncryption
from matrix_encryption_algorithm import matrixEncryptionAlgorithm

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

if __name__ == '__main__':
    unittest.main()
