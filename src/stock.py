class Stock:
    name: str
    shares: int
    price: float
    change: float

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price
        self.change: float

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, nshares: int) -> None:
        self.shares -= nshares

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Stock):
            return NotImplemented

        return all(
            [
                self.name == other.name,
                self.shares == other.shares,
                self.price == other.price,
            ]
        )
