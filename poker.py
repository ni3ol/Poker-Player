import random
from collections import Counter

POKER_RANKS = {
    1: 'ROYAL FLUSH',
    2: 'STRAIGHT FLUSH',
    3: '4 OF A KIND',
    4: 'FULL HOUSE',
    5: 'FLUSH',
    6: 'STRAIGHT',
    7: '3 OF A KIND',
    8: '2 PAIR',
    9: '1 PAIR',
    10: 'HIGH CARD'
}

HIGH_CARDS = {
    11: 'JACK',
    12: 'QUEEN',
    13: 'KING',
    14: 'ACE'
}

class Poker(object):
    def __init__(self):
        self.deck = []
        for i in ['HEART', 'CLUBS', 'SPADES', 'DIAMONDS']:
            for j in range(2, 15):
                self.deck.append((i,j))
        self.discard_pile = []

    def shuffle(self):
        for i in self.discard_pile:
            self.deck.append(self.deck.pop(i))

    def get_hand(self):
        hand = []
        for i in range(5):
            index = random.randint(0, len(self.deck) - 1)
            hand.append(self.deck[index])
            self.discard_pile.append(self.deck.pop(index))
        return hand

    def classify_hand(self, hand):
        # sorts in place
        hand.sort(key=lambda tup: tup[1])
        # count suits
        suit_count = Counter(card[0] for card in hand)
        #count values
        value_count = Counter(card[1] for card in hand)
        suit = hand[0][0]
        num = hand[0][1]
        if (suit, 10) in hand and (suit, 11) in hand and (suit, 12) in hand and (suit, 13) in hand and (suit, 14) in hand:
            return 1, hand
        elif (suit, num) in hand and (suit, num+1) in hand and (suit, num+2) in hand and (suit, num+3) in hand and (suit, num+4) in hand:
            return 2, hand
        elif 4 in value_count.values():
            return 3, hand
        elif 3 in value_count.values() and 2 in value_count.values():
            return 4, hand
        elif 5 in suit_count.values():
            return 5, hand
        elif num+1 == hand[1][1] and num+2 == hand[2][1] and num+3 == hand[3][1] and num+4 == hand[4][1]:
            return 6, hand
        elif 3 in value_count.values() and 1 in value_count.values():
            return 7, hand
        elif value_count.values().count(2) == 2:
            return 8, hand
        elif value_count.values().count(2) == 1:
            return 9, hand
        else:
            return 10, hand

    def break_tie(self, hand_one, hand_two):
        max_one = max(hand_one,key=lambda item:item[1])[1]
        max_two = max(hand_two,key=lambda item:item[1])[1]
        count_hand_one = Counter(card[1] for card in hand_one)
        count_hand_two =  Counter(card[1] for card in hand_two)

        if hand_one[0] == 1:
            return 'Players tie. Split the pot'

        if hand_one[0] == 2:
            pass

        if hand_one[0] == 3:
            for x, y in count_hand_one.items():
                if y == 4:
                    max_1 = x
            for x, y in count_hand_two.items():
                if y == 4:
                    max_2 = x

        if hand_one[0] == 4:
            for x, y in count_hand_one.items():
                if y == 3:
                    max_1 = x
            for x, y in count_hand_two.items():
                if y == 3:
                    max_2 = x

        if hand_one[0] == 5:
            pass

        if hand_one[0] == 6:
            pass

        if hand_one[0] == 7:
            for x, y in count_hand_one.items():
                if y == 3:
                    max_1 = x
            for x, y in count_hand_two.items():
                if y == 3:
                    max_2 = x

        if hand_one[0] == 8:
            for x, y in count_hand_one.items():
                max_1 = 0
                max_2 = 0
                if y == 2:
                    if x > max_1:
                        max_1 = x
            for x, y in count_hand_two.items():
                if y == 2:
                    if x > max_2:
                        max_2 = x

        if hand_one[0] == 9:
            for x, y in count_hand_one.items():
                if y == 2:
                    max_1 = x
            for x, y in count_hand_two.items():
                if y == 2:
                    max_2 = x

        if hand_one[0] == 10:
            pass

        if max_one > max_two:
            return 'Player one wins'
        elif max_two > max_one:
            return 'Player two wins'
        else:
            return 'Players tie. Split the pot'


    def rank_hands(self, hand_one, hand_two):
        if hand_one[0] == hand_two[0]:
            self.break_tie(hand_one, hand_two)
        if hand_one[0] < hand_two[0]:
            return 'Player one wins'.format(POKER_RANKS[hand_one[0]])
        elif hand_two[0] < hand_one[0]:
            return 'Player two wins with {}'.format(POKER_RANKS[hand_two[0]])

    def compare_hands(self, player_one, player_two):
        one = self.classify_hand(player_one)
        two = self.classify_hand(player_two)
        rank = self.rank_hands(one, two)
        print('rank',rank)
