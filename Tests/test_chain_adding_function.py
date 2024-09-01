import pytest

from Practice.chain_adding_function import Adder


class TestAdder:
    # Creating an Adder instance with an initial value
    def test_initial_value(self):
        adder = Adder(1)
        assert repr(adder) == "1"

    # Creating an Adder instance with a negative initial value
    def test_negative_initial_value(self):
        adder = Adder(-5)
        assert repr(adder) == "-5"

    # Calling an Adder instance with a negative number
    def test_call_with_negative_number(self):
        adder = Adder(5)
        result = adder(-3)
        assert repr(result) == "2"

    # Chaining calls to Adder instances to accumulate values
    def test_chaining_calls(self):
        adder_instance = Adder(1)(2)(3)(4)
        assert int(adder_instance) == 10

    # Using the __repr__ method to get the string representation of the current value
    def test_repr_method(self):
        adder_instance = Adder(5)
        assert repr(adder_instance) == "5"

    # Adding two Adder instances with integer values
    def test_add_two_adder_instances_with_integer_values(self):
        adder1 = Adder(3)
        adder2 = Adder(5)
        result = adder1 + adder2.value
        assert result == 8


if __name__ == "__main__":
    pytest.main(["-vv", __file__])
