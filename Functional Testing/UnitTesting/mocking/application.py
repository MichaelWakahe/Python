"""
Application under test.
"""

def get_next_person(user):
    person = get_random_person()
    while person in user['people_seen']:
        person = get_random_person()
    return person


def get_random_person():
    """
    This is meant to simulate getting a random person from a database
    :return: 
    """
    return "someone"