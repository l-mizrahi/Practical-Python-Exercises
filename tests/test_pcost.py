import pytest
from src.pcost import portfolio_cost


def test_portfolio_cost():
    assert portfolio_cost("data/portfolio.csv") == 44671.15


def test_portfolio_cost_missing_values():
    with pytest.raises(ValueError):
        portfolio_cost("data/missing.csv")


def test_portfolio_cost_different_headers():
    assert portfolio_cost("data/portfoliodate.csv") == 44671.15


def test_portfolio_cost_incorrect_format():
    with pytest.raises(ValueError):
        portfolio_cost("data/portfolio3.csv")
