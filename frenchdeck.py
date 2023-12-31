import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    """
    Represents a French deck of playing cards.

    Example:
    >>> deck = FrenchDeck()
    >>> len(deck)
    52

    >>> deck[0]
    Card(rank='2', suit='spades')

    >>> deck[-1]
    Card(rank='A', suit='hearts')

    >>> deck[:3]
    [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
    """

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')
