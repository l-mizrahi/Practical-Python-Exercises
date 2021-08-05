from pathlib import Path
from typing import TextIO, Union


class Follow:
    """
    Class for continuously reading from a list of stock prices as a generator.
    """

    file_path_or_buffer: Union[str, Path, TextIO]

    def __init__(self, file_path_or_buffer: Union[str, Path, TextIO]) -> None:
        if isinstance(file_path_or_buffer, (str, Path)):
            file_path_or_buffer = open(file_path_or_buffer)
        self.file_path_or_buffer = file_path_or_buffer

    def __iter__(self):
        """
        Return iterator of file.
        """
        return iter(self.file_path_or_buffer)

    def __next__(self):
        """
        Return next line of file.
        """
        line = next(self.file_path_or_buffer)
        return line
