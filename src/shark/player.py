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

from . import constants

class Player():
    def __init__(self):
        self.hand = list()
        self.agent = None
        self.chips = 500  # TODO: Chips could be a class of their own or enums (discretisation).
        self.is_little_blind = False
        self.is_big_blind = False
    
    def receive_card(self, card):
        self.hand.append(card)
    
    def get_action(self, game_state):
        '''
        TODO: Game_state should have a variable containing the minimum call amount.
        TODO: Add the timeout in here.
        '''
        return None

    def __str__(self):
        return f'{[str(c) for c in self.hand]}'
    
    def get_small_blind_bet(self):
        '''
        TODO: Do something if they've run out of money or don't have enough.
        TODO: Allow changing the blind sizes somehow.
        '''
        self.is_little_blind = True
        if self.chips <= constants.BUY_IN:
            raise NotImplementedError("haven't figured those two cases out yet")
        else:
            self.chips -= constants.BUY_IN
        return constants.BUY_IN

    def get_big_blind_bet(self):
        '''
        TODO: Do something if they've run out of money or don't have enough.
        TODO: Allow changing the blind sizes somehow.
        '''
        self.is_big_blind = True
        if self.chips <= constants.BUY_IN // 2:
            raise NotImplementedError("haven't figured those two cases out yet")
        else:
            self.chips -= constants.BUY_IN // 2
        return constants.BUY_IN // 2
