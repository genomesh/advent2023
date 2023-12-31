import numpy as np

file = open("test.txt", "r")

hands = []

class hand_object:
    def __init__(self, hand, bid, type, value):
        self.hand = hand
        self.bid = bid
        self.type = type
        self.value = value

def get_card_value(card):
    if card == 'J':
        return 0
    if card == 'A':
        return 12
    if card == 'K':
        return 11
    if card == 'Q':
        return 10
    if card == 'T':
        return 9
    return int(card) - 1

def get_hand_value(hand):
    value = 0
    for i, card in enumerate(hand):
        value += 13 ** (4-i) * get_card_value(card)
    return value

possible_card_types = ['five', 'four', 'full house', 'three', 'two pair', 'one pair', 'high card']

def get_type_no_joker(hand):
    card_counts = []
    for card in hand:
        card_counts.append(hand.count(card))
    if max(card_counts) == 5:
        return 'five'
    if max(card_counts) == 4:
        return 'four'
    if max(card_counts) == 3 and min(card_counts) == 2:
        return 'full house'
    if max(card_counts) == 3:
        return 'three'
    if card_counts.count(2) == 4:
        return 'two pair'
    if max(card_counts) == 2:
        return 'one pair'
    return 'high card'

def get_type(hand):
    num_jokers = hand.count('J')
    if num_jokers == 0:
        return get_type_no_joker(hand)
    if num_jokers == 5:
        return 'five'
    # assumption: always best to add Joker to most populous card type.
    # find most common character
    other_cards = list(filter(lambda x: x != 'J', hand))
    # either 1, 2, 3, 4 other cards
    card_counts = []
    for card in other_cards:
        card_counts.append(hand.count(card))
    most_common_card = other_cards[np.argmax(card_counts)]
    return get_type_no_joker(hand.replace('J', most_common_card))

for line in file.readlines():
    hand, bid = line.split(' ')
    hands.append(hand_object(hand, int(bid.strip()), get_type(hand), get_hand_value(hand)))

answer = 0
current_rank = 1

for t in reversed(possible_card_types):
    hands_of_type = list(filter(lambda x: x.type == t, hands))
    hand_values = []
    for hand in hands_of_type:
        hand_values.append(hand.value)
    for index in np.argsort(hand_values):
        answer += current_rank * hands_of_type[index].bid
        current_rank += 1

print(answer)

file.close()