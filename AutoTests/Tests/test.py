import pytest

from AutoTests.app.calc import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1 ,1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_multyply_success(self):
        assert self.calc.multiply(self, 5, 5) == 25

    def test_multyply_unseccess(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 2, 2) == 0

    def test_subtraction_unsuccess(self):
        assert self.calc.subtraction(self, 2, 2) == 1

    def test_division_success(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_division_unsuccess(self):
        assert self.calc.division(self, 2, 2) == 0

    def teardown(self):
        print('Выполнение метода Teardown')
