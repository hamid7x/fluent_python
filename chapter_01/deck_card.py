import collections
from random import choice


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenshDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


card = Card('7', 'diamonds')
print(card)

deck = FrenshDeck()
print(len(deck))
print(deck[0])
print(deck[-1])
print(choice(deck))
print(deck[:3])
print(deck[12::13])

for card in reversed(deck):
    print(card)

print(Card('Q', 'hearts') in deck)
print(Card('7', 'beats') in deck)
