from src.follow import Follow
from src import DATA_DIRECTORY


def test_follow_iter():
    """
    Tests if Follow generates correct data.
    """
    follow = Follow(DATA_DIRECTORY / "portfolio.csv")
    expected = [
        "name,shares,price\n",
        '"AA",100,32.20\n',
        '"IBM",50,91.10\n',
        '"CAT",150,83.44\n',
        '"MSFT",200,51.23\n',
        '"GE",95,40.37\n',
        '"MSFT",50,65.10\n',
        '"IBM",100,70.44\n',
    ]
    assert list(follow) == expected  # all([f == e for f, e in zip(follow, expected)])
