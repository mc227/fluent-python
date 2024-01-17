"""
frenchdeck from scratch
"""
import collections

Card = collections.namedtuple('Card',['rank','suit'])

class Frenchdeck:
    """
    docstring
    """
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades hearts clubs diamonds'.split()

    def __init__(self):
        """
        __init__
        """
        
if __name__ == "__main__":
    print(Frenchdeck().suits)
