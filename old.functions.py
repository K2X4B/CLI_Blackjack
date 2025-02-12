import random

deck_p = [1, 10]#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card = 0
player_hand = []

bank = 20 # starting amount of chips


def player_deal(): # deals the player two cards and adds them to their hand
    player_bj = False
    card = (random.choice(deck_p))
    player_hand.append(card)
    card = (random.choice(deck_p))
    player_hand.append(card)

    A = 11 # solves for the ace
    if player_hand[0] == 1 and player_hand[1] == 10:
        player_hand[0] = A

    if player_hand[0] == 10 and player_hand[1] == 1: 
        player_hand[1] = A   
    
    player_score = sum(player_hand)
    
    if player_score == 21:
        player_bj = True
        print("Blackjack!")
    
    print(player_hand, end=" ")
    print(player_score)

deck_h = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # dealer can not draw a one
house_hand = []

def house_deal(): # keeps dealing cards to the house's hand until their score is at least 17
    house_score = 0
    house_bust = False
    house_bj = False

    while house_score < 17:
        card = (random.choice(deck_h))
        house_hand.append(card)
        house_score = sum(house_hand)
    else:    
        print(house_hand)
    
    if house_score > 21:
        house_bust = True
        print("The dealer is Bust!")
    
    if house_score == 21 and len(house_hand) < 3:
        house_bj = True
        print("The deal has Blackjack!")


def hit_stay():
    hit = input("Would you like another card (y/n)?        ")
    if hit == "y" or hit == "h":
        card = (random.choice(deck_p))
        player_hand.append(card)
        player_score = sum(player_hand)
        print(player_hand, end=" ")
        print(player_score)
    else:
        print("Okay, let's see how you did...")

def results(): # who won?
    bank = bank
    if player_hand == house_hand:
        print("Push")
    if player_hand < house_hand:
        print("Better luck next time.")
        bank = bank - 2
    else:
        print("Congratulations, you won!")
        bank = bank + 3


bank = 20 # starting amount of chips

player_deal()

house_deal()

hit_stay()

#results()

