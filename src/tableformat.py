from typing import List, Tuple, Union


class TableFormatter:
    """
    Base class for formatting the portfolio report.
    This class should be extended to create tables in different formats.
    """

    def headings(self, headers: List[Tuple[str, str, str, str]]) -> List[str]:
        """
        Format the table headings.

        :param headers: The headers of the table
        :raises NotImplementedError: If headings() has not been overloaded
        :return: The formatted headers
        """
        raise NotImplementedError()

    def row(self, rowdata: List[Tuple[str, int, float, float]]) -> List[str]:
        """
        Format a single row of table data.

        :param rowdata: A single row of the table to be formatted
        :raises NotImplementedError: If row() has not been overloaded
        :return: The formatted row
        """
        raise NotImplementedError()

    def format(
        self,
        data: Union[
            List[Tuple[str, str, str, str]], List[Tuple[str, int, float, float]]
        ],
    ) -> List[str]:
        """
        Formats data as a table.
        """
        pass


class TextTableFormatter(TableFormatter):
    """
    Formats table in plain-text format.
    """

    def headings(self, headers: List[Tuple[str, str, str, str]]) -> List[str]:
        pass

    def row(self, rowdata: List[Tuple[str, int, float, float]]) -> List[str]:
        pass


class CSVTableFormatter(TableFormatter):
    """
    Formats table in CSV format.
    """

    def headings(self, headers: List[Tuple[str, str, str, str]]) -> List[str]:
        pass

    def row(self, rowdata: List[Tuple[str, int, float, float]]) -> List[str]:
        pass
