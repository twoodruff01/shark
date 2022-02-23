#    Copyright 2022 Thomas Woodruff

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from . import deck
from . import players
from . import constants
from . import action

import copy


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
        self.players  = players.Players(constants.PLAYER_COUNT)
        self.game_won = False
        self.pot      = 0

        # TODO: Figure out how to deal with betting and raising logic.
        self.raise_amount = constants.BUY_IN
        self.raise_index = None
        self.raised = False
        # self.call_amount = 0  # TODO: Pass to players when asking for action.

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
        TODO: This is really the crux of this whole program.

        goes around till everyone is equal and either in or out

        player at self.button + 1 puts in half the buy-in
        player at self.button + 2 puts in full buy-in
        players from self.button + 2 can fold, call, or raise (agent actions)
        if no-one raises:
            continue till you get back to self.button + 2
        if some-one raises:
            continue till you get back to them
        '''
        self.blind_bet(amount=self.players.next_player().get_small_blind_bet(), minimum=constants.BUY_IN // 2)
        self.blind_bet(amount=self.players.next_player().get_big_blind_bet(), minimum=constants.BUY_IN)
        while something:  # TODO: Till when?
            next_player = self.players.next_player()
            sanitised_game = self.sanitise()
            action = next_player.get_action(sanitised_game)
            self.apply_action(action)
    
    def blind_bet(self, amount, minimum):
        if amount < minimum:
            print('illegal addition to pot below minimum')
            raise NotImplementedError
        elif amount == minimum:
            self.pot += amount
        else:
            print('blind raised on pre-flop, is that legal?')
            raise NotImplementedError
    
    def apply_action(self, act):
        '''
        TODO: This method might just have to be unavoidably messy.
        '''
        if self.raised:
            # TODO: See if this action at least matches the raise.
            if act.type == action.ActionType.FOLD:
                raise NotImplementedError
            if act.type == action.ActionType.CALL:
                self.pot += act.amount
                raise NotImplementedError
            if act.type == action.ActionType.RAISE:
                self.pot += act.amount
                raise NotImplementedError
            if act.type == action.ActionType.CHECK:
                raise NotImplementedError
            else:
                raise TypeError('nonexistent action type given')
        else:
            # TODO: Don't have to worry about raises.
            if act.type == action.ActionType.FOLD:
                print('why would you fold if noone has raised?')
                raise NotImplementedError
            if act.type == action.ActionType.CALL:
                self.pot += act.amount
                raise NotImplementedError
            if act.type == action.ActionType.RAISE:
                self.pot += act.amount
                raise NotImplementedError
            if act.type == action.ActionType.CHECK:
                raise NotImplementedError
            else:
                raise TypeError('nonexistent action type given')

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
    
    def sanitise(self):
        '''
        TODO: Remove anything from the game state that you don't want individual players to see
         i.e. the other players' cards...
        '''
        return copy(self)
    
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
