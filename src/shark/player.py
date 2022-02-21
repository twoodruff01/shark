# Copyright © Thomas Woodruff, 2022

# This file is part of shark.

# Shark is free software: you can redistribute it and/or modify it under the terms of 
# the GNU Affero General Public License as published by the Free Software Foundation.

# Shark is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License along with shark. If 
# not, see <https://www.gnu.org/licenses/>.

from . import constants

class Player():
    def __init__(self):
        self.hand = list()
        self.agent = None
        self.chips = 500  # TODO: Chips could be a class of their own or enums (discretisation).
    
    def receive_card(self, card):
        self.hand.append(card)
    
    def get_action(self, game_state):
        '''
        TODO: Create class.
        '''
        return None

    def __str__(self):
        return f'{[str(c) for c in self.hand]}'
    
    def get_small_blind_bet(self):
        '''
        TODO: Do something if they've run out of money or don't have enough.
        TODO: Allow changing the blind sizes somehow.
        '''
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
        if self.chips <= constants.BUY_IN // 2:
            raise NotImplementedError("haven't figured those two cases out yet")
        else:
            self.chips -= constants.BUY_IN // 2
        return constants.BUY_IN // 2


'''
Bet Actions:
    fold
    call
    raise
    reraise
    check
'''
