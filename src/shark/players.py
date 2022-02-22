# Copyright © Thomas Woodruff, 2022

# This file is part of shark.

# Shark is free software: you can redistribute it and/or modify it under the terms of 
# the GNU Affero General Public License as published by the Free Software Foundation.

# Shark is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License along with shark. If 
# not, see <https://www.gnu.org/licenses/>.

from . import player

class Players():
    '''
    Pretty much a circular list.
    TODO: Increment button after a play.
    '''
    def __init__(self, player_count):
        self.players  = [player.Player() for _ in range(player_count)]
        self.better_index = self._better_index()
        self.button = 0

    def next_player(self):
        return self.players[self.button + next(self.better_index)]
    
    @staticmethod
    def _better_index(self):
        '''
        For 5 players the idea is: 0 1 2 3 4 -> 0 1 2 3 4 -> 0 1 2 3 4 -> ...
        '''
        i = 1
        while True:
            yield i
            if i >= len(self.players) - 1:
                i = 0
            else:
                i += 1
