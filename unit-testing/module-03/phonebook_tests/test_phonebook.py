import pytest
from phonebook import Phonebook

# @pytest.fixture
# def phonebook(request):
#     phonebook = Phonebook()
#     def cleanup_phonebook():
#         phonebook.clear()
#     request.add_finalizer(cleanup_phonebook) # check the docs for a better mechanism
#     return Phonebook()

@pytest.fixture
def phonebook()
    return Phonebook()

def test_lookup_entry_by_name(phonebook):
    phonebook.add("Bob", "12345")
    assert "12345" == phonebook.lookup("Bob"), "Bob not found"

def test_phonebook_gives_access_to_names_and_numbers(phonebook):
    phonebook.add("Foobar", "12345")
    assert "Foobar" in phonebook.names()
    assert "12345" in phonebook.numbers()
    
def test_missing_entry_raises_KeyError(phonebook):
    #pytest.skip("WIP")
    with pytest.raises(KeyError):
        phonebook.lookup("foobar")