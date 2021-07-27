import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            if not row:
                raise ValueError
            portfolio.append((row[0], int(row[1]), float(row[2])))

    return portfolio
