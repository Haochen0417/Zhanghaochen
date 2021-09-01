"""
TODO: Define the Creature class, as described on page 10 of the assignment
description. You are allowed to change the scaffold somewhat to better suit
the needs of your program (change function parameters, etc.)

You are allowed to create as many methods as you feel are necessary.
"""

class Creature:
    def __init__(self, name, full_desc, terror_rating ,location, direction):
        self.name=name
        self.full_desc=full_desc
        self.terror_rating=terror_rating
        self.location=location
        self.direction=direction
        self.health=2
        self.item=[]
        """
        TODO: Constructor; instantiates a Creature class. You may modify
        this constructor so that it can receive additional arguments (or
        fewer arguments).
        """

    def take(self, item):       
        """
        TODO: A function that may be useful when a Creature TAKEs an Item
        object.
        """
        self.item.append(item)

    def drop(self, item):
        """
        TODO: A function that may be useful when a Creature DROPs an Item
        object.
        """
        self.item.remove(item)
    def get_terror_rating(self):
        """
        TODO: Returns a Creature's terror_rating.
        """
        if len(self.item)!=0:
            for a in self.item:
                self.terror_rating=int(self.terror_rating)+int(a.terror_rating)
        else:
            self.terror_rating=int(self.terror_rating)
    # These methods probably aren't enough! You can create more
    # methods here.
