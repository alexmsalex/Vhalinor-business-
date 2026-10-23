import pytest
from src.finance import compound_growth, monthly_contributions

def test_compound_growth_zero_rate():
    assert compound_growth(1000, 0, 5) == 1000

def test_compound_growth_positive_rate():
    assert compound_growth(1000, 0.10, 2) == pytest.approx(1210)

def test_monthly_contributions_increase_future_value():
    assert monthly_contributions(1000, 100, 0.05, 5) > compound_growth(1000, 0.05, 5)

def test_invalid_principal():
    with pytest.raises(ValueError):
        compound_growth(-1, 0.05, 3)
