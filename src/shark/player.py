# Copyright © Thomas Woodruff, 2022

# This file is part of shark.

# Shark is free software: you can redistribute it and/or modify it under the terms of 
# the GNU Affero General Public License as published by the Free Software Foundation.

# Shark is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License along with shark. If 
# not, see <https://www.gnu.org/licenses/>.

class Player():
    def __init__(self):
        self.hand = None
        self.agent = None
    
    def get_action(self, game_state):
        pass

'''
Bet Actions:
    fold
    call
    raise
    reraise
    check
'''
