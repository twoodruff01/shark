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

import enum


class Action():

    def __init__(self, action_type, amount=None):
        if not isinstance(action_type, ActionType):
            raise TypeError
        elif amount and action_type != ActionType.RAISE:
            raise AttributeError('only a raise action should have an amount associated with it')
        self.type = action_type
        self.amount = amount


class ActionType(enum.Enum):
    FOLD  = enum.auto()
    CALL  = enum.auto()
    RAISE = enum.auto()
    CHECK = enum.auto()
