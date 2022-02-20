# Copyright © Thomas Woodruff, 2022

# This file is part of shark.

# Shark is free software: you can redistribute it and/or modify it under the terms of 
# the GNU Affero General Public License as published by the Free Software Foundation.

# Shark is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License along with shark. If 
# not, see <https://www.gnu.org/licenses/>.

from . import deck
from . import player

class Game():
    '''
    Figure out how to move dealer
    '''
    def __init__(self, player_count):
        if player_count <= 1:
            print('player count too low')
            exit(1)
        self.deck = deck.Deck()
        self.players = [player.Player() for _ in range(player_count)]

    def print_deck(self):
        for card in self.deck.cards:
            print(card)
    
    def round(self):
        self.deal()
        self.bet()
        self.flop()
        self.bet()
        self.turn()
        self.bet()
        self.river()
        self.bet()

    def deal(self):
        '''
        deal one card per player in clockwise direction from dealer's left
        do it again
        '''
        pass

    def bet(self):
        '''
        goes around till everyone is equal and either in or out
        '''
        pass

    def flop(self):
        '''
        three cards
        '''
        pass
    
    def turn(self):
        '''
        one card
        '''
        pass
    
    def river(self):
        '''
        last chance!
        '''
        pass
