deck_base = ["A"] + list(map(str, range(2, 11))) + ["J", "Q", "K"]

cardDict = {k+1: v for k, v in enumerate(deck_base)}

card_list = list(range(1, 14)) * 4

def pass_Deck():
    return cardDict

class Support_vars:
    permutations_new = ['NEW', 'NEw', 'New', 'NeW', 'nEW', 'nEw', 'neW', 'new']