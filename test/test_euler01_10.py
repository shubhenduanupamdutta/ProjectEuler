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
        if number > 10000:
            pytest.skip("This test takes too long.")
        nth_prime = self.euler07(number)
        assert isinstance(nth_prime, int)
        assert nth_prime == expected


class TestEuler08:
    def setup_method(self, method):
        print(f"Setting up method {method.__name__}...")
        self.euler08 = pe01.largest_product_in_series
        self.series = "73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518438586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966489504452445231617318564030987111217223831136222989342338030813533627661428280644448664523874930358907296290491560440772390713810515859307960866701724271218839987979087922749219016997208880937766572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397536978179778461740649551492908625693219784686224828216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"  # noqa: E501

    @pytest.mark.parametrize("number, expected", [
        (4, 5832), (13, 23514624000)
    ])
    def test_euler08(self, number, expected):
        largest_product = self.euler08(self.series, number)
        assert isinstance(largest_product, int)
        assert largest_product == expected


class TestEuler09:
    def setup_method(self, method):
        print(f"Setting up method {method.__name__}...")
        self.euler09 = pe01.special_pythagorean_triplet

    @pytest.mark.parametrize("number, expected", [
        (12, 60), (24, 480), (1000, 31875000)
    ])
    def test_euler09(self, number, expected):
        product = self.euler09(number)
        assert isinstance(product, int)
        assert product == expected
