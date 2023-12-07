from helpers.datagetter import aocd_data_in
from collections import defaultdict
from itertools import product

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def classify_old(hand):
    hand_set = list(set(hand))
    if len(hand_set) == 1:
        return 6
    elif len(hand_set) == 2:
        if hand.count(hand[0]) in [2, 3]:
            return 4
        else:
            return 5
    elif len(hand_set) == 3:
        if 3 in [hand.count(hand_set[0]), hand.count(hand_set[1]), hand.count(hand_set[2])]:
            return 3
        else:
            return 2
    elif len(hand_set) == 4:
        return 1
    return 0

def classify(hand):
    num_jokers = hand.count("J")
    jokers_locations = [i for i in range(len(hand)) if hand[i] == "J"]
    best = 0
    if num_jokers == 0:
        return classify_old(hand)
    for new_hand in product(cards[1:], repeat=num_jokers):
        j_hand = ""
        j = 0
        for i in range(len(hand)):
            if i in jokers_locations:
                j_hand += new_hand[j]
                j += 1
            else:
                j_hand += hand[i]
        best = max(classify_old(j_hand), best)
    return best


games = defaultdict(list)
games_score = {}

for game in din:
    hand = game.split(" ")[0]
    bid = game.split(" ")[1]

    games[classify([*hand])].append(hand)
    games_score[hand] = bid

rank = 0
for i in range(7):
    games[i].sort(key=lambda x: [cards.index(c) for c in x])
    for item in games[i]:
        rank += 1
        ans += rank * int(games_score[item])


aocd_submit(ans)
