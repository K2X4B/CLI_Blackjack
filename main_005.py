#___________________________CLI_Blackjack_Main_004.py____________________2025-02-07______#
import random
import time
#-------------------------------- setting up vars -----------------------------------------#
player_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #[1, 10] #
house_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #[11, 10] #
new_card = 0
player_hand = []
player_score = 0
player_bust = False
player_blackjack = False
house_hand = []
house_score = 0
house_bust = False
house_blackjack = False
dealt = 0
hit = ""
dealing = False
push = False
bank = 20
#-------------------------------- setting up functions -----------------------------------------#
def player_deal(): # deals two cards and appends them to the players hand
    new_card = (random.choice(player_deck))
    player_hand.append(new_card)
    new_card = (random.choice(player_deck))
    player_hand.append(new_card)
    if player_hand[0] == 1 and player_hand[1] == 10:
        player_hand[0] = 11
    if player_hand[0] == 10 and player_hand[1] == 1:
        player_hand[1] = 11
    player_score = sum(player_hand)
    if player_score == 21:
        player_blackjack = True
        print("Blackjack!")

def house_deal(): # deals cards to the dealer's hand until their score is at least 17
    new_card = (random.choice(house_deck))
    house_hand.append(new_card)
    new_card = (random.choice(house_deck))
    house_hand.append(new_card)
    house_score = sum(house_hand)
    if house_score < 17:
        new_card = (random.choice(house_deck))
        house_hand.append(new_card)
    if house_score > 21:
        house_bust = True
    if house_score == 21:
        house_blackjack = True

def draw(): # adds a card to the player's hand
    dealt = (random.choice(player_deck))
    print("You were dealt", end=" ")
    print(dealt)
    player_hand.append(dealt)
    print("Your updated had is", end=" ")
    print(player_hand, end=" ")
    player_score = sum(player_hand)
    print("Total", end=" ")
    print(player_score)

def check_for_bust(): # does what it says on the tin
    player_score = sum(player_hand)
    if player_score > 21:
        player_bust = True
        print("Bust! Better luck next time.")
        dealing = False

def starting_deal(): # sets up a round
    player_deal()
    house_deal()
    player_score = sum(player_hand)
    print(player_hand)
    print(player_score)
    print("The dealer is showing", end=" ")
    print(house_hand[0])

def playing(): # the main loop of a round
    dealing = True
    while player_score < 21 and dealing == True:
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
print(house_hand, end=" ")
print(house_score)
if player_bust == True and house_bust == True: # show who won and update the bank
    print("Push")
    push = True
elif player_score == house_score:
    print("Push")
    push = True
elif player_bust == False and player_score > house_score:
    print("You win!")
    bank = bank + 3
else:
    print("The house wins.")
    bank = bank - 2
house_score = sum(house_hand)
print(house_hand, end=" ")
print(house_score)
print("Bank: ", end=" ")
print(bank)
#-------------------------------- main code -----------------------------------------#

#starting_deal()
#playing()
#results() # I think I need some classes/objects so that I can set states and call them regardless of funtion