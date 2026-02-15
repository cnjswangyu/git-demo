def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

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

def modulo(a, b):
    return a % b

def absolute(n):
    return abs(n)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return absolute(a)

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return absolute(a * b) // gcd(a, b)

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 3 = {multiply(4, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"2^5 = {power(2, 5)}")
    print(f"5! = {factorial(5)}")
    print(f"sqrt(16) = {square_root(16)}")
    print(f"10 % 3 = {modulo(10, 3)}")
    print(f"|-7| = {absolute(-7)}")
    print(f"gcd(12, 18) = {gcd(12, 18)}")
    print(f"lcm(12, 18) = {lcm(12, 18)}")
