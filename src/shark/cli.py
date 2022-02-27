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

# NOTE: This file should not import any file related to game logic.
# TODO: Use CLI parser instead of constants.

import importlib


HOLE_CARDS   = 2
THINK_TIME   = 3
BUY_IN       = 6  # NOTE: This must be an even number.

# Users can add their newly created agents to a game here
#  by adding the filenames of their agents to this list in the same order
#  as they want them to play in. It's a bit like deciding which poker players 
#  will be sitting next to each other.
AGENTS = [
    'coward',
    'coward',
    'coward',
    'coward'
]

PLAYER_COUNT = len(AGENTS)


def load_agents():
    '''
    At run-time, find all agents that have had a file added to the /agents directory.

    Returns:
        list: containing instantiation methods for each agent class which has been loaded.
    '''
    agents = list()
    for file_name in AGENTS:
        module_path = '.'.join(['src', 'shark', 'agents', file_name])
        module = importlib.import_module(module_path)
        agent_class = getattr(module, get_class_name_from_file_name(file_name))
        agents.append(agent_class)
    return agents

def get_class_name_from_file_name(file_name):
    '''
    Assumes the following convention for agent files:
        file name will be lower caps and use underscore case.
    Assumes the following convention for agent class names:
        class name will be almost identical to file name, but will use camelcase instead.
    
    An example combo:
        file_name of  'best_agent_ever_seen_123'
        class_name of 'BestAgentEverSeen123'
    '''
    words = file_name.split('_')
    words = [word.capitalize() for word in words]
    return ''.join(words)
