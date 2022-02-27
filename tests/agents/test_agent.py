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

from src.shark.agents import agent
from src.shark.poker import action


class TestAgent(agent.Agent):
    def get_action(self, game_state, player):
        print(f'player {player.index} TestAgent returns action fold')
        return action.Action(action.ActionType.FOLD)
