import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if not row:
                raise ValueError
            row = (row[0], int(row[1]), float(row[2]))
            portfolio.append(dict(zip(headers, row)))

    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            if not row:
                continue
            prices[row[0]] = float(row[1])
    return prices


def calc_gain_loss(portfolio, prices):
    for port in portfolio:
        port["change"] = round(-(port["price"] - prices[port["name"]]), 2)
    return portfolio


def make_report(portfolio, prices):
    gain_loss = calc_gain_loss(portfolio, prices)
    report_data = []

    for gl in gain_loss:
        report_data.append((gl["name"], gl["shares"], prices[gl["name"]], gl["change"]))
    return report_data
