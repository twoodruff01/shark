# Copyright © Thomas Woodruff, 2022

# This file is part of shark.

# Shark is free software: you can redistribute it and/or modify it under the terms of 
# the GNU Affero General Public License as published by the Free Software Foundation.

# Shark is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License along with shark. If 
# not, see <https://www.gnu.org/licenses/>.

import math
import sys

from . import deck
from . import player
from . import constants

class Game():
    '''
    TODO: Figure out how to move dealer.
    '''
    def __init__(self):
        if constants.PLAYER_COUNT <= 1:
            print('player count too low')
            exit(1)
        elif constants.PLAYER_COUNT > 9:
            print('player count too high')
            exit(1)
        self.players  = [player.Player() for _ in range(constants.PLAYER_COUNT)]
        self.game_won = False
        self.button   = 0
        self.pot      = 0

    def tournament(self):
        print(f'starting new tournament')
        # while not self.game_won:
        #     self.play()
        for _ in range(7):
            self.play()
        print('tournament finished')

    def play(self):
        print(f'playing a new game')
        self.deck = deck.Deck()
        self.deal()
        self.first_bet()
        self.flop()
        self.bet()
        self.turn()
        self.bet()
        self.river()
        self.bet()
        print('game finished')
        self.move_button()
        self.collect_cards()
        print(f'button moved to {self.button}')

    def deal(self):
        '''
        Deal one card per player in clockwise direction from dealer's left.
        Repeat.
        '''
        for _ in range(constants.HOLE_CARDS):
            for player in self.players:
                player.receive_card(self.deck.deal())
        for i in range(constants.PLAYER_COUNT):
            print(f'player {i + 1} cards: {self.players[i]}')

    def first_bet(self):
        '''
        goes around till everyone is equal and either in or out
        for player in players:
            action = func_timeout(player.get_action(new_game))
            new_game.apply_action(action)
        '''
        '''
        player at self.button + 1 puts in half the buy-in
        player at self.button + 2 puts in full buy-in
        players from self.button + 2 can fold, call, or raise (agent actions)
        if no-one raises:
            continue till you get back to self.button + 2
        if some-one raises:
            continue till you get back to them
        '''
        # TODO: Improve betting logic to maybe not use indexes as directly.
        self.pot += self.get_player(self.button + 1).get_small_blind_bet()  # TODO: Track the fact that they have to match the pot.
        self.pot += self.get_player(self.button + 2).get_big_blind_bet()
        for i in range(self.button + 3, int(sys.maxsize - 1)):
            action = self.get_player(i).get_action(None)  # TODO: Timeout.
            self.apply_action(action)
    
    def get_player(self, index):
        return self.players[self.player_index(index)]
    
    def apply_action(self, action):
        pass

    def flop(self):
        '''
        three cards
        '''
        pass

    def bet(self):
        '''
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

    def move_button(self):
        '''
        Increments dealer index so that it loops back to zero after last player in list.
        '''
        if self.button == constants.PLAYER_COUNT - 1:
            self.button = 0
        else:
            self.button += 1
    
    @staticmethod
    def player_index(index):
        return index - constants.PLAYER_COUNT * (index // constants.PLAYER_COUNT)
    
    def collect_cards(self):
        '''
        Take the cards out of each player's hand before the next game.
        '''
        for player in self.players:
            player.hand = list()
    
    def print_deck(self):
        for card in self.deck.cards:
            print(card)

    # def play(self):
    #     self.deck = deck.Deck()
    #     for action in [self.deal,
    #                    self.bet,
    #                    self.flop,
    #                    self.bet,
    #                    self.turn,
    #                    self.bet,
    #                    self.river,
    #                    self.bet,
    #                    self.move_dealer]:
    #         if action():
    #             return False
