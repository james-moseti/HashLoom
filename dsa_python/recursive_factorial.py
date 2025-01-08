# jemo_tech@2025

def recursive_factorial(num):
    if num <= 0:
        return 1
    else:
        return num * recursive_factorial(num - 1)
    
if __name__ == "__main__":
    number = int(input("Enter a positive integer: "))
    result = recursive_factorial(number)
    print(f"Factorial of {number}: {result}")