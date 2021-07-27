from src.pcost import portfolio_cost
import pytest
from src.report import read_portfolio


def test_read_portfolio():
    portfolio = read_portfolio("data/portfolio.csv")
    expected = [
        ("AA", 100, 32.2),
        ("IBM", 50, 91.1),
        ("CAT", 150, 83.44),
        ("MSFT", 200, 51.23),
        ("GE", 95, 40.37),
        ("MSFT", 50, 65.1),
        ("IBM", 100, 70.44),
    ]

    assert len(portfolio) == len(expected)
    assert all([p == e for p, e in zip(portfolio, expected)])


def test_read_portfolio_missing_values():
    with pytest.raises(ValueError):
        portfolio_cost("data/missing.csv")
