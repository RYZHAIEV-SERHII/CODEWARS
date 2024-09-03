import pytest

from how_many_eggs import calculate_eggs


class TestCalculateEggs:
    # Return "No chickens yet!" when the year is 0
    def test_no_chickens_yet(self):
        assert calculate_eggs(0, 5) == "No chickens yet!"

    # Correctly decrease egg production by 20% each year
    def test_decrease_egg_production(self):
        assert calculate_eggs(2, 1) == 900

    # Calculate eggs for a given year and span with initial chickens
    def test_calculate_eggs_initial_chickens(self):
        assert calculate_eggs(4, 8) == 2655

    # Calculate eggs for a long term and custom span
    def test_long_term_egg_production(self):
        assert calculate_eggs(74, 10), 3984

    # Handle the case when year is 1
    def test_handle_year_one(self):
        assert calculate_eggs(1, 15), 900


if __name__ == "__main__":
    pytest.main(["-v", __file__])
