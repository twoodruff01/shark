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
