def multiple_of_3_and_5(number):
    """Euler Project Q. 001
    Find the sum of all natural numbers divisible by 3 or 5
    below a given number.
    """
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])


def fibonacci_even_sum(number):
    """Euler Project Q. 002
    Find the sum of all even Fibonacci numbers below a given number.
    """
    fib = [1, 2]
    while fib[-1] < number:
        new_fib = fib[-1] + fib[-2]
        # print(new_fib)
        if new_fib <= number:
            fib.append(new_fib)
        else:
            break

    return sum([i for i in fib if i % 2 == 0])


# print(fibonacci_even_sum(4_000_000))

def largest_prime_factor(number: int):
    """Euler Project Q. 003
    Find the largest prime factor of a given number.
    """
    largest_factor: int = 0
    i: int = 2
    if number < 2:
        return "No Prime Factor"

    while number > 1:
        while number % i == 0:
            largest_factor = i
            number = number // i
        i += 1
    return largest_factor

# print(largest_prime_factor(600851475143))
