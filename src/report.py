from typing import List, Dict, Tuple, Union, cast
from pathlib import Path
from .fileparse import parse_csv
from .stock import Stock
from .tableformat import (
    FORMAT2FORMATTER_CLS,
    TableFormatter,
)
from .portfolio import Portfolio


def read_portfolio(file_path: Union[str, Path]) -> Portfolio:
    """
    Reads a portfolio file and places each entry into a list.

    :param file_path: Path to the portfolio file
    :return: Returns list of Stock entries
    """
    portdict = parse_csv(
        file_path,
        select=["name", "shares", "price"],
        convert_fn={"name": str, "shares": int, "price": float},
    )
    portfolio = [
        Stock(pd["name"], pd["shares"], pd["price"])
        for pd in portdict
        if isinstance(pd, dict)
    ]
    return Portfolio(portfolio)


def read_prices(file_path: Union[str, Path]) -> Dict[str, float]:
    """
    Reads a prices file and places each entry into a dictionary.

    :param file_path: Path to the prices file
    :return: Returns a dictionary of prices and their stock names
    """
    prices = parse_csv(file_path, convert_fn=[str, float], has_headers=False)
    prices = cast(List[Tuple], prices)
    return {name: price for name, price in prices}


def calc_gain_loss(portfolio: Portfolio, prices: Dict) -> Portfolio:
    """
    Calculates the change in stock price from a given portfolio and the current price.

    :param portfolio: Portfolio list
    :param prices: Dictionary of prices
    :return: Returns a new portfolio list with the change in price
    """
    for port in portfolio:
        port.change = round(-(port.price - prices[port.name]), 2)
    return portfolio


def make_report(
    portfolio: Portfolio, prices: Dict[str, float]
) -> List[Tuple[str, int, float, float]]:
    """
    Calculates the gain/loss for the portfolio and formats it to be printed.

    :param portfolio: Portfolio list
    :param prices: Dictionary of prices
    :return: Returns the portfolio entries as a list of tuples
    """
    gain_loss = calc_gain_loss(portfolio, prices)
    report_data = []

    for gl in gain_loss:
        report_data.append((gl.name, gl.shares, prices[gl.name], gl.change))
    return report_data


def get_report(
    report_data: List[Tuple[str, int, float, float]],
    formatter: TableFormatter,
) -> List[str]:
    """
    Returns a report as a table.

    :param report_data: List of formatted portfolios
    :param formatter: Formatter object to format the report.
    :return: Returns the table as a list where each entry is a row of the table
    """
    return formatter.format(
        headers=("Name", "Shares", "Price", "Change"), rows=report_data
    )


def portfolio_report(
    portfolio_file_path: Union[str, Path],
    prices_file_path: Union[str, Path],
    fmt: str = "txt",
) -> List[str]:
    """
    Create a tabulated report from a portfolio file and price file.

    :param portfolio_file_path: Path to the portfolio file
    :param prices_file_path: Path to the prices file
    :param fmt: Format for the report to printed. Can be any formatter defined in src/tableformat.py
    :return: Returns the table as a list where each entry is a row of the table
    """
    try:
        formatter = FORMAT2FORMATTER_CLS[fmt]()
    except KeyError:
        raise RuntimeError(
            f"Unknown format {fmt} - available formats are {FORMAT2FORMATTER_CLS.keys()}"
        )

    portfolio = read_portfolio(portfolio_file_path)
    prices = read_prices(prices_file_path)
    report = make_report(portfolio, prices)
    printed_report = get_report(report, formatter=formatter)
    return printed_report
