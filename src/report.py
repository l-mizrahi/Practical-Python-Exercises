import csv
from typing import List, Dict, Tuple


def read_portfolio(filename: str) -> List[Dict]:
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if not row:
                raise ValueError
            newrow = (row[0], int(row[1]), float(row[2]))
            portfolio.append(dict(zip(headers, newrow)))

    return portfolio


def read_prices(filename: str) -> Dict:
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            if not row:
                continue
            prices[row[0]] = float(row[1])
    return prices


def calc_gain_loss(portfolio: List[Dict], prices: Dict) -> List[Dict]:
    for port in portfolio:
        port["change"] = round(-(port["price"] - prices[port["name"]]), 2)
    return portfolio


def make_report(
    portfolio: List[Dict], prices: Dict
) -> List[Tuple[str, int, float, float]]:
    gain_loss = calc_gain_loss(portfolio, prices)
    report_data = []

    for gl in gain_loss:
        report_data.append((gl["name"], gl["shares"], prices[gl["name"]], gl["change"]))
    return report_data


def print_report(report_data: List[Tuple]) -> List[str]:
    output = []
    output.append(f"{'Name':>10s} {'Shares':>10s} {'Price':>10s} {'Change':>10s}")
    output.append(" ".join(["-" * 10] * 4))
    for r in report_data:
        output.append("{:>10s} {:>10d} {:>10.2f} {:>10.2f}".format(*r))
    return output
