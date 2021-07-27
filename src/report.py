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
    pass
