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
class Bank:
    def __init__(self, chips):
        self.chips = chips
#class Loop:
    #def __init__(self,start, playing, menu)
        #self.start = start
        #self.playing = playing
        #self.menu = menu
#-------------------------------- Objects ------------------------------------------#
user = Player([], 0, False, False)
house = Player([], 0, False, False)
bank = Bank(20)
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
    user.score = sum(user.hand)
    print("Your starting hand", end=" ")
    print(user.hand, end=" ")
    print(user.score)
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
def result_text():
        print("You: ", end=" ")
        print(user.hand, end=" ")
        print(user.score)
        print("The House:", end=" ")
        print(house.hand, end=" ")
def draw_one(): # ask the player if they want to hit and apply the card to their hand if they do
    hit = input("Would you like another card (y/n)?")
    if hit == "y":
        C = (random.choice(player_deck))
        user.hand.append(C)
        print("You were dealt ", end=" ")
        user.score = sum(user.hand)
        print(user.hand)
        print(user.score)
        if user.score >21:
            print("Bust! Better luck next time.")
            user.bust = True
def end_results():
    user.score = sum(user.hand)
    house.score = sum(house.hand)
    if user.score == house.score: # tie aka Push
        print("Results: Push")
        result_text()
        house.score = sum(house.hand)
        print(house.score)
        print(bank.chips)
    elif user.score > house.score and user.bust == False:
        bank.chips = bank.chips + 3
        print("Results: Congratulations, you won!")
        result_text()
        print(house.score)
        print(bank.chips)
    elif house.score > user.score:
        bank.chips = bank.chips - 2
        print("Results: The House won. Better luck next time.")
        result_text()
        print(house.score)
        print(bank.chips)
    else:
        print(error)

#-------------------------------- Code ----------------------------------------------#

#-------------------------------- Test ----------------------------------------------#
player_deal()
print(user.blackjack)
house_deal()
print(house.hand, end=" ")
print(house.score)
print(house.bust)
draw_one()
print(user.bust)
end_results()