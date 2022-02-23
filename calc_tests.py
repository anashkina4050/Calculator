import pytest
from app.calculator import calculator


class Testcalc:
    def setup(self):
        self.calc = calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 4, 1) == 3

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 4, 1) == 5
