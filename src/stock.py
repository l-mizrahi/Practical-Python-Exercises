class Stock:
    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name: str = name
        self.shares: int = shares
        self.price: float = price
        self.change: float

    @property
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
        Tests equivalence of two Python objects.

        :param other: Python object to compare to
        :return: Returns True if self and other have the same attributes otherwise False
        """
        if not isinstance(other, Stock):
            return NotImplemented

        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        return f"Stock(name='{self.name}', shares={self.shares}, price={self.price})"
