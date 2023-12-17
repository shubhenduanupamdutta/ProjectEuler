def largest_grid_product(grid: list[list[int]], n: int):
    """
    Project Euler Q. 011
    Find the largest product of n adjacent numbers in a grid."""
    largest_product: int = 1
    # checking in rows
    for row in grid:
        for i in range(len(row) - n + 1):
            product = 1
            for j in range(n):
                product *= row[i + j]
            if product > largest_product:
                largest_product = product

    # checking in columns
    for i in range(len(grid) - n + 1):
        for j in range(len(grid[i])):
            product = 1
            for k in range(n):
                product *= grid[i + k][j]
            if product > largest_product:
                largest_product = product

    # checking in left to right diagonals
    for i in range(len(grid) - n + 1):
        for j in range(len(grid[i]) - n + 1):
            product = 1
            for k in range(n):
                product *= grid[i + k][j + k]
            if product > largest_product:
                largest_product = product

    # checking in right to left diagonals
    for i in range(len(grid) - n + 1):
        for j in range(n - 1, len(grid[i])):
            product = 1
            for k in range(n):
                product *= grid[i + k][j - k]
                print(i + k, j - k, grid[i + k][j - k], product)
            if product > largest_product:
                largest_product = product

    return largest_product


def divisible_triangle_number(n):
    """
    Project Euler Q. 012
    Find the first triangle number with more than n divisors."""

    def num_of_divisors(number):
        divisors_list = []
        for i in range(1, int(number ** 0.5) + 1):
            if number % i == 0:
                divisors_list.append(i)
                # Corresponding divisor is number // i
                # Check for avoid duplicate
                if i != (number // i):
                    divisors_list.append(number // i)
        divisors_list.append(number)
        return len(divisors_list)

    triangle_number = 1
    i = 2
    while True:
        if num_of_divisors(triangle_number) > n:
            return triangle_number

        triangle_number += i
        i += 1


def large_sum(numbers: list[str]):
    """
    Project Euler Q. 013
    Find the first ten digits of the sum of the given numbers (in string format)."""

    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += int(number)
    return int(str(sum_of_numbers)[:10])


def largest_collatz_sequence(n: int):
    """
    Project Euler Q. 014
    Find the number under n that produces the longest Collatz chain."""

    def collatz_sequence(number: int):
        sequence = [number]
        while number != 1:
            if number % 2 == 0:
                number = number // 2
            else:
                number = 3 * number + 1
            sequence.append(number)
        print(sequence)
        return sequence

    longest_sequence = []
    for i in range(1, n + 1):
        sequence = collatz_sequence(i)
        if len(sequence) > len(longest_sequence):
            longest_sequence = sequence
    return longest_sequence[0]
