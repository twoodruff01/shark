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
