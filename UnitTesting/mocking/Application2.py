"""
An application under test.
"""

class Application2:
    def get_next_person(self, user):
        person = self.get_random_person()
        while person in user['people_seen']:
            person = self.get_random_person()
        return person

    def get_random_person(self):
        """
        This is meant to simulate getting a random person from a database
        :return:
        """
        return "someone"