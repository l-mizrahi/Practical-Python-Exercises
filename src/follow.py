from pathlib import Path
from typing import Iterable, List, TextIO, Union
from .portfolio import Portfolio


class Follow:
    """
    Class for reading a stock price file, such as stocklog_test.csv
    """

    file_path_or_buffer: Union[TextIO]

    def __init__(self, file_path_or_buffer: Union[str, Path, TextIO]) -> None:
        if isinstance(file_path_or_buffer, (str, Path)):
            file_path_or_buffer = open(file_path_or_buffer)
        self.file_path_or_buffer = file_path_or_buffer

    def __iter__(self) -> Iterable:
        """
        Return iterator of file.
        """
        return iter(self.file_path_or_buffer)

    def __next__(self) -> str:
        """
        Return next line of file.
        """
        line = next(self.file_path_or_buffer)
        return line

    def follow_portfolio(self, portfolio: Portfolio) -> List[str]:
        """
        Returns a list of stock price changes only for stocks in a given portfolio.

        :param portfolio: A Portfolio object
        :return: A list of all stock price changes for a given portfolio
        """
        output: List[str] = []
        for line in self.file_path_or_buffer:
            fields = line.split(",")
            name = fields[0].strip('"')
            price = float(fields[1])
            change = float(fields[4])
            if name in portfolio:
                output.append(f"{name} {price:.2f} {change:.2f}")
        return output
