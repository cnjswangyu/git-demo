def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a + b  # BUG: 这里写错了！

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def square_root(n):
    if n < 0:
        raise ValueError("Square root not defined for negative numbers")
    return n ** 0.5

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 3 = {multiply(4, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"2^5 = {power(2, 5)}")
    print(f"5! = {factorial(5)}")
    print(f"sqrt(16) = {square_root(16)}")
