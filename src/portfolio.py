from typing import Iterator, List
from .stock import Stock
from collections import Counter


class Portfolio:
    """
    Class to provide functionality to a list of stocks.
    :param _holdings: The list of stocks
    """

    _holdings: List[Stock]

    def __init__(self, holdings: List[Stock]):
        self._holdings = holdings

    def __iter__(self) -> Iterator[Stock]:
        return self._holdings.__iter__()

    @property
    def total_cost(self) -> float:
        """
        Returns the total cost of all shares.
        """
        return sum([stock.shares * stock.price for stock in self._holdings])

    def tabulate_shares(self) -> Counter:
        """
        Returns the total count of each different share.
        """
        shares_counter: Counter = Counter()
        for stock in self._holdings:
            shares_counter[stock.name] += stock.shares
        return shares_counter

    def __eq__(self, other: object) -> bool:
        """
        Tests equivalence of two Portfolio objects.

        :param other: Portfolio object to compare to
        :return: Returns True if self and other have the same attributes otherwise False
        """
        if not isinstance(other, Portfolio):
            return NotImplemented

        return self._holdings == other._holdings
