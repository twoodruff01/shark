import pytest

from src.shark.game import Game

@pytest.fixture
def game_object():
    return Game()
