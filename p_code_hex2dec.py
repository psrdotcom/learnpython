# Python code​​​​​​‌​‌‌‌​‌​‌​​​‌‌‌‌​‌‌​​​​​​ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    result = 0
    count = 1
    length = len(hexNum)
    for v in hexNum:
        #print ('val: ', hexNumbers.get(v))
        if hexNumbers.get(v) is not None:
            #print('valu:', length - count)
            result = result + hexNumbers[v] * (16 ** (length - count))
            count = count + 1
        else:
            result = None
            break
    print (result)

hexToDec('A2')
hexToDec('1BC3A2')
hexToDec('spam spam spam')
