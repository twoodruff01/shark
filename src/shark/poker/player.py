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

class Player():
    def __init__(self, index, agent):
        self.index           = index
        self.hand            = list()
        self.agent           = agent()
        self.chips           = 500  # TODO: Chips could be a class of their own or enums (discretisation).
        self.is_little_blind = False
        self.is_big_blind    = False
        self.folded          = False
    
    def receive_card(self, card):
        self.hand.append(card)
    
    def get_action(self, game_state):
        '''
        TODO: Add the timeout in here.
        TODO: Can use some fancy multiprocessing here if you want, to implement strict timeouts.
        TODO: Pass in modified copy of self (to avoid changing chips).
        '''
        return self.agent.get_action(game_state, self)
    
    def small_blind_bet(self):
        '''
        TODO: Do something if they've run out of money or don't have enough.
        TODO: Allow changing the blind sizes somehow.
        '''
        self.is_little_blind = True
        if self.chips < cli.BUY_IN // 2:
            raise NotImplementedError("small blind doesn't have enough chips")
        elif self.chips == cli.BUY_IN // 2:
            raise NotImplementedError("small blind has exactly sufficient chips")
        else:
            self.chips -= cli.BUY_IN // 2
        return cli.BUY_IN // 2

    def big_blind_bet(self):
        '''
        TODO: Do something if they've run out of money or don't have enough.
        TODO: Allow changing the blind sizes somehow.
        '''
        self.is_big_blind = True
        if self.chips < cli.BUY_IN:
            raise NotImplementedError("big blind doesn't have enough chips")
        elif self.chips == cli.BUY_IN // 2:
            raise NotImplementedError("big blind has exactly sufficient chips")
        else:
            self.chips -= cli.BUY_IN
        return cli.BUY_IN
    
    def has_funds(self, amount):
        return amount <= self.chips
    
    def take_bet(self, amount):
        if self.chips - amount < 0:
            raise Exception('tried to decrement player chips below 0')
        self.chips -= amount

    def __str__(self):
        return f'{[str(c) for c in self.hand]}'
