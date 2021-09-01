from creature import Creature
from item import Item
from location import Location

def process_locations(source):
    """
    Parameters:
    - `source`: The (path to) a configuration file as described under the
                heading `<PATHS>` (page 3 of the assignment description).

    TODO: Read the given configuration file and return a list of Location
    objects based on the file's contents.
    """
    file_open=open(source)
    file_read=file_open.readlines()
    file_read_filter=[]
    line1=[]
    # cancel space
    for line in file_read:
        line1=line.strip()
        if len(line1)!=0:
            file_read_filter.append(line)
    # change direction
    file_read_final=[]
    location_check=[]
    direction_check=[]
    destination_check=[]
    for line in file_read_filter:
        word=line.split(">")
        word_change=(word[1].strip()).lower()
        word[0]=word[0].strip()
        word[2]=word[2].strip()
        word[1]=word_change
        file_read_final.append(">".join(word))
        location_check.append(word[0])
        direction_check.append(word[1])
        destination_check.append(word[2])
    #make a list of location string
    location_list=[]
    location_list_final=[]
    for line in file_read_final:
        word=line.split(">")
        location_list.append(word[0])
        location_list.append(word[2])
    location_list_final=list(set(location_list))
    #make a list of location object
    location_list_object=[]
    for name in location_list_final:
        p=Location(name)
        location_list_object.append(p)
        n=0
        while n+1<=len(location_check):
            if location_check[n]==name:
                p.add_direction(direction_check[n])
                p.add_destination(destination_check[n])
                n+=1
            else:
                n+=1
    return location_list_object
                
        
def process_items(source,locations):
    file_items=open(source)
    file_items_readlines=file_items.readlines()
    item_object_list=[]
    if len(file_items_readlines)==0:
        return item_object_list

    item_location_list=[]
    #make a list of item object

    for item in file_items_readlines:
        word=item.split('|')
        if len(word)==5:
            item_object_list.append(Item(word[0].strip(),word[1].strip(),word[2].strip(),word[3].strip(),word[4].strip()))
        else:
            continue

    return item_object_list
    
    
        
        
        
        
        
        
    """
    Parameters:
    - `source`: The (path to) a configuration file as described under the
                heading `<ITEMS>` (page 4 of the assignment description.)
    - `locations`: A list of Location objects.

    TODO: Read the given configuration file and return a list of Item objects
    based on the file's contents. You might also want to link the new Item
    objects to their starting Locations.
    """

def process_creatures(source, locations):
    file_creatures=open(source)
    file_creatures_readlines=file_creatures.readlines()
    #make a list of object
    creature_list=[]
    if len(file_creatures_readlines)==0:
        return creature_list
    creature_location_list=[]
    location_list=[]
    for n in locations:
        location_list.append(n.name)
    #make a list of creature object
    for creature in file_creatures_readlines:
        word=creature.split('|')
        if len(word)==5:
            creature_list.append(Creature(word[0].strip(),word[1].strip(),word[2].strip(),word[3].strip(),word[4].strip()))
        else:
            continue
    
    return creature_list
    
    
    
    
    
    
    """
    Parameters:
    - `source`: The (path to) a configuration file as described under the
                heading `<CHASERS>` (page 5 of the assignment description.)
    - `locations`: A list of Location objects.

    TODO: Read the given configuration file and return a list of Creature
    objects based on the file's contents. You might also wan to find a way to
    link each Goosechaser with their starting locations.
    """

def process_exits(source, locations):
    
    """
    Parameters:
    - `source`: The (path to) a configuration file as described under the
                heading `<EXITS>` (page 5 of the assignment description.)
    - `locations`: A list of Location objects.

    TODO: Read the given configuration file and use this to indicate which
    Location objects allow the use of the FLEE command.
    """
    
