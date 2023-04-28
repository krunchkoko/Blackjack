#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


playing = True


# In[ ]:


class Card:
    
    def __init__(self,suits,ranks):
        self.suits = suits
        self.ranks = ranks
    
    def __str__(self):
        return self.ranks + ' of ' + self.suits


# In[ ]:


card = Card('Hearts','Ace')


# In[ ]:


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                newcard = Card(suits,ranks)
                self.deck.append(newcard)


    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()


# In[ ]:


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        for suit in suits:
            for rank in ranks:
                newcard = Card(suits,ranks)
                self.cards.append(newcard.values)
                self.value = self.value + int(sum(self.cards))
            return self.value

    
    def adjust_for_ace(self):
        while self.value > 21:
            if self.ranks == 'Ace':
                self.value == self.value - 10
            else:
                pass


# In[ ]:


class Chips:
    
    def __init__(self,total,bet):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total = self.total + self.bet
    
    def lose_bet(self):
        self.total = self.total - self.bet


# In[ ]:


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How much do you wish to bet? '))
        except:
            print ('An error occurred! Please try again!')
        else:
            if chips.bet > chips.total:
                return (f'Bet cannot exceed {chips.total}')
            else:
                break


# In[ ]:


def hit(deck,hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()
        


# In[ ]:


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        
        x= input('hit or stay? ')
        
        if x == 'hit':
            hit(deck,hand)
        elif x == 'stay':
            print('Player stay and dealer will now play. ')
            playing = False
            break
        else:
            pass
        break
            
    
        


# In[ ]:


def show_some(player,dealer):
    
    print ("Player has ", *player.cards)
    print ("Dealer first card hidden, second card is", dealer.cards[1])
    
def show_all(player,dealer):
    
    print ('Player has cards of' , *player.cards)
    print ('Wtih value of',player.value)
    print ('Dealer has cards of' , *dealer.cards)
    print ('Wtih value of',dealer.value)


# In[ ]:


def player_busts(player,dealer,chips):
    print('Player has bust.')
    print(f'Player lost {chips.bet}')
    return chips.lose_bet

def player_wins(player,dealer,chips):
    print('Player value greater than dealer, player has won.')
    print(f'Player won {chips.bet}')
    return chips.win_bet

def dealer_busts(player,dealer,chips):
    print('Dealer has bust.')
    print(f'Player won {chips.bet}')
    return chips.win_bet
        
def dealer_wins(player,dealer,chips):
    print('Dealer value greater than player, player has lost.')
    print(f'Player lost {chips.bet}')
    return chips.lose_bet
    
def push(player,dealer):
    print('It is a tie!')


# In[ ]:


while True:
    # Print an opening statement
    print('Welcome to a game of Blackjack!')
    
    # Create & shuffle the deck, deal two cards to each player
    new_deck = Deck()
    new_deck.shuffle()
    
    player = Hand()
    dealer = Hand()
    
    for x in range(2):
        player.add_cards(new_deck.deal())
        dealer.add_cards(new_deck.deal())
           
    # Set up the Player's chips
    chips = Chips(total,bet)
    
    # Prompt the Player for their bet
    
    take_bet(chips)

    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)
   
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)

        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player,dealer,chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
        while dealer.value<17:
            hit(deck,dealer)
                
        # Show all cards
        show_all(player,dealer)
    
        # Run different winning scenarios
        if dealer.value>21:
            dealer_busts(player,dealer,chips)
            
        elif player.value > dealer.value:
            player_wins(player,dealer,chips)
            
        elif dealer.value > player.value:
            dealer_wins(player,dealer,chips)
            
        else:
            push(player,dealer)
    
    # Inform Player of their chips total 
    print(f'Currently you have {chips.total} left.')
    
    # Ask to play again
    replay = input('Play again? Y/N').upper()
        
    if replay == 'Y':
        playing = True
    elif replay == 'N':
        playing = False
        print('Thank you for playing.')
        break
    else:
        pass


# In[ ]:




