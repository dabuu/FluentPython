# coding:utf-8
"""
@file: 1.1.py
@time: 8/7/2018 11:50 PM
@contact: dabuwang
"""

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades hearts diamonds clubs".split()

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

    def choice_random_card(self):
        return choice(self.cards)

    def get_same_ranks(self, rank_name):
        if rank_name in self.ranks:
            return self[self.ranks.index(rank_name)::13]


if __name__ == '__main__':
    fd = FrenchDeck()
    print len(fd)

    # =========== choice random
    for x in range(5):
        print fd.choice_random_card()

    # =========== choice random
    print fd.get_same_ranks("A")
    print fd.get_same_ranks("2")
    print fd.get_same_ranks("a")
