
def test_1(game_object):
    game_object.run()
    assert isinstance(game_object, object), "is object"
