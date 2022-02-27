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

from .. import cli
from . import deck
from . import action
from . import players


class Game():
    '''
    '''
    def __init__(self):
        if cli.PLAYER_COUNT <= 1:
            print('player count too low')
            exit(1)
        elif cli.PLAYER_COUNT > 9:
            print('player count too high')
            exit(1)
        self.players  = players.Players(cli.load_agents())
        self.deck     = deck.Deck()
        self.game_won = False
        self.pot      = 0

        # TODO: Figure out how to deal with betting and raising logic.
        self.raise_index  = 1  # Big blind raises by default
        self.raise_amount = cli.BUY_IN

    def tournament(self):
        print(f'starting new tournament')
        # while not self.game_won:
        #     self.play()
        for _ in range(7):
            self.play()
        print('tournament finished')

    def play(self):
        print(f'playing a new game')
        self.deal()
        self.first_bet()
        # self.flop()
        # self.bet()
        # self.turn()
        # self.bet()
        # self.river()
        # self.bet()
        print('game finished')
        self.cleanup_play()

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

    def deal(self):
        '''
        Deal one card per player in clockwise direction from dealer's left.
        Repeat.
        TODO: Add burn.
        '''
        for _ in range(cli.HOLE_CARDS):
            for player in self.players.players:
                player.receive_card(self.deck.deal())
        for i in range(cli.PLAYER_COUNT):
            print(f'player {i + 1} cards: {self.players.players[i]}')

    def first_bet(self):
        '''
        TODO: This is really the crux of this whole program.

        goes around till everyone is equal and either in or out

        player at button + 1 puts in half the buy-in
        player at button + 2 puts in full buy-in
        players from button + 2 can fold, call, or raise (agent actions)
        if no-one raises:
            continue till you get back to button + 2
        if some-one raises:
            continue till you get back to them
        '''
        next_player = self.players.next_player()
        self.blind_bet(amount=next_player.small_blind_bet(), is_small=True, index=next_player.index)

        next_player = self.players.next_player()
        self.blind_bet(amount=next_player.big_blind_bet(), is_small=False, index=next_player.index)

        next_player = self.players.next_player()
        while not self.players.majority_folded() and next_player.index != self.raise_index:  # TODO: Till when?
            if not next_player.folded:
                sanitised_game = self.sanitise()
                action = next_player.get_action(sanitised_game)
                self.apply_action(action, next_player)
            next_player = self.players.next_player()
        
    def blind_bet(self, amount, is_small, index):
        if is_small:
            minimum = cli.BUY_IN // 2
        else:
            minimum = cli.BUY_IN

        if amount < minimum:
            print('illegal addition to pot below minimum')
            raise NotImplementedError
        elif amount == minimum:
            self.pot += amount
            blind_string = 'small' if is_small else 'big'
            print(f'player {index} ({blind_string} blind) puts in {amount}')
        else:
            print('blind raised on pre-flop, is that legal?')
            raise NotImplementedError
    
    def apply_action(self, act, player):
        '''
        If a player returns an illegal action, they will be made to fold.
        TODO: Deal with negative amounts.
        '''
        if act.amount and act.amount < 0:
            player.folded = True
            print(f'player {player.index} returned action with negative amount: folding instead')
            return
        elif act.amount and act.amount == 0:
            player.folded = True
            print(f'player {player.index} returned action with 0 amount: folding instead')
            return

        if act.type == action.ActionType.FOLD:
            player.folded = True
            print(f'player {player.index} folds')
        elif act.type == action.ActionType.CALL:
            if player.has_funds(self.raise_amount):
                player.take_bet(self.raise_amount)
                self.pot += self.raise_amount
                print(f'player {player.index} calls {self.raise_amount} chips')
            else:
                print(f'player {player.index} called {self.raise_amount} but is short: folding instead')
                player.folded = True
        elif act.type == action.ActionType.RAISE:
            if player.has_funds(act.amount):
                player.take_bet(act.amount)
                self.pot += act.amount
                self.raise_amount = act.amount
                self.raise_index = player.index
                print(f'player {player.index} raised {act.amount} chips')
            else:
                print(f'player {player.index} raised {act.amount} but is short: folding instead')
                player.folded = True
        elif act.type == action.ActionType.CHECK:
            raise NotImplementedError
        else:
            player.folded = True
            print(f'player {player.index} returned nonexistent action: folding instead')

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

    def sanitise(self):
        '''
        TODO: Remove anything from the game state that you don't want individual players to see
         i.e. the other players' cards...
        '''
        return self
    
    def cleanup_play(self):
        self.players.move_button()
        self.deck = deck.Deck()
        for player in self.players.players:
            player.hand.clear()
            player.folded = False
            # player.is_little_blind = False
            # player.is_big_blind = False
