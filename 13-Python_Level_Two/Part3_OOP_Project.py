#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle, sample
from itertools import product

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def shuffleCards(self):
        shuffle(self.allcards)

    def halve(self):
        return (self.allcards[:26], self.allcards[26:])

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def addCard(self, addition):
        self.cards.append(addition)

    def removeCard(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def playCard(self):
        play = self.hand.removeCard()
        print(f"{self.name} has played: "+play[0]+play[1])
        return play

    def playWarCards(self):
        war_cards = []
        if len(self.hand.cards) < 4:
            print(f"{self.name} doesn't have enough cards!")
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop(0))
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0




######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

d = Deck()
d.shuffleCards()
d1, d2 = d.halve()
my_hand, comp_hand = Hand(d1), Hand(d2)
me, comp = Player("Daniel",my_hand), Player("Computer",comp_hand)

turn_counter = 0
war_counter = 0

while me.still_has_cards() and comp.still_has_cards():

    # add to turn counter
    turn_counter += 1

    # indicate how many cards each player has
    print(f"At turn start, I have {len(me.hand.cards)} cards, comp has {len(comp.hand.cards)} cards")

    # initialize pot of cards that will go to winner of round
    table_cards = []

    # each player picks one
    x, y = me.playCard(), comp.playCard()
    for l in [x,y]:
        table_cards.append(l)

    # player > computer
    if RANKS.index(x[1]) > RANKS.index(y[1]):
        print(f"{me.name} wins this hand!")
        for l in table_cards:
            me.hand.addCard(l)

    # player < computer
    elif RANKS.index(x[1]) < RANKS.index(y[1]):
        print(f"{comp.name} wins this hand!")
        for l in table_cards:
            comp.hand.addCard(l)

    # ranks are equal --> war
    else:
        print("It's war!")

        # add to war counter
        war_counter += 1

        # get war cards and add to table cards
        for l in me.playWarCards() + comp.playWarCards():
            table_cards.append(l)

        # flip next card
        c, d = me.playCard(), comp.playCard()
        for l in [c, d]:
            table_cards.append(l)

        # player card is higher rank than computer
        if RANKS.index(c[1]) > RANKS.index(d[1]):
            print(f"{me.name} wins this war!")
            for card in table_cards:
                me.hand.addCard(card)

        # computer card is higher rank than player
        elif RANKS.index(c[1]) < RANKS.index(d[1]):
            print(f"{comp.name} wins this war!")
            for card in table_cards:
                comp.hand.addCard(card)

        # ranks are equal --> burn one, play one
        else:
            print("Another flip!")

            # burn one
            e, f = me.playCard(), comp.playCard()
            for x in [e, f]:
                table_cards.append(x)

            # compare one
            g, h = me.playCard(), comp.playCard()
            for x in [g, h]:
                table_cards.append(x)

            # player > computer
            if RANKS.index(g[1]) > RANKS.index(h[1]):
                print(f"{me.name} wins this war!")
                for card in table_cards:
                    me.hand.addCard(card)

            # player < computer
            elif RANKS.index(g[1]) < RANKS.index(h[1]):
                print(f"{comp.name} wins this war!")
                for card in table_cards:
                    comp.hand.addCard(card)

            # another match, how to keep this going??
            else:
                print("I give up!")

    print(f"After this round, I have {len(me.hand.cards)} cards, comp has {len(comp.hand.cards)} cards")
    round_end = input("Press enter to continue!\n\n")

else:

    if not me.still_has_cards():
        print(f"{comp.name} wins!")
    else:
        print(f"{me.name} wins!")
    print(f"The game lasted {str(turn_counter)} turns, and there were {str(war_counter)} wars.")

# Use the 3 classes along with some logic to play a game of war!
