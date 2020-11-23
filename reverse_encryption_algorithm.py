import sys
import requests

def reverseEncryption(text: str) -> str:
    '''encrypt text using reverse encryption algorithm'''
    if not text:
        return ''
    response = requests.post('http://backendtask.robustastudio.com/encode', data={ 'string' : text })
    responseJson = response.json()
    encryptedText = responseJson['string']
    return encryptedText

def decryptReverseEncryption(text: str) -> str:
    '''decrypt message encrypted by reverse encryption algorithm'''
    if not text:
        return ''
    response = requests.post('http://backendtask.robustastudio.com/decode', data={ 'string' : text })
    responseJson = response.json()
    decryptedText = responseJson['string']
    return decryptedText

if __name__ == "__main__":
    '''ask user for a text to encrypt in case of main'''
    args = sys.argv[1:]
    encryptedArgs = [] # array of encrypted values of the provided args
    for arg in args:
        encryptedValue = reverseEncryption(arg)
        encryptedArgs.append(encryptedValue)
    for i in range(len(encryptedArgs)):
        print(args[i], "->",encryptedArgs[i])
