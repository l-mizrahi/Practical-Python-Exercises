from pathlib import Path
from typing import TextIO, Union


class Follow:
    """
    Class for continuously reading from a list of stock prices as a generator.
    """

    file_path_or_buffer: Union[str, Path, TextIO]

    def __init__(self, file_path_or_buffer: Union[str, Path, TextIO]) -> None:
        pass

    def __iter__(self):
        """
        Return iterator of file.
        """
        pass

    def __next__(self):
        """
        Return next line of file.
        """
        pass
