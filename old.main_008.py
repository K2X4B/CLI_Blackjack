#___________________________CLI_Blackjack_Main_004.py____________________2025-02-07______#
import random
import time
#-------------------------------- setting up vars -----------------------------------------#
player_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #[1, 10] #
house_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #[11, 10] #
new_card = 0

player_bust = False
player_blackjack = False


house_blackjack = False
dealt = 0
hit = ""
dealing = False
push = False

#-------------------------------- create up object classes --------------------------------------#
class Bank:
    def __init__(self, chips):
        self.chips = chips
    def set_bank(self, chips):
        self.chips = chips
    def get_bank(self,chip):
        return self.chips

class Player:
    def __init__(self, hand, score):
        self.hand = hand
        self.score = sum(self.hand)
    def set_hand(self):
        self.hand = hand
    def get_hand(self):
        return self.hand
    def get_score(self):
        return self.score
#-------------------------------- setting up objects -------------------------------------------#

player = Player([], 0)
house = Player([], 0)
bank = Bank(20)

#--**Here**------------------------- setting up functions --------------------------------------#
def player_deal(): # deals two cards and appends them to the players hand
    new_card = (random.choice(player_deck))
    player.hand.append(new_card)
    new_card = (random.choice(player_deck))
    player.hand.append(new_card)
    if player.hand[0] == 1 and player.hand[1] == 10:
        player.hand[0] = 11
    if player.hand[0] == 10 and player.hand[1] == 1:
        player.hand[1] = 11
    house.hand = sum(player.hand)
    if house.hand == 21:
        player_blackjack = True
        print("Blackjack!")

def house_deal(): # deals cards to the dealer's hand until their score is at least 17
    new_card = (random.choice(house_deck))
    house.hand.append(new_card)
    new_card = (random.choice(house_deck))
    house.hand.append(new_card)
    house.score = sum(house.hand)
    if house.score < 17:
        new_card = (random.choice(house_deck))
        house.hand.append(new_card)
    if house.score > 21:
        house_bust = True
    if house.score == 21:
        house_blackjack = True

def draw(): # adds a card to the player's hand
    dealt = (random.choice(player_deck))
    print("You were dealt", end=" ")
    print(dealt)
    player.hand.append(dealt)
    print("Your updated had is", end=" ")
    print(player.hand, end=" ")
    house.hand = sum(player.hand)
    print("Total", end=" ")
    print(house.hand)

def check_for_bust(): # does what it says on the tin
    house.hand = sum(player.hand)
    if house.hand > 21:
        player_bust = True
        print("Bust! Better luck next time.")
        dealing = False

def starting_deal(): # sets up a round
    player_deal()
    house_deal()
    house.hand = sum(player.hand)
    print(player.hand)
    print(house.hand)
    print("The dealer is showing", end=" ")
    print(house.hand[0])

def playing(): # the main loop of a round
    dealing = True
    while house.hand < 21 and dealing == True:
        hit = input("Would you like to Hit or Stay (h/s)?")
        if hit == "h":
            draw()
            check_for_bust()
        elif hit == "s":
            print("Okay, let's see how you did.")
            dealing = False
        else:
            print("Error, please answer h or s.")
#-------------------------------- main code -----------------------------------------#
starting_deal()
playing()
print("House: ", end=" ")
print(house.hand, end=" ")
print(house.score)
if player_bust == True and house_bust == True: # show who won and update the bank
    print("Push")
    push = True
elif house.hand == house.score:
    print("Push")
    push = True
elif player_bust == False and house.hand > house.score:
    print("You win!")
    bank = bank + 3
else:
    print("The house wins.")
    bank = bank - 2
house.score = sum(house.hand)
print(house.hand, end=" ")
print(house.score)
print("Bank: ", end=" ")
print(bank)
#-------------------------------- main code -----------------------------------------#

#starting_deal()
#playing()
#results() # I think I need some classes/objects so that I can set states and call them regardless of funtion
