#This code is for playing blackjack/21
import random

 # card deck consisting of numbers till 2 to 10 and all the face cards with value of 10 and ace card with value 11.
cards = [11,2,3,4,5,6,7,8,9,10,10,10]

# Dealer and player set of cards. Initially set to 0 cards indicated by list with no elements.
dealer = []
player = []

def win(c,d):
    '''Function for winning condition.'''
    print("Win!")
    print("Dealers cards: ", d,"\t Your cards: ", c)
    return

def loss(c,d):
    '''Function for losing condition.'''
    print("Bust")
    print("Dealers cards: ", d,"\t Your cards: ", c)
    return

def tie(c,d):
    '''Function for draw condition.'''
    print("Draw")
    print("Dealers cards: ", d,"\t Your cards: ", c)
    return

def draw():
    '''A card is drawn from the deck i.e.,a value from cards is selected.'''
    return cards[random.randint(0, len(cards)-1)]

def result(c, d):
    '''The score of dealer and player is compared.'''
    a = sum(c)
    b  = sum(d)
    if b>21:
        win(c,d)
        return
    elif (a==b):
        tie(c,d)
        return     
    elif (a<b) or (b==21):
        loss(c,d)
        return
    else:
        d.append(draw())
        result(c,d)

def playerdraw(player, dealer):
    '''Player draws a card i.e., a value from cards is selected.'''
    player.append(draw())
    if sum(player)==21:
        win(player, dealer)
        return
    elif sum(player)>21:
        loss(player, dealer)
        return
    else:
        print ("Your cards: ", player , "\t Dealers cards", dealer[1])
        if input("Draw card? y: ") == "y":
            playerdraw(player, dealer)
        else:
            result(player, dealer)
        return

def play():
    '''Start of the game.'''
    dealer = [draw(), draw()]
    player = [draw(), draw()]
    print ("Your cards: ", player , "\t Dealers cards", dealer[1])
    if sum(player) == 21:
        win(player, dealer)
        return
    else:
        if input("Draw? y: ") == "y":
            playerdraw(player, dealer)
        else:
            result(player, dealer)
        return 

while(1):
    k = input("Do you want to start the game? y/n: ")
    if k == "y":
        play()
    elif k == 'n':
        break
    else:
        print("Invalid input, Try again")
        


        


    