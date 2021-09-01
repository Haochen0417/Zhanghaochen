# You will need to import the Creature class.
from creature import Creature
from item import Item 
# You may need to import other classes. Remember, outside of the
# files given in the scaffold, the only module that you can import
# is `sys`.

def test_creatures_1():

    """
    Write your test case description and data as comments, like so.

    TODO: Code your first unit test! Remember, you need to define
    at least 5 tests.
    """
    #check can creature tkae item?
    dog=Creature('dog','just a dog','2','lily home','north')
    expected=['knife']
    dog.take('knife')
    actual=dog.item
    if actual!=expected:
        print("Test 1 failed.")
def test_creatures_2():
    #check can creature drop item?
    dog=Creature('dog','just a dog','2','lily home','north')
    expected=[]
    dog.take('knife')
    dog.drop('knife')
    actual=dog.item
    if actual!=expected:
        print("Test 2 failed.")
def test_creatures_3():  
    #can creature get_terror_rating and item become a object
    dog=Creature('dog','just a dog','2','lily home','north')
    knife=Item('knife','fruit knife','please be careful','2','lily home')
    expected=4
    dog.take(knife)
    dog.get_terror_rating()
    actual=dog.terror_rating
    if actual!=expected:
        print("Test 3 failed.")
def test_creatures_4(): 
    #complex check all function
    dog=Creature('dog','just a dog','2','lily home','north')
    knife=Item('knife','fruit knife','please be careful','2','lily home')
    expected=2
    dog.take(knife)
    dog.drop(knife)
    dog.get_terror_rating()
    actual=dog.terror_rating
    
    if actual!=expected:
        print("Test 4 failed.")
def test_creatures_5():
    #two item check
    dog=Creature('dog','just a dog','2','lily home','north')
    knife=Item('knife','fruit knife','please be careful','2','lily home')
    orange=Item('orange','bad orange','donnot eat','-2','lily home')
    expected=2
    dog.take(knife)
    dog.drop(knife)
    dog.take(orange)
    dog.take(knife)
    dog.get_terror_rating()
    actual=dog.terror_rating
    
    if actual!=expected:
        print("Test 5 failed.")    
        
        
        
test_creatures_1()   
test_creatures_2()       
test_creatures_3()   
test_creatures_4()    
test_creatures_5()    
    
    
    
    
    
    
    
    
    
# ===============================================================
#  Create additional test cases here! Don't forget to run them.
# ===============================================================
