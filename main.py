import random

colors = ["Hearts", "Tiles", "Clovers", "Pikes"]
card_values = [str(x) for x in range(2, 11)] + ["A", "J", "Q", "K"]
deck = []
for color in colors:
    for c_v in card_values:
        deck.append((color, c_v))

number_of_player = int(input("How many player in game ? "))
player_names = [input(f'Name of {number + 1} player: ') for number in range(number_of_player)]
# player_names = []
# for number in range(number_of_player):
#     player_names.append(input(f'Name of {number + 1} player: '))
print(player_names)




def hand_draw():
    players_hands = {}
    players_hands["Table"] = [deck.pop(random.randint(0, len(deck) - 1)) for _ in range(5)]
    for name in player_names:
        players_hands[name] = [deck.pop(random.randint(0, len(deck) - 1)) for _ in range(2)]
    return players_hands

print(hand_draw())
