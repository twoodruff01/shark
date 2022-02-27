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

from . import card

class Deck():
    def __init__(self):
        self.cards = [card.Card(rank, suit) for rank in card.Rank for suit in card.Suit]
        self.shuffle()
 
    def shuffle(self):
        # TODO: Do this properly, to avoid bias in simulations.
        pass

    def deal(self):
        return self.cards.pop()

    def print_cards(self):
        for card in self.cards:
            print(card)
