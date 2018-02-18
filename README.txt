Blackjack; Created by Michael @ Intuitive Designs.

Play a great game of Blackjack on your command line! The program creates a real-time deck
that is shuffled natturally (the randomization process in the shuffle function mimics
the effect of real-life card shuffling; I don't simply use a random generator).
Also, the deck is iterated through card-by-card in the same real-life manner
you would be dealt a deck of cards. The lesser alternative would mean randomly generating
cards each time a player needed a new hand or a singular card for a "hit". This would allow
five '2' cards being dealt in one game.
Please e-mail me @ michaeldb3@gmail.com if you don't understand how this game provides a
realistic Blackjack experience and look at the following examples
========================

instead of:

x = Deck_of_cards_dictionary[random.randrange(1,13)]
y = Deck_of_cards_dictionary[random.randrange(1,13)]
print("Player 1's Hand:\n", x, y)
==================================
This program uses:

deck = [**imagine A, 2-10, J, Q, K in a dict with their matching 
numerical values of 1-13 for brevity**]
x = next(iter(deck)
y = next(iter(deck)

See how this program iterates through a deck just how you would "iterate" through a deck in
real life? This is the goal of this project.
To create a fun but, REALISTIC gambling experience to all.
I hope you all enjoy and don't worry.

A GUI VERSION IS COMING SOON AND WILL UTILIZE PyQT likely and not TKinter like in other 
projects i've created.
