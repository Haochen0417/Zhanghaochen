"""
TODO: Define the Location class, as described on page 6 of the assignment
description. You are allowed to change the scaffold somewhat to better suit
the needs of your program (change function parameters, etc.)

You are allowed to create as many methods as you feel are necessary.
"""
class Location:
    def __init__(self, name):
        self.name=name
        self.direction=[]
        self.destination=[]
        self.item=[]
        self.creature=[]
        self.exit=[]
        """
        TODO: Constructor; instantiates a Location object. You may modify
        this constructor so that it can receive additional arguments (or
        fewer arguments).
        """

    def add_item(self, item):
        self.item.append(item)
        """
        TODO: Might help when something is DROPped at a Location, but
        but can be useful in other ways.
        """

    def remove_item(self, item):
        self.item.remove(item)
        """
        TODO: Might help when something is TAKEn from a Location, but
        but can be useful in other ways.
        """
        
# You can define more methods here!
    def add_direction(self,direction):
        self.direction.append(direction)
        
    def add_destination(self,destination):
        self.destination.append(destination)
    def add_creature(self,creature):
        self.creature.append(creature)
    def remove_creature(self,creature):
        self.creature.remove(creature)
    def add_exit(self,exit):
        self.exit.append(exit)
