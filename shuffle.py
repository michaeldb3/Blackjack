from deck import *
from random import *
import quantumrandom

flatList = lambda l: [item for sublist in l for item in sublist]

def shuffle(deck):
    num = len(deck) // 2
    x = deck[: num]
    y = deck[num:]
    q = sample(x, len(x))
    r = sample(y, len(y))
    s = flatList(list(zip(q, r)))
    return s


shuffled_deck = shuffle(shuffle(shuffle(card_list)))
def shuffle_gen():
    for q, r in enumerate(shuffled_deck):
        try:
            if shuffled_deck[q] == shuffled_deck[q + 1] and quantumrandom.randint() <= 0.701:
                tmpnum = random.randrange(0, 52)
                index = tmpnum if tmpnum != q else random.randrange(0, q)
                shuffled_deck.insert(index, shuffled_deck[q])
                del shuffled_deck[q]
            else:
                pass
        except Exception:
            pass
    return shuffled_deck
