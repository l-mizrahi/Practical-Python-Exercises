import csv
from typing import List, Dict, Tuple, Union, TypedDict
from pathlib import Path


class PortDict(TypedDict, total=False):
    name: str
    shares: int
    price: float
    change: float


def read_portfolio(file_path: Union[str, Path]) -> List[PortDict]:
    """
    Reads a portfolio file and places each entry into a list.

    :param file_path: Path to the portfolio file
    :raises ValueError: Raises error if line in the file is empty
                        Like in missing.csv. This was part of the exercise
    :return: Returns list of portfolio entries
    """
    portfolio: List[PortDict] = []
    with open(file_path) as f:
        rows = csv.reader(f)
        next(rows)
        for name, shares, price in rows:
            if not all([name, shares, price]):
                raise ValueError("Cannot process blank lines.")
            pdict = PortDict(name=name, shares=int(shares), price=float(price))
            portfolio.append(pdict)

    return portfolio


def read_prices(file_path: Union[str, Path]) -> Dict[str, float]:
    """
    Reads a prices file and places each entry into a dictionary.

    :param file_path: Path to the prices file
    :return: Returns a dictionary of prices and their stock names
    """
    prices = {}
    with open(file_path) as f:
        rows = csv.reader(f)
        for name, price in rows:
            if not all([name, price]):
                continue
            prices[name] = float(price)
    return prices


def calc_gain_loss(portfolio: List[PortDict], prices: Dict) -> List[PortDict]:
    """
    Calculates the change in stock price from a given portfolio and the current price.

    :param portfolio: Portfolio list
    :param prices: Dictionary of prices
    :return: Returns a new portfolio dictionary with the change in price
    """
    for port in portfolio:
        port["change"] = round(-(port["price"] - prices[port["name"]]), 2)
    return portfolio


def make_report(
    portfolio: List[PortDict], prices: Dict[str, float]
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
        report_data.append((gl["name"], gl["shares"], prices[gl["name"]], gl["change"]))
    return report_data


def get_report(report_data: List[Tuple[str, int, float, float]]) -> List[str]:
    """
    Returns a report as a table.

    :param report_data: List of formatted portfolios
    :return: Returns the table as a list where each entry is a row of the table
    """
    output = []
    output.append(f"{'Name':>10s} {'Shares':>10s} {'Price':>10s} {'Change':>10s}")
    output.append(" ".join(["-" * 10] * 4))
    for r in report_data:
        output.append("{:>10s} {:>10d} {:>10.2f} {:>10.2f}".format(*r))
    return output


def portfolio_report(
    portfolio_file_path: Union[str, Path], prices_file_path: Union[str, Path]
) -> List[str]:
    """
    Create a tabulated report from a portfolio file and price file.

    :param portfolio_file_path: Path to the portfolio file
    :param prices_file_path: Path to the prices file
    :return: Returns the table as a list where each entry is a row of the table
    """
    portfolio = read_portfolio(portfolio_file_path)
    prices = read_prices(prices_file_path)
    report = make_report(portfolio, prices)
    printed_report = get_report(report)
    return printed_report
