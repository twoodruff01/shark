# Copyright © Thomas Woodruff, 2022

# This file is part of shark.

# Shark is free software: you can redistribute it and/or modify it under the terms of 
# the GNU Affero General Public License as published by the Free Software Foundation.

# Shark is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License along with shark. If 
# not, see <https://www.gnu.org/licenses/>.

from . import game

# TODO: Add player count as a CLI argument.
PLAYER_COUNT = 5

def run():
    new_game = game.Game(PLAYER_COUNT)
    new_game.print_deck()
    '''
    Create a new game.
    Decide if showing gui or not.
    Deal
    while not new_game.is_won():
        for player in players:
            action = func_timeout(player.get_action(new_game))
            new_game.apply_action(action)
    '''
