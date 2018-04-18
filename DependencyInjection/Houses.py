from com.example.DustCleaner import Duster
from com.example.Cleaner import Cleaner

"""
Our first house.
Here we have tight coupling with a Cleaner type of object.
"""
class House:

    def __init__(self):
        self.cleaner = Duster()

    def clean_up(self):
        cleaning_action = self.cleaner.do_some_cleaning()
        print(cleaning_action)


"""
Our improved house.
It demonstrates Dependency Injection both at the constructor and at method level
N.B. the __init__ method is strictly not a constructor.
"""
class BetterHouse:

    def __init__(self, Cleaner):
        self.cleaner = Cleaner

    def clean_up(self):
        cleaning_action = self.cleaner.do_some_cleaning()
        print(cleaning_action)

    def another_clean_up(self, Cleaner):
        cleaning_action = Cleaner.do_some_cleaning()
        print(cleaning_action)
