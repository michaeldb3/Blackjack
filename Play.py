from shuffle import *
from deck import *

ChoicePerms = Support_vars.permutations_new

def post_game(route_to=None):
    input_val = input("Input \'H\' to get a new card,\ninput \'NEW\' to be dealt a new hand,\ninput nothing to exit.\n\t")
    choice = input_val if route_to == None else "null string"
    if choice == 'H' or choice == 'h':
        deal(1)
    elif choice in ChoicePerms:
        deal(2)
    else:
        def final_chance():
            last_chance = input("Are you sure you want to exit? \'Y\' to exit and \'N\' to continue playing.")
            if last_chance == "Y" or last_chance == "y":
                pass
            elif last_chance == "N" or last_chance == "n":
                post_game()
            else:
                post_game(True)
        final_chance()

def deal(numCards):
    if numCards == 1:
        try:
            z1 = next(list_iter)
            z2 = deck[z1]
            print(z2,'\n')
            post_game()
        except StopIteration:
            print("You've reached the end of the deck, please start a new game to reshuffle and deal a new hand.")
            reshuffle_Q = input("Would you like to play again? \'Y\' to reshuffle, \'N\' to stop.")
            if reshuffle_Q == 'Y':
                __init__()
            elif reshuffle_Q == 'N':
                pass
    elif numCards == 2:
        x1 = next(list_iter)
        y1 = next(list_iter)
        x2 = deck[x1]
        y2 = deck[y1]
        print(x2, '\t', y2)
        post_game()

def __init__():
    shuffled_list = shuffle_gen()
    global list_iter
    list_iter = iter(shuffle_gen())
    global deck
    deck = pass_Deck()
    print(shuffled_list)
    deal(2)

__init__()