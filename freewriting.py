"""
freewriting.py
"""
import collections

Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    """
    docstring
    """
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        """
        __init__
        """
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        """
        __len__
        """
        return len(self._cards)

    def __getitem__(self, position):
        """
        __getitem__
        """
        return self._cards[position]

if __name__ == "__main__":
    print(FrenchDeck().ranks)
