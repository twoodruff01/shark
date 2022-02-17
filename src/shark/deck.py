# Copyright © Thomas Woodruff, 2022

# This file is part of shark.

# Shark is free software: you can redistribute it and/or modify it under the terms of 
# the GNU Affero General Public License as published by the Free Software Foundation.

# Shark is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License along with shark. If 
# not, see <https://www.gnu.org/licenses/>.

from . import card

class Deck():
    def __init__(self):
        self.cards = [card.Card(rank, suit) for rank in card.Rank for suit in card.Suit]
        self.shuffle()
 
    def shuffle(self):
        # TODO: Do this properly, to avoid bias in simulations.
        pass
