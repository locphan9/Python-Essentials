# Python code​​​​​​‌‌‌‌‌‌​‌‌‌​‌​​‌‌​​‌​‌​‌‌​ below

def encodeString(stringVal):
    # Your code goes here.
    n, i = len(stringVal), 0
    prevChar, prevIndex = None, 0
    result = []
    while i < n:
        if stringVal[i] != prevChar and prevChar is not None:
            result.append((prevChar, i - prevIndex))
            prevIndex = i
        prevChar = stringVal[i]
        i += 1
    result.append((prevChar, n - prevIndex))
    return result
    
def decodeString(encodedList):
    # Your code goes here.
    return "".join([i * f for i,f in encodedList])
