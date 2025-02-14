#------------------------CLI_Blackjack_V12.2_alpha.py------------------------------#
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
#-------------------------------- Objects -----------------------------------------------#
user = Player([], 0, False, False)
house = Player([], 0, False, False)
bank = Bank(20)
#--------------------------------- Section 1 Functions ----------------------------------#
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
#--------------------------------- Section 2 Functions ----------------------------------#
def draw_one():
        C = (random.choice(player_deck))
        user.hand.append(C)
        print("You were dealt ", end=" ")
        user.score = sum(user.hand)
        print(user.hand)
        print(user.score)
        if user.score >21:
            user.bust = True
#--------------------------------- Section 3 Functions ----------------------------------#
def result_text(): # results blurb
        print("You: ", end=" ")
        print(user.hand, end=" ")
        print(user.score)
        print("The House:", end=" ")
        print(house.hand, end=" ")
def bank_text():
        print("Bank: ", end=" ")
        print(bank, end="  ")
        print("Chips")
def end_results():
    user.score = sum(user.hand)
    house.score = sum(house.hand)
    if user.score == house.score: # tie aka Push
        print("Results: Push")
        result_text()
        house.score = sum(house.hand)
        print(house.score)
        bank_text()
    if user.score > house.score and user.bust == False:
        self.bank = self.bank + 3
        print("Results: Congratulations, you won!")
        result_text()
        print(house.score)
        bank_text()
    if house.score > user.score and house.bust == False:
        self.bank = self.bank - 2
        print("Results: The House won. Better luck next time.")
        result_text()
        print(house.score)
        bank_text()
#-------------------------------- Menu Functions --------------------------------------#
def the_rules():
    print("Rules go here.")
def the_credits():
    print("The credits go here")
#-------------------------------------- Loops -----------------------------------------#

# Set player's starting ammount of chips (20 chips = 10 plays, 2 chips are bet per game)
bank = 20

# The main/outer loop
hello = input("Would you like to play Blackjack (y/n)?    ")
if hello == "y":
    game_loop = True
    while game_loop:
        player_deal()
        house_deal()
        while user.score < 22:
            hit = input("Would you like another card (y/n)?    ")
            if hit == "y":
                draw_one()
            elif hit == "n":
                print("Okay, let's see how you did.")
                end_results()
                game_loop = False
            elif user.score > 21:
                print("Player Bust!")
                game_loop = False
            else:
                print("Please answer y or n.     ")
elif hello == "n":
    print("Bye!")
    game_loop = False
else:
    print("Please answer y or n.     ")





#-------------------------------- old --------------------------------------------------#

#def ask():
#    hit = input("Would you like another card (y/n)?    ")
#    if hit == "y":
#        draw_one()
#    elif hit == "n":
#        end_results()
#    else:
#        print("Please answer y or n.")


#def game_loop():
#    game = True
#    while game == True:
#        print("Welcome to Mattchu's CLI Blackjack!")
#        Q = input("Please make a selection.1.Play Blackjack, 2.Read the rules, 3.Read the credits, 4.Exit program.")
#        if Q == "1":
#            S1 = True
#            while S1 == True:
#                player_deal()
#        if Q == "2":
#            the_rules()
#        if Q == "3":
#            the_credits()
#        if Q == "4":
#            exit("Thank you for playing. Good Bye.")
#    else:
#       ("Please answer y or n.")

#-------------------------------- Code ----------------------------------------------#
#game_loop()
#-------------------------------- Test ----------------------------------------------#
#player_deal()
#print(user.blackjack)
#house_deal()
#print(house.hand, end=" ")
#print(house.score)
#print(house.bust)
#draw_one()
#print(user.bust)
#end_results()