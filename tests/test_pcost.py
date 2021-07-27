import pytest
from src.pcost import portfolio_cost


def test_portfolio_cost():
    assert portfolio_cost("src/Data/portfolio.csv") == 44671.15


def test_portfolio_cost_missing_values():
    with pytest.raises(ValueError):
        portfolio_cost("src/Data/missing.csv")
