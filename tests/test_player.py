from src.shark.poker.card import Card, Suit, Rank
import pytest

def test_has_funds(player_object):
    assert player_object.has_funds(player_object.chips)

def test_take_bet(player_object):
    amount = player_object.chips
    expected = 0
    player_object.take_bet(amount)
    assert player_object.chips == expected

def test_take_bet_exception(player_object):
    amount = player_object.chips + 1
    with pytest.raises(Exception):
        player_object.take_bet(amount)

def test_receive_card(player_object):
    expected = [
        Card(Rank.SEVEN, Suit.DIAMOND),
        Card(Rank.ACE, Suit.HEART),
    ]
    for card in expected:
        player_object.receive_card(card)
    assert player_object.hand == expected
