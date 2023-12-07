from helpers.datagetter import aocd_data_in
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def classify(hand):
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
