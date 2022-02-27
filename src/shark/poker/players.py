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
    '''
    def __init__(self, agents):
        self.players        = [player.Player(i, agent) for agent, i in zip(agents, range(len(agents)))]
        self.__better_index = self._better_index()
        self.button       = 0

    def _better_index(self):
        '''
        For 5 players the idea is: 0 1 2 3 4 -> 0 1 2 3 4 -> 0 1 2 3 4 -> ...
        '''
        i = self.button + 1
        while True:
            if i >= len(self.players) - 1:
                i = 0
                yield i
            else:
                i += 1
                yield i

    def next_player(self):
        return self.players[next(self.__better_index)]
    
    def move_button(self):
        if self.button == len(self.players) - 1:
            self.button = 0
        else:
            self.button += 1
        self.__better_index = self._better_index()
        print(f'button moved to player {self.button}')
    
    def majority_folded(self):
        return sum([player.folded for player in self.players]) == 1
