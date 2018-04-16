from com.example.DustCleaner import Duster
from com.example.Cleaner import Cleaner

"""
Our first house
"""
class House:

    def __init__(self):
        self.cleaner = Duster()

    def clean_up(self):
        cleaning_action = self.cleaner.do_some_cleaning()
        print(cleaning_action)


"""
Our improved house
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
