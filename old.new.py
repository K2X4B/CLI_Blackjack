#-------------------------------- Modules -----------------------------------------#
import random
import time
#-------------------------------- Vars --------------------------------------------#
player_deck = [1, 10] #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
house_deck = [11, 10] #[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#-------------------------------- Classes -----------------------------------------#
class Player:
    def __init__(self, hand, score, blackjack):
        self.hand = hand
        self.score = score
        self.blackjack = blackjack
    def set_score():
        self.score = sum(self.hand)
#-------------------------------- Objects ------------------------------------------#
user = Player([], 0, False)
house = Player([], 0, False)
#-------------------------------- Functions -----------------------------------------#
def player_deal(): # deals two cards and appends them to the players hand
    C1 = (random.choice(player_deck))
    user.hand.append(C1)
    C2 = (random.choice(player_deck))
    user.hand.append(C2)

    if C1 == 1 and C2 == 10:
        user.hand = [11, 10]
        print("Blackjack")
    if C1 == 10 and C2 == 1:
        user.hand = [10, 11]
        print("Blackjack")

    print("Your starting hand", end=" ")
    print(user.hand)

#-------------------------------- Code ----------------------------------------------#

#-------------------------------- Go ------------------------------------------------#
player_deal()
