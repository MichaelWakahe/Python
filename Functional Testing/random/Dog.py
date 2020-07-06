class Dog:
    count = 0 # this is a class variable
    dogs = [] # this is a class variable

    def __init__(self, name):
        self.name = name #self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n): # this is an instance method
        print("{} says: {}".format(self.name, "woof! " * n))

    def rollCall(n): #this is implicitly a class method (see comments below)
        print("There are {} dogs.".format(Dog.count))
        if n >= len(Dog.dogs) or n < 0:
            print("They are:")
            for dog in Dog.dogs:
                print("  {}".format(dog))
        else:
            print("The dog indexed at {} is {}.".format(n, Dog.dogs[n]))