from ..scripts.discover_data_processing import say_hello

def test_say_hello():
    result = say_hello("Marvin")
    assert result == "Hello, Marvin!"