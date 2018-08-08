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
fd = FrenchDeck()

def test_len():
    print len(fd)

def test_getitem():
    print "# =========== slice"
    print fd[10]
    print fd[-2]

    print fd[:3]
    print fd[-1:]
    print fd[12::13]

    print "# =========== choice random"
    for x in range(5):
        print choice(fd)

    print "# =========== iter & sort"
    # for card in fd:
    #     print card
    # for card in reversed(fd):
    #     print card

    for card in sorted(fd, key=spades_high):
        print card

suits_value = dict(spades=3, hearts=2, diamonds=1,clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suits_value) + suits_value[card.suit]


if __name__ == '__main__':
    test_len()
    test_getitem()


