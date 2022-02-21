# Copyright © Thomas Woodruff, 2022

# This file is part of shark.

# Shark is free software: you can redistribute it and/or modify it under the terms of 
# the GNU Affero General Public License as published by the Free Software Foundation.

# Shark is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License along with shark. If 
# not, see <https://www.gnu.org/licenses/>.

import enum

class Rank(enum.Enum):
    TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE = range(13)

class Suit(enum.Enum):
    SPADE, CLUB, DIAMOND, HEART = range(4)

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f'{str(self.rank.name)} {str(self.suit.name)}s'.lower()
