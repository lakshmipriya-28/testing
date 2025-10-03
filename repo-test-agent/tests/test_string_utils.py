from src.utils import string_utils

def test_capitalize_words():
    assert string_utils.capitalize_words("hello world") == "Hello World"
