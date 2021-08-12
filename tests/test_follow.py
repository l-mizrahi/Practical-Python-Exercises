from src.stock import Stock
from src.follow import Follow
from src import DATA_DIRECTORY
from src.portfolio import Portfolio


def test_follow_iter():
    """
    Tests if Follow generates correct data.
    """
    follow = Follow(DATA_DIRECTORY / "portfolio.csv")
    expected = [
        "name,shares,price\n",
        '"AA",100,32.20\n',
        '"IBM",50,91.10\n',
        '"CAT",150,83.44\n',
        '"MSFT",200,51.23\n',
        '"GE",95,40.37\n',
        '"MSFT",50,65.10\n',
        '"IBM",100,70.44\n',
    ]
    assert list(follow) == expected


def test_follow_portfolio():
    """
    Tests if follow_portfolio only outputs stock prices for stock in given portfolio
    """
    portfolio = Portfolio(
        [
            Stock(name="IBM", shares=50, price=91.1),
            Stock(name="MSFT", shares=200, price=51.23),
        ],
    )
    follow = Follow(DATA_DIRECTORY / "stocklog_test.csv")
    expected = [
        "IBM 102.77 -0.30",
        "MSFT 29.95 -0.10",
        "IBM 102.79 -0.28",
        "MSFT 29.97 -0.08",
        "MSFT 29.99 -0.06",
    ]

    assert follow.follow_portfolio(portfolio) == expected
