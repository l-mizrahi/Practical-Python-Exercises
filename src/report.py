import csv
from typing import List, Dict, Tuple


def read_portfolio(file_path: str) -> List[Dict]:
    """
    Reads a portfolio file and places each entry into a list.

    :param file_path: Path to the portfolio file
    :raises ValueError: Raises error if line in the file is empty
                        Like in missing.csv. This was part of the exercise
    :return: Returns list of portfolio entries
    """
    portfolio = []
    with open(file_path) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if not row:
                raise ValueError
            newrow = (row[0], int(row[1]), float(row[2]))
            portfolio.append(dict(zip(headers, newrow)))

    return portfolio


def read_prices(file_path: str) -> Dict:
    """
    Reads a prices file and places each entry into a dictionary.

    :param file_path: Path to the prices file
    :return: Returns a dictionary of prices and their stock names
    """
    prices = {}
    with open(file_path) as f:
        rows = csv.reader(f)
        for row in rows:
            if not row:
                continue
            prices[row[0]] = float(row[1])
    return prices


def calc_gain_loss(portfolio: List[Dict], prices: Dict) -> List[Dict]:
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
    portfolio: List[Dict], prices: Dict
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


def print_report(report_data: List[Tuple]) -> List[str]:
    """
    Prints a report as a table.

    :param report_data: List of formatted portfolios
    :return: Returns the table as a list where each entry is a row of the table
    """
    output = []
    output.append(f"{'Name':>10s} {'Shares':>10s} {'Price':>10s} {'Change':>10s}")
    output.append(" ".join(["-" * 10] * 4))
    for r in report_data:
        output.append("{:>10s} {:>10d} {:>10.2f} {:>10.2f}".format(*r))
    return output
