from Application2 import Application2
from mock import patch

"""
Application to demonstrate mocking.
"""

@patch.object(Application2, "get_random_person")
def test_new_person(mock_get_rand_person):
    # arrange
    app = Application2()
    user = {'people_seen' : []}
    expected_person = 'Katie'
    mock_get_rand_person.return_value = 'Katie'

    # action
    actual_person = app.get_next_person(user)

    # assert
    assert actual_person == expected_person


# Run the test
test_new_person()