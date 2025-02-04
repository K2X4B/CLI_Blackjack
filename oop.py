import random
deck_p = [1, 10]#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck_h = [11, 10]#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card = 0
player_deal = []
house_deal = []
bank = 20 # starting amount of chips

class Deal:
    def __init__(self, ):
        self.self = self
    def deal_one(): # deals the player a card and adds it to their Deal
        card = (random.choice(deck_p))
        player_deal.append(card)
        return player_deal
    def deal_two(): # deals the player two cards and adds them to their Deal
        card = (random.choice(deck_p))
        player_deal.append(card)
        card = (random.choice(deck_p))
        player_deal.append(card)
        return player_deal
    
    def deal_house():
        card = (random.choice(deck_h))
        house_deal.append(card)
        card = (random.choice(deck_h))
        house_deal.append(card)
        return house_deal

    
class Hand:
    def __init__(self, score, cards):
        self.cards = cards
        self.score = score
        #self.bj = bj
        #self.bust = bust
    def set_cards(self):
        self.cards = cards 

cards = Deal.deal_two()
# ------------------------------

#print(player_deal)
print("Your starting hand is ", end=" ")
print(cards)

hit = input("Would you like another card (y/n)?         ")
if hit == "y":
    new_card = Deal.deal_one()
    print("You were dealt a ", end=" ")
    print(new_card)  
if hit == "n":
    print(cards)

score = sum(cards)
print("Your score is ", end=" ")
print(score)
    
player_hand = cards
print(player_hand)

Deal.deal_house()
print(house_deal)

print("The House is showing a ", end=" ")
print(house_deal[0])



