from typing import Counter, List
from .stock import Stock


class Portfolio:
    """
    Class to provide functionality to a list of stocks.
    :param _holdings: The list of stocks
    """

    _holdings: List[Stock]

    def __init__(self, holdings: List[Stock]):
        pass

    def __iter__(self):
        pass

    @property
    def total_cost(self) -> float:
        """
        Returns the total cost of all shares.
        """
        pass

    def tabulate_shares(self) -> Counter:
        """
        Returns the total count of each different share.
        """
        pass
