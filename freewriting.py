"""
freewriting.py
"""
import collections

if __name__ == "__main__":
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    print(Card)
