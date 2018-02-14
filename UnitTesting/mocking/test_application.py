from application import get_next_person
from mock import patch


"""
Application to demonstrate mocking.
"""

@patch("application.get_random_person")
def test_new_person(mock_get_rand_person):
    # arrange
    user = {'people_seen' : []}
    expected_person = 'Katie'
    mock_get_rand_person.return_value = 'Katie'

    # action
    actual_person = get_next_person(user)

    # assert
    assert actual_person == expected_person


# Run the test
test_new_person()