import pytest

from src.shark.poker.game import Game
from src.shark.poker.player import Player
from src.shark.poker.players import Players

from .agents.test_agent import TestAgent

@pytest.fixture
def test_agent_object():
    return TestAgent()

@pytest.fixture
def game_object():
    return Game()

@pytest.fixture
def player_object():
    return Player(index=1, agent=TestAgent)

@pytest.fixture
def players_object():
    players_list = [object for _ in range(5)]
    return Players(agents=players_list)
