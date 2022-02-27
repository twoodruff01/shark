from src.shark.cli import get_class_name_from_file_name

def test_one_word():
    input = 'word'
    expected = 'Word'
    assert get_class_name_from_file_name(input) == expected

def test_two_words():
    input = 'word_again'
    expected = 'WordAgain'
    assert get_class_name_from_file_name(input) == expected

def test_two_words_numbers():
    input = 'word_again_123'
    expected = 'WordAgain123'
    assert get_class_name_from_file_name(input) == expected

def test_two_words_capitalised():
    input = 'Word_Again'
    expected = 'WordAgain'
    assert get_class_name_from_file_name(input) == expected
