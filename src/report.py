from typing import List, Dict, Tuple, Union, TypedDict, Any, cast
from pathlib import Path
from .fileparse import parse_csv
from .stock import Stock


class PortDict(TypedDict, total=False):
    name: str
    shares: int
    price: float
    change: float


def to_portdict(data: Dict[str, Any]) -> PortDict:
    pdict = PortDict(name=data["name"], shares=data["shares"], price=data["price"])
    return pdict


def read_portfolio(file_path: Union[str, Path]) -> List[PortDict]:
    """
    Reads a portfolio file and places each entry into a list.

    :param file_path: Path to the portfolio file
    :return: Returns list of Stock entries
    """
    portfolio = parse_csv(
        file_path,
        select=["name", "shares", "price"],
        convert_fn={"name": str, "shares": int, "price": float},
    )
    portfolio = cast(List[Dict[str, Any]], portfolio)
    portdicts = [to_portdict(p) for p in portfolio]
    return portdicts


def read_prices(file_path: Union[str, Path]) -> Dict[str, float]:
    """
    Reads a prices file and places each entry into a dictionary.

    :param file_path: Path to the prices file
    :return: Returns a dictionary of prices and their stock names
    """
    prices = parse_csv(file_path, convert_fn=[str, float], has_headers=False)
    prices = cast(List[Tuple], prices)
    return {name: price for name, price in prices}


def calc_gain_loss(portfolio: List[Stock], prices: Dict) -> List[Stock]:
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
    portfolio: List[Stock], prices: Dict[str, float]
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
