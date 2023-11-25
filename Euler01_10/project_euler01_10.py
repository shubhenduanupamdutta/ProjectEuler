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


def largest_palindrome_product(number: int):
    """Euler Project Q. 004
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    largest_palindrome: int = 0
    start_number: int = 10 ** (number - 1)
    end_number: int = 10 ** number
    # print(largest_palindrome, start_number, end_number)
    for i in range(start_number, end_number):
        # print(i)
        for j in range(start_number, end_number):
            product: int = i * j
            if str(product) == str(product)[::-1]:
                if product > largest_palindrome:
                    largest_palindrome = product
    if largest_palindrome == 0:
        return "No Palindrome"

    return largest_palindrome


def smallest_multiple(number: int):
    """Euler Project Q. 005
    Find the smallest positive number that is evenly divisible
    by all of the numbers from 1 to a given number.
    """
    smallest_multiple: int = 1
    for i in range(1, number + 1):
        if smallest_multiple % i != 0:
            for j in range(1, i + 1):
                if (smallest_multiple * j) % i == 0:
                    smallest_multiple *= j
                    break
    return smallest_multiple


def sum_square_and_square_sum_diff(n):
    """Euler Project Q. 006
    Find the difference between the sum of the squares of the first n
    natural numbers and the square of the sum.
    """
    sum_of_squares = sum([i ** 2 for i in range(1, n + 1)])
    square_of_sum = sum([i for i in range(1, n + 1)]) ** 2
    return abs(square_of_sum - sum_of_squares)


def nth_prime_number(n: int):
    """Euler Project Q. 007
    Find the nth prime number.
    """
    prime_list: list[int] = [2]
    i: int = 3
    while len(prime_list) < n:
        if all(i % j != 0 for j in prime_list):
            prime_list.append(i)
        i += 2
    return prime_list[-1]


def largest_product_in_series(series: str, n: int):
    """Euler Project Q. 008
    Find the largest product of n consecutive digits in a given series.
    """
    print(series, n)
    largest_product: int = 1
    for i in range(len(series) - n):
        product: int = 1
        for j in range(n):
            print(series[i + j], product)
            product *= int(series[i + j])
        if product > largest_product:
            largest_product = product
    return largest_product
