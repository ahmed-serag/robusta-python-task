import sys

keyMatrix = [
    [8.000, 4.000, 4.000, 8.000, 7.000, 8.000, 7.000, 1.000,
     9.000, 4.000, 1.000, 1.000, 1.000, 6.000, 3.000, 0.000],
    [9.000, 6.000, 0.000, 0.000, 5.000, 4.000, 2.000, 3.000,
     1.000, 4.000, 7.000, 8.000, 2.000, 6.000, 0.000, 5.000],
    [0.000, 7.000, 2.000, 4.000, 4.000, 9.000, 4.000, 0.000,
     1.000, 1.000, 3.000, 1.000, 2.000, 7.000, 0.000, 7.000],
    [9.000, 5.000, 9.000, 7.000, 8.000, 3.000, 2.000, 6.000,
     5.000, 5.000, 6.000, 1.000, 6.000, 8.000, 4.000, 6.000],
    [5.000, 1.000, 7.000, 1.000, 1.000, 0.000, 2.000, 9.000,
     8.000, 6.000, 0.000, 9.000, 5.000, 5.000, 6.000, 3.000],
    [3.000, 9.000, 8.000, 4.000, 0.000, 4.000, 5.000, 0.000,
     1.000, 0.000, 9.000, 6.000, 6.000, 7.000, 0.000, 7.000],
    [7.000, 1.000, 8.000, 3.000, 1.000, 0.000, 2.000, 1.000,
     0.000, 1.000, 3.000, 3.000, 7.000, 5.000, 5.000, 3.000],
    [6.000, 1.000, 4.000, 3.000, 9.000, 5.000, 1.000, 2.000,
     9.000, 7.000, 5.000, 4.000, 2.000, 5.000, 0.000, 0.000],
    [9.000, 3.000, 7.000, 5.000, 0.000, 4.000, 4.000, 2.000,
     5.000, 9.000, 3.000, 1.000, 6.000, 6.000, 7.000, 4.000],
    [3.000, 2.000, 3.000, 4.000, 4.000, 1.000, 5.000, 1.000,
     1.000, 0.000, 6.000, 5.000, 1.000, 2.000, 8.000, 3.000],
    [6.000, 6.000, 0.000, 7.000, 2.000, 7.000, 1.000, 0.000,
     2.000, 6.000, 4.000, 2.000, 2.000, 9.000, 4.000, 0.000],
    [9.000, 7.000, 7.000, 3.000, 1.000, 5.000, 1.000, 0.000,
     9.000, 5.000, 4.000, 9.000, 3.000, 6.000, 6.000, 0.000],
    [6.000, 4.000, 9.000, 3.000, 9.000, 7.000, 8.000, 8.000,
     3.000, 8.000, 2.000, 1.000, 5.000, 9.000, 5.000, 2.000],
    [4.000, 2.000, 1.000, 7.000, 0.000, 2.000, 7.000, 9.000,
     2.000, 8.000, 5.000, 7.000, 6.000, 7.000, 1.000, 9.000],
    [4.000, 2.000, 4.000, 2.000, 9.000, 4.000, 6.000, 2.000,
     2.000, 6.000, 3.000, 0.000, 6.000, 7.000, 3.000, 2.000],
    [5.000, 9.000, 1.000, 4.000, 2.000, 3.000, 1.000, 0.000,
     0.000, 8.000, 5.000, 6.000, 9.000, 9.000, 7.000, 0.000]
] # Key matrix used to encrypt the text

inverseMatrix = [
    [8.76987304e-02, 1.06508424e-01, -3.58378895e-02, -1.82126146e-02,
       2.92822059e-02, 9.76853596e-03, 5.10220925e-02, -2.60015901e-03,
       6.25994838e-02, -2.05886609e-02, -5.73164667e-03, -1.09625191e-01,
      -6.93240737e-03, -5.62026689e-02, -7.53184848e-02,  1.47087665e-02],
     [-2.29282566e-02, -2.66834493e-02, -1.10125885e-02,  1.29942415e-01,
      -1.22921871e-01, -4.30587418e-02, -1.17420501e-01, -1.40391874e-01,
      -7.10455833e-02, -3.41486658e-02, -9.56667643e-02,  2.34091140e-01,
       2.73579203e-02,  7.27266767e-02,  6.53307933e-02,  3.09669729e-02],
     [-2.18268560e-01, -1.67198025e-01,  1.87419691e-02,  1.34524170e-01,
      -3.21465833e-01, -1.66586732e-01,  3.93851787e-02, -1.13346936e-01,
      -1.85692853e-01, -4.32592477e-02, -7.65490031e-02,  5.73616991e-01,
       1.04219032e-01,  2.46544562e-01,  1.77605218e-01, -1.34494180e-01],
     [-7.42347101e-02, -1.52484831e-01,  3.28887740e-02,  1.26780473e-01,
      -2.80349993e-01, -1.77762952e-01,  6.86288174e-02, -5.12178416e-02,
      -1.80654642e-01, -1.17665022e-02, -8.07758218e-02,  3.79125350e-01,
       4.86827984e-02,  2.51118886e-01,  2.57532975e-02, -1.57412799e-02],
     [-1.07282379e-01, -7.64736127e-02,  4.84119522e-02,  1.28387746e-01,
      -2.18476883e-01, -1.82054567e-01,  1.52976146e-02, -7.10685236e-02,
      -1.73515463e-01, -4.12709916e-03, -1.06414518e-01,  3.63864949e-01,
       2.45242171e-02,  1.65306495e-01,  1.63356978e-01, -3.50336745e-02],
     [ 2.77288910e-01,  1.91426837e-01,  1.15975545e-01, -3.00809424e-01,
       3.53820685e-01,  2.06982196e-01,  1.35654125e-01,  3.81774055e-01,
       3.13562376e-01,  6.90548980e-02, -1.17978867e-02, -8.53234848e-01,
       8.60565871e-02, -3.64305268e-01, -6.18093105e-01,  2.53957529e-01],
     [ 3.83584452e-02, -5.46407471e-04, -7.34657773e-02, -3.32005156e-02,
      -2.06217199e-02,  4.67799692e-02, -5.72907797e-02, -9.59714252e-02,
      -9.64847045e-03,  6.68079564e-03,  1.87581945e-03,  6.22977235e-02,
      -5.18260933e-03,  4.02837705e-02,  1.44418033e-01, -5.52729384e-02],
     [ 2.41341634e-01,  1.73795889e-01, -3.75589515e-02, -1.42555331e-01,
       3.84872718e-01,  2.38727072e-01, -1.20257209e-02,  2.05726531e-01,
       2.15305804e-01,  5.00862191e-02,  5.81300455e-02, -7.41794721e-01,
       5.00783702e-02, -3.10037624e-01, -4.30832650e-01,  1.79950028e-01],
     [ 1.71381217e-01,  8.60607805e-02, -4.25650079e-02, -7.89561436e-02,
       3.27447146e-01,  2.06393272e-01, -9.99529325e-02,  8.75520458e-02,
       1.73129038e-01,  1.83979104e-02,  8.66853944e-02, -4.29207905e-01,
      -1.34850124e-01, -2.38397134e-01, -5.91414821e-02,  4.23220304e-02],
     [-2.88768790e-01, -1.80939916e-01,  1.47296971e-02,  1.67827001e-01,
      -4.32864620e-01, -2.72139265e-01, -5.57988568e-02, -1.58129080e-01,
      -1.79029373e-01, -5.74095133e-02, -1.07043503e-01,  7.43098244e-01,
       7.56653959e-02,  3.66662136e-01,  3.01325497e-01, -1.27959854e-01],
     [ 1.76761191e-01,  1.63276218e-01, -9.03262635e-02, -1.79551087e-01,
       3.63256815e-01,  3.29970109e-01, -5.18792211e-02,  2.56728748e-01,
       2.77043384e-01,  1.04113728e-01,  1.39981372e-01, -7.42130480e-01,
      -3.45240730e-02, -3.43286484e-01, -3.06301247e-01,  1.17604350e-01],
     [-1.45793545e-01, -1.03188495e-01,  5.87884102e-02,  5.16550386e-02,
      -2.64038008e-01, -2.03541648e-01,  9.04180182e-02, -6.41077594e-02,
      -2.19857427e-01, -1.60879229e-02, -1.04557303e-01,  4.88954503e-01,
       5.79221329e-02,  2.58682715e-01,  1.11924826e-01, -5.27088363e-02],
     [ 3.47740014e-01,  1.86040292e-01,  3.17058919e-02, -2.45707324e-01,
       4.27598566e-01,  2.70498332e-01,  1.11400473e-01,  3.27817668e-01,
       3.02461446e-01,  2.75129573e-02, -6.07115143e-02, -9.25728053e-01,
      -3.31178070e-02, -3.80932347e-01, -4.93071060e-01,  3.28947236e-01],
     [-1.73318365e-01, -7.71425700e-02, -7.63105604e-02,  8.92259943e-02,
      -2.01888064e-03, -1.31631788e-02, -6.43309362e-02, -2.37122798e-01,
      -1.72523534e-01, -6.47848335e-02,  2.77209132e-01,  3.34394268e-01,
      -1.20700446e-01,  9.22038595e-02,  4.85868651e-01, -2.62678175e-01],
     [ 5.12454916e-02,  4.77355858e-02,  1.98894592e-02, -5.53814654e-02,
       1.71358402e-01,  4.93148856e-02, -2.18343163e-02,  3.39019857e-02,
       1.21062562e-01,  9.50995930e-02,  5.29949571e-02, -2.46427468e-01,
      -2.97737686e-02, -1.53276055e-01, -8.49544018e-02,  5.20241376e-02],
     [-1.53612088e-01, -5.82122212e-02,  9.64674733e-02,  1.29389831e-01,
      -1.66369565e-01, -1.63654572e-01, -1.93956496e-02, -1.40682220e-01,
      -7.15304054e-02, -1.68367774e-02, -6.34093114e-02,  3.72333201e-01,
      -6.15109806e-02,  1.72726337e-01,  2.23722169e-01, -1.20402896e-01]] # inverse of key matrix used to decrypt the text

def to16BitbinaryString(char: str) -> str:
    '''convert a character to a 16 bit binary representation of its ASCII'''
    return '{0:016b}'.format(ord(char))

def binaryToDecimal(string: str) -> str:
    return chr(int(string, 2))

def converStringToNumberList(numbersString: str) -> list:
    '''convert string of numbers to array of int numbers'''
    numbersList = []
    for char in list(numbersString):
        numbersList.append(int(char))
    return numbersList

def convertNumberListToString(numbersList: list) -> str:
    '''convert list of numbers to a string'''
    numbersString = ''
    for num in numbersList:
        numbersString += str(round(num))
    return numbersString


def multiplyMatrixWithCharVector(matrix: list, charVector: list) -> list:
    result = []
    for i in range(len(matrix)):
        result.append(0)
        for j in range(len(matrix[i])):
            result[i] += matrix[i][j]*charVector[j]
    return result

def matrixEncryptionAlgorithm(text: str) -> list:
    '''encrypt text using Matrix Encryption Algorithm'''
    encryptedMatrix = []
    for char in text:
        charBinary = to16BitbinaryString(char)
        charBinaryList = converStringToNumberList(charBinary)
        encryptedVector = multiplyMatrixWithCharVector(keyMatrix, charBinaryList)
        encryptedMatrix.append(encryptedVector)
    return encryptedMatrix

def decryptMatrixEncryptionAlgorithm(encryptedMatrix: list) -> str:
    '''decrypt message encrypted by Matrix Encryption Algorithm'''
    message = ''
    for encryptedVector in encryptedMatrix:
        charBinaryList = multiplyMatrixWithCharVector(inverseMatrix, encryptedVector)
        charBinary = convertNumberListToString(charBinaryList)
        char = binaryToDecimal(charBinary)
        message += char

    return message

if __name__ == "__main__":
    '''ask user for a text to encrypt in case of main'''
    args = sys.argv[1:]
    encryptedArgs = []  # array of encrypted values of the provided args
    for arg in args:
        encryptedValue = matrixEncryptionAlgorithm(arg)
        encryptedArgs.append(encryptedValue)
    for i in range(len(encryptedArgs)):
        print(args[i], "->", encryptedArgs[i])
