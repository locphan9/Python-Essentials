def allPrimesUpTo(num):
    # Your code goes here.
    if num < 2:
        return []
    primesFound = [2]
    for number in range(2, num):
        sqrtNum = number ** 0.5
        for factor in primesFound:
            if number % factor == 0:
                break
            if factor > sqrtNum:
                primesFound.append(number)
                break
    return primesFound