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

class Agent():
    '''
    All custom agents written by users should inherit from this class.
    '''

    def get_action(self, game_state, player):
        '''
        Agents will be given:
            - a copy of the game_state which has had some information removed.
            - a copy of the player object that represents them.
        '''
        raise NotImplementedError('you need to override the get_action method with your own version')
