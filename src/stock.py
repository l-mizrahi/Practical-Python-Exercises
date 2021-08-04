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
        """
        Calculates the cost of the stock.

        :return: Returns the cost of the stock
        """
        return self.shares * self.price

    def sell(self, nshares: int) -> None:
        """
        Subtracts shares.

        :param nshares: Number of shares to sell
        """
        self.shares -= nshares

    def __eq__(self, other: object) -> bool:
        """
        Tests equivalence of two Stock objects.

        :param other: Stock object to compare to
        :return: Returns True if self and other have the same attributes otherwise False
        """
        if not isinstance(other, Stock):
            return NotImplemented

        return all(
            [
                self.name == other.name,
                self.shares == other.shares,
                self.price == other.price,
            ]
        )

    def __repr__(self) -> str:
        return f"Stock('{self.name}', {self.shares}, {self.price})"
