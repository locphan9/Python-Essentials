hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    n = len(hexNum)
    if n > 3:
        return
    integer_decimal = 0
    i = n - 1
    while i >= 0:
        if hexNum[i] not in hexNumbers:
            return
        integer_decimal += hexNumbers[hexNum[i]] * (2 ** (4 * (n - 1 - i)))
        i = i - 1
    return integer_decimal