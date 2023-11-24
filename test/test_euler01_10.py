import pytest
from Euler01_10 import project_euler01_10 as pe01


class TestEuler01:
    def setup_method(self, method):
        print(f"Setting up method {method.__name__}...")
        self.euler01 = pe01.multiple_of_3_and_5

    def test_euler01_number(self):
        """Check if result is a integer"""
        assert type(self.euler01(10)) == int

    @pytest.mark.parametrize("number, expected", [
        (49, 543), (1000, 233168), (8456, 16687353), (19564, 89301183)
    ])
    def test_euler01_values(self, number, expected):
        assert self.euler01(number) == expected


class TestEuler02:
    def setup_method(self, method):
        print(f"Setting up method {method.__name__}...")
        self.euler02 = pe01.fibonacci_even_sum
        # print("Setting up done.")

    def test_euler02_integer(self):
        """Check if result is a integer"""
        assert type(self.euler02(10)) == int

    def test_euler02_even(self):
        """Check if result is even"""
        assert self.euler02(10) % 2 == 0

    @pytest.mark.parametrize("number, expected", [
        (8, 10), (10, 10), (34, 44), (60, 44),  (1000, 798), (10000, 3382),
        (100000, 60696), (4000000, 4613732)
    ])
    def test_euler02_values(self, number, expected):
        assert self.euler02(number) == expected


class TestEuler03:
    def setup_method(self, method):
        print(f"Setting up method {method.__name__}...")
        self.euler03 = pe01.largest_prime_factor

    @pytest.mark.parametrize("number, expected", [
        (2, 2), (3, 3), (5, 5), (7, 7), (8, 2), (13195, 29),
        (600851475143, 6857)
    ])
    def test_euler03(self, number, expected):
        largest_factor = self.euler03(number)
        assert isinstance(largest_factor, int)
        assert largest_factor == expected


class TestEuler04:
    def setup_method(self, method):
        print(f"Setting up method {method.__name__}...")
        self.euler04 = pe01.largest_palindrome_product

    @pytest.mark.parametrize("number, expected", [
        (2, 9009), (3, 906609), (4, 99000099)
    ])
    def test_euler04(self, number, expected):
        if number > 3:
            pytest.skip("This test takes too long.")
        largest_palindrome = self.euler04(number)
        assert isinstance(largest_palindrome, int)
        assert largest_palindrome == expected


class TestEuler05:
    def setup_method(self, method):
        print(f"Setting up method {method.__name__}...")
        self.euler05 = pe01.smallest_multiple

    @pytest.mark.parametrize("number, expected", [
        (5, 60), (7, 420), (10, 2520), (13, 360360), (20, 232792560)
    ])
    def test_euler05(self, number, expected):
        smallest_multiple = self.euler05(number)
        assert isinstance(smallest_multiple, int)
        assert smallest_multiple == expected


class TestEuler06:
    def setup_method(self, method):
        print(f"Setting up method {method.__name__}...")
        self.euler06 = pe01.sum_square_and_square_sum_diff

    @pytest.mark.parametrize("number, expected", [
        (10, 2640), (20, 41230), (100, 25164150)
    ])
    def test_euler06(self, number, expected):
        difference = self.euler06(number)
        assert isinstance(difference, int)
        assert difference == expected


class TestEuler07:
    def setup_method(self, method):
        print(f"Setting up method {method.__name__}...")
        self.euler07 = pe01.nth_prime_number

    @pytest.mark.parametrize("number, expected", [
        (6, 13), (10, 29), (100, 541), (1000, 7919), (10001, 104743)
    ])
    def test_euler07(self, number, expected):
        nth_prime = self.euler07(number)
        assert isinstance(nth_prime, int)
        assert nth_prime == expected
