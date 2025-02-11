#-------------------------------- Modules -----------------------------------------#
import random
import time
#-------------------------------- Vars --------------------------------------------#
player_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #[1, 10]
house_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #[11, 10]
#-------------------------------- Classes -----------------------------------------#
class Player:
    def __init__(self, hand, score, blackjack, bust):
        self.hand = hand
        self.score = score
        self.blackjack = blackjack
        self.bust = bust
    def set_score():
        self.score = sum(self.hand)
    def check_bust():
        if self.score > 21:
            self.bust = True
#-------------------------------- Objects ------------------------------------------#
user = Player([], 0, False, False)
house = Player([], 0, False, False)
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

    if user.hand == [11, 10]:
        user.blackjack = True
    if user.hand == [10, 11]:
        user.blackjack = True

    print("Your starting hand", end=" ")
    print(user.hand)

def house_deal(): # adds cards to dealer's hand until their score is at least 17

    while house.score < 17:
        C = (random.choice(house_deck))
        house.hand.append(C)
        house.score = sum(house.hand)

        if house.score > 21:
            house.bust = True

    else:
        print("The House is showing ", end=" ")
        print(house.hand[0])

def draw_one():
    hit = input("Would you like another card (y/n)?")
    if hit == "y":
        C = (random.choice(player_deck))
        user.hand.append(C)
        print("You were dealt ", end=" ")
        print(player.hand)
        print(player.score)


#-------------------------------- Code ----------------------------------------------#

#-------------------------------- Test ----------------------------------------------#
player_deal()
print(user.blackjack)
house_deal()
print(house.hand, end=" ")
print(house.score)
print(house.bust)
draw_one()