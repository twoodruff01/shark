def test_next_player(players_object):
    expected = 1
    players_object.move_button()
    assert players_object.button == expected, 'move button 1'
