# jemo_tech@2025

def iterative_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
        
    return factorial

number = int(input("Enter number to find factorial: "))
result = iterative_factorial(number)
print(result)