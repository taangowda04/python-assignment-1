# math_utils.py

def factorial(n):
    # Validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("factorial() only accepts non-negative integers")

    # Factorial of 0 is 1
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    # Validate input
    if not isinstance(n, int) or n < 2:
        raise ValueError("is_prime() requires an integer greater than 1")

    # Check divisibility
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    # Validate input
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("gcd() only accepts integers")

    a, b = abs(a), abs(b)

    # Euclid's Algorithm
    while b != 0:
        a, b = b, a % b
    return a
