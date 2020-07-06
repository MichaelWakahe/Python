from Houses import House, BetterHouse
from com.example.WashCleaner import Washer
from com.example.VacuumCleaner import Vacuumer

"""
This class demonstrates the Dependency Injector
"""
if __name__ == '__main__':
    # house = House()
    # house.clean_up()

    betterHouse = BetterHouse(Washer())
    betterHouse.clean_up()
    betterHouse.another_clean_up(Vacuumer())
