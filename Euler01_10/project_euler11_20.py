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


grid2 = [
    [40, 17, 81, 18, 57],
    [74, 4, 36, 16, 29],
    [36, 42, 69, 73, 45],
    [51, 54, 69, 16, 92],
    [7, 97, 57, 32, 16]
]
print(largest_grid_product(grid2, 4))
