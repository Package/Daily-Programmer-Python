# https://www.reddit.com/r/dailyprogrammer/comments/75p1cs/20171011_challenge_335_intermediate_scoring_a/
from itertools import combinations


class Hand(object):

    def __init__(self, str_cards, score=0):
        self.cards = [Card.parse_card(s) for s in str_cards.split(',')]
        self.score = score

    def __str__(self):
        return '{} {}'.format(self.cards, self.score)

    def calc_score(self):
        return self.fifteens_score() + self.run_score() + self.pairs_score() + self.flush_score() + self.nobs_score()

    def fifteens_score(self):
        fifteens = 0
        card_values = [min(c.value, 10) for c in self.cards]
        for x in range(1, len(self.cards) + 1):
            fifteens += 2 * len([c for c in combinations(card_values, x) if sum(c) == 15])
        return fifteens

    def run_score(self):
        sc = sorted(self.cards, key=lambda c: c.value)
        current_connection = 1
        best_connection = 1
        last_value = None

        for c in sc:
            if last_value is None:
                last_value = c.value
                continue

            if last_value + 1 != c.value:
                best_connection = current_connection
                current_connection = 1
            else:
                current_connection += 1

            last_value = c.value

        # If we've seen more than our previous best connection then update!
        if current_connection > best_connection:
            best_connection = current_connection

        return best_connection if best_connection >= 3 else 0

    def pairs_score(self):
        value_map = {}
        for c in self.cards:
            if c.value not in value_map:
                value_map[c.value] = 0
            value_map[c.value] += 1

        # 12 pts for four of a kind
        if 4 in value_map.values():
            return 12

        # 6 pts for three of a kind
        elif 3 in value_map.values():
            return 6

        # 2 pts for two of a kind
        elif 2 in value_map.values():
            return 2

        else:
            return 0

    def flush_score(self):
        suit_map = {}
        for c in self.cards:
            if c.suit not in suit_map:
                suit_map[c.suit] = 0
            suit_map[c.suit] += 1

        four_flush = len([c for c in self.cards[:-1] if c.suit == self.cards[0].suit]) == 4
        five_flush = 5 in suit_map.values()
        return 5 if five_flush else 4 if four_flush else 0

    def nobs_score(self):
        nob_suit = self.cards[-1].suit
        jacks = [c for c in self.cards[:-1] if c.value == Value.Jack and c.suit == nob_suit]
        return 1 if len(jacks) > 0 else 0


class Suit(object):
    Spade, Diamond, Heart, Club = range(1, 5)

    @staticmethod
    def parse_suit(s):
        suit_map = {'S': Suit.Spade, 'D': Suit.Diamond, 'H': Suit.Heart, 'C': Suit.Club}
        return suit_map[s]


class Value(object):
    Ace, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King = range(1, 14)

    @staticmethod
    def parse_value(s):
        card_map = {'A': Value.Ace, '2': Value.Three, '3': Value.Three, '4': Value.Four, '5': Value.Five,
                    '6': Value.Six, '7': Value.Seven, '8': Value.Eight, '9': Value.Nine, '10': Value.Ten,
                    'J': Value.Jack, 'Q': Value.Queen, 'K': Value.King}
        return card_map[s]


class Card(object):

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return 'Value: {} Suit: {}'.format(self.value, self.suit)

    @staticmethod
    def parse_card(s):
        value = Value.parse_value(s[:-1])
        suit = Suit.parse_suit(s[-1])

        return Card(value, suit)


h1 = Hand('5D,QS,JC,KH,AC', 0)
h2 = Hand('8C,AD,10C,6H,7S', 0)
h3 = Hand('AC,6D,5C,10C,8C', 0)
print(h1.calc_score())  # 10
print(h2.calc_score())  # 7
print(h3.calc_score())  # 4
