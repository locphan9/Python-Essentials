def factorial(num):
    # Your code goes here.
    if isinstance(num, str):
        return
    if num == 0:
        return 1
    if num < 0 or num % 1 != 0:
        return
    factorial = 1
    for i in range(2,num+1):
        factorial *= i
    return factorial