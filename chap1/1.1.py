# coding:utf-8
"""
@file: 1.1.py
@time: 8/7/2018 11:50 PM
@contact: dabuwang
"""

import collections

Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)]+list("JQKA")
    suits = "spades hearts diamonds clubs".split()

    def __init__(self):
        self.cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

if __name__ == '__main__':
    fd = FrenchDeck()
    print fd.__len__()