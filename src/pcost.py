def portfolio_cost(filename):
    total_cost = 0
    with open(filename) as f:
        next(f)
        for line in f:
            if not line:
                raise ValueError
            row = line.split(",")
            total_cost += int(row[1]) * float(row[2])

    return total_cost
