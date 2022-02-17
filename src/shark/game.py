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
    def __init__(self, player_count):
        if player_count <= 1:
            print('player count too low')
            exit(1)
        self.deck = deck.Deck()
        self.players = [player.Player() for _ in range(player_count)]

    def print_deck(self):
        for card in self.deck.cards:
            print(card)
