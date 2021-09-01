# A few import statements to start you off. This is how you can
# access the classes and functions defined in other classes;
# be sure to update this if you choose to create functions that
# are otherwise not imported!
import sys

from creature import Creature
from item import Item
from location import Location
from preprocessing import process_locations, process_exits,\
                          process_items, process_creatures

# ===============================================
#  Your code starts here!
# ===============================================
# solve the error
if len(sys.argv)<5:
  print("Usage: python3 game.py <PATHS> <ITEMS> <CHASERS> <EXITS>")
  sys.exit()
i=1
while i<=4:
  try:
    file=open(sys.argv[i])
    file.close()
    i+=1
  except FileNotFoundError:
      print("You have specified an invalid configuration file.")
      sys.exit()
file=open(sys.argv[1])
if (len(file.readlines()))==0:
  print("The game cannot run without any rooms :(")
  sys.exit()
file=open(sys.argv[3]) 
if (len(file.readlines()))==0:
  print("There is nothing chasing you!")
  sys.exit()

#input list of location object

location_list=process_locations(sys.argv[1])
n=0

# list of location name, according name to find the object location in list
l=[]
ll=[]
lll=[]
while n+1<=len(location_list):
  l.append(location_list[n].name)
  n+=1
item_list=process_items(sys.argv[2],location_list)
creature_list=process_creatures(sys.argv[3],location_list)
#create item location list
n=0
while n+1<=len(item_list):
  ll.append(item_list[n].location)
  n+=1
#add item into location object
n=0
while n+1<=len(ll):
  i=0
  while i+1<=len(l):
    if ll[n]==l[i]:
      location_list[i].add_item(item_list[n])
      break
    else:
      i+=1
  n+=1
#create creature location list
n=0
while n+1<=len(creature_list):
  lll.append(creature_list[n].location)
  n+=1
# location add creature:
n=0
while n+1<=len(lll):
  i=0
  while i+1<=len(l):
    if lll[n]==l[i]:
      location_list[i].add_creature(creature_list[n])
      break
    else:
      i+=1
  n+=1

#create exit_list
exitread=open(sys.argv[4])
exitreadlines=exitread.readlines()


#FLEE
def flee_exit(location_current,location_list):
  n=location_find(location_current,location_list)
  if location_list[n].exit==[]:
    a=1
    return a
  else:
    a=2
    return a
    
  
  
  
  
  
  
  
#function to control output
def output_word(locationname,direction,locationlist):
  location_list_name=[]
  count=0
  for r in locationlist:
    location_list_name.append(r.name)
  i=0
  while i+1<=len(locationlist):
    if locationname==locationlist[i].name:
      break
    else:
      i+=1
  for x in locationlist[i].direction:
    if direction==x:
      count=1
      break
    else:
      continue
  if count==1:
    n=0
    while n+1<=len(locationlist[i].direction):
      if direction==locationlist[i].direction[n]:
        break
      else:
        n+=1
    location=locationlist[i].destination[n]
    n=0
    while n+1<=len(locationlist):
      if location==locationlist[n].name:
        break
      else: 
        n+=1
    
    if len(locationlist[n].creature)==0:
      word='[ ]'
      return word
    else:
      word='[C]'
      return word
  else:
    word='   '
    return word

#start details
r=open(sys.argv[1])
r1=r.readlines()
r2=r1[0].split(">")
r3=r2[0].strip()
n=0
while n<len(location_list):
  if location_list[n].name==r3:
    break
  else:
    n+=1
location_current=location_list[n].name

goose_terror=5
goose_item=[]
def gooserate(goose_item):
  rate=5
  for item in goose_item:
    n=0
    while n<len(item_list):
      if item==item_list[n].short_name:
        break
      else:
        n+=1
    rate+=int(item_list[n].terror_rating)
  return rate
    
    

#maintain length at 16 character
def maintainlength(a,b):
  num=16
  num1=num-len(a)
  l=[]
  l.append(a.upper())
  n=0
  while n<num1:
    l.append(' ')
    n+=1
  l.append('|')
  l.append(' ')
  l.append(b)
  c=''.join(l)
  return c
# find where the location in the location list
def location_find(location_current,location_list):
  n=0
  while n<len(location_list):
    if location_current==location_list[n].name:
      break
    else:
      n+=1
  return n

#exit list
exitread=open(sys.argv[4])
exitreadlines=exitread.readlines()
for exits in exitreadlines:
  if exits=='':
    continue
  else:
    n=location_find(exits.strip(),location_list)
    location_list[n].add_exit(exits.strip())

# add take {item}
def commandappend(command_list,location_current,location_list):
  n=location_find(location_current,location_list)
  iteml=location_list[n].item
  item_list=[]
  for item in iteml:
    word='TAKE {}'.format(item.short_name)
    command_list.append(word.upper())
    a=item.short_name
    item_list.append(a.upper())
  return command_list,item_list
# add drop {item}
def commanddropappend(command_list,goose_item):
  for item in goose_item:
    word='DROP {}'.format(item.upper())
    command_list.append(word)
  return command_list
#item in goose_item and item in location
def ti(goose_item,item_current):
  item_list=[]
  for item in goose_item:
    item_list.append(item)
  for item in item_current:
    item_list.append(item.lower())
  return item_list  
#add look{item} and look{creature}
def commandlookappend(command_list,totalitem):
  for item in totalitem:
    
    word='LOOK {}'.format(item.upper())
    command_list.append(word)
  return command_list
#add look{creature}
def commandchaserappend(command_list,chaser_list):
  for chaser in chaser_list:
    a=chaser.name
    word='LOOK {}'.format(a.upper())
    command_list.append(word)
  return command_list
#find which path can go  
def movecommand(direction,location_current,location_list):
  i=0
  while i<len(location_list[n].direction):
    if direction==location_list[n].direction[i]:
      break
    else:
      i+=1
  location_current=location_list[n].destination[i]
  return location_current


#list of chaser 
def chaserlistcreate(location_current,location_list):
  n=location_find(location_current,location_list)
  chaser_list=[]
  for chaser in location_list[n].creature:
    chaser_list.append(chaser)
  return chaser_list
#find where the chaser in the liust
def chaserfind(chaser,creature_list):
  i=0
  while i<len(creature_list):
    if chaser.name==creature_list[i].name:
      break
    else:
      i+=1
  return i
#action of chaser, 4 diffenernt action together
def chaseract(creature_list,location_current,location_list,goose_item):
  for chaser in creature_list:
    
    i=chaserfind(chaser,creature_list)
    creature_list[i].direction=creature_list[i].direction.lower()
    n=location_find(location_current,location_list)
    cn=location_find(chaser.location,location_list)
    if chaser.location==location_current:
      rate=gooserate(goose_item)
      print('')
      print('{} is trying to catch you!'.format(chaser.name))
      if rate<=int(chaser.terror_rating):
        print("Oh no, you've been caught!")
        print('========= GAME OVER =========')
        sys.exit()
      else:
        chaser.health-=1
        if chaser.health==1:
          print('But your presence still terrifies them...')
        else:
          print("Oh no, you've been caught!")
          print('========= GAME OVER =========')
          sys.exit()
    elif location_list[n].name in location_list[cn].destination:
        
      location_list[cn].creature.remove(creature_list[i])
      creature_list[i].location=location_current
      location_list[n].creature.append(creature_list[i])
      print('')
      print('{} has arrived at {}.'.format(chaser.name,location_current))
    elif location_list[cn].item!=[]:
      creature_list[i].terror_rating=int(creature_list[i].terror_rating)+int(location_list[cn].item[0].terror_rating)
      location_list[cn].item.remove(location_list[cn].item[0])
    else:
      iii=0
      while creature_list[i].direction not in location_list[cn].direction and iii<=8:
        iii+=1
        if creature_list[i].direction=='north':
          creature_list[i].direction='northeast'

        elif creature_list[i].direction=='northeast':
          creature_list[i].direction='east'

        elif creature_list[i].direction=='east':
          creature_list[i].direction='southeast'

        elif creature_list[i].direction=='southeast':
          creature_list[i].direction='south'

        elif creature_list[i].direction=='south':
          creature_list[i].direction='southwest'

        elif creature_list[i].direction=='southwest':
          creature_list[i].direction='west'
        elif creature_list[i].direction=='west':
          creature_list[i].direction='northwest'

        elif creature_list[i].direction=='northwest':
          creature_list[i].direction='north'
      if iii<=8:
          
        location_list[cn].creature.remove(creature_list[i])
        ni=0
        while ni<len(location_list[cn].direction):
          if creature_list[i].direction==location_list[cn].direction[ni]:
            break
          else:
            ni+=1
        creature_list[i].location=location_list[cn].destination[ni]
        nii=location_find(creature_list[i].location,location_list)
        location_list[nii].creature.append(creature_list[i])
      
      











def map_print(location_current,location_list):
  #map
  a1=output_word(location_current,'northwest',location_list)
  a2=output_word(location_current,'north',location_list)
  a3=output_word(location_current,'northeast',location_list)
  b1=output_word(location_current,'west',location_list)
  b2=output_word(location_current,'east',location_list)
  c1=output_word(location_current,'southwest',location_list)
  c2=output_word(location_current,'south',location_list)
  c3=output_word(location_current,'southeast',location_list)
  #The first two lines
  if a1!='   ':
      if a2!='   ':
          if a3!='   ':
              print(a1,a2,a3)
              print('   \ | /')
          else:
              print(a1,a2)
              print('   \ |')
      else:
          if a3!='   ':
              print(a1,a2,a3)
              print('   \   /')
          else:
              print(a1)
              b='   \ '
              b=b.rstrip()
              print(b)
  else:
      if a2!='   ':
          if a3!='   ':
              print(a1,a2,a3)
              print('     | /')
          else:
              print(a1,a2)
              print('     |')
      else:
          if a3!='   ':
              print(a1,a2,a3)
              print('       /')
          else:
              print()
              print('')
  #The third line
  if b1!='   ':
      if b2!='   ':
          l=[b1,'[x]',b2]
          l1="-".join(l)
          print(l1)
      else:
          l=[b1,'[x]']
          l1="-".join(l)
          print(l1)
  else:
      if b2!='   ':
          l=['[x]',b2]
          l1="-".join(l)
          print(b1,l1)
      else:
          l=[b1,'[x]']
          l1=" ".join(l)
          print(l1)
  #The last two line
  if c1!='   ':
      if c2!='   ':
          if c3!='   ':
              d='   / | \   '
              d=d.rstrip()
              print(d)
              print(c1,c2,c3)

          else:
              print('   / |')
              print(c1,c2)

      else:
          if c3!='   ':
              d='   /   \   '
              d=d.rstrip()
              print(d)
              print(c1,c2,c3)

          else:
              print('   /')
              print(c1,)

  else:
      if c2!='   ':
          if c3!='   ':
              d='     | \   '
              d=d.rstrip()
              print(d)
              print(c1,c2,c3)

          else:
              print('     |')
              print(c1,c2)

      else:
          if c3!='   ':
              d='       \   '
              d=d.rstrip()
              print(d)
              print(c1,c2,c3)

          else:
              print('')
              print()
map_print(location_current,location_list)
#print details
print('You are now at: {}.'.format(location_current))
def desc(location_current,location_list):
  n=0
  while n<len(location_list):
    if location_current==location_list[n].name:
      break
    else:
      n+=1
  if location_list[n].item==[]:
    if location_list[n].creature==[]:
      print('There is nothing here.')  
    else:
      creature_print=[]
      for a in location_list[n].creature:
        creature_print.append(a.full_desc)
      creature_print1=" ".join(creature_print)
      print(creature_print1)
  else:
    if location_list[n].creature==[]:
      item_print=[]
      for a in location_list[n].item:
        item_print.append(a.full_desc)
      item_print1=" ".join(item_print)
      print(item_print1) 
    else:
      item_print=[]
      for a in location_list[n].item:
        item_print.append(a.full_desc)
      item_print1=" ".join(item_print)
      creature_print=[]
      for a in location_list[n].creature:
        creature_print.append(a.full_desc)
      creature_print1=" ".join(creature_print)
      print(item_print1+' '+creature_print1)     
desc(location_current,location_list)    
fleesee=flee_exit(location_current,location_list) 
if fleesee==2:
  print('The path to freedom is clear. You can FLEE this place.')

print('')
#create command list to verify if the command is right
command_list=['HELP','INV','LOOK','L','LOOK ME','LOOK HERE','NORTHWEST','NORTH','NORTHEAST','EAST','SOUTHEAST','WEST','SOUTHWEST','SOUTH','NW','N','NE','E','SE','S','SW','W','FLEE','HONK','Y','WAIT','QUIT']
command_list2=[]
for a in command_list:
  command_list2.append(a)
command_list1=command_list2
(command_list1,item_current)=commandappend(command_list1,location_current,location_list)
totalitem=ti(goose_item,item_current)
command_list1=commandlookappend(command_list1,totalitem)
chaser_list=chaserlistcreate(location_current,location_list)
command_list1=commandchaserappend(command_list1,chaser_list)

command=input('>> ').upper()

#just command here
while command!='QUIT':
    if command not in command_list1:
      commandword=command.split()
      if len(commandword)==2 and commandword[0]=='TAKE':
        print("You don't see anything like that here.")
        print('')
        command=input('>> ').upper()
      elif len(commandword)==2 and commandword[0]=='DROP':
        print("You don't have that in your inventory.")
        print('')
        command=input('>> ').upper()
      elif len(commandword)==2 and commandword[0]=='LOOK':
        print("You don't see anything like that here.")
        print('')
        command=input('>> ').upper()
      else:
        print("You can't do that.")
        print('')
        command=input('>> ').upper()
    else:
      if command=='QUIT':
        break
      if command=='HELP':
        print('HELP            - Shows some available commands.')
        print('INV             - Lists all the items in your inventory.')
        print('TAKE <ITEM>     - Takes an item from your current location.')  
        print('DROP <ITEM>     - Drops an item at your current location.')
        print('')
        print('LOOK or L       - Lets you see the map/location again.')
        print('LOOK <ITEM>     - Lets you see an item in more detail.')
        print('LOOK ME         - Sometimes, you just have to admire the feathers.')
        print('LOOK <CREATURE> - Sizes up a nearby creature.')
        print('LOOK HERE       - Shows a list of all items in the room.')
        print('')
        print('NORTHWEST or NW - Moves you to the northwest.')
        print('NORTH or N      - Moves you to the north.')
        print('NORTHEAST or NE - Moves you to the northeast.')
        print('EAST or E       - Moves you to the east.')
        print('')
        print('SOUTHEAST or SE - Moves you to the southeast.')
        print('SOUTH or S      - Moves you to the south.')
        print('SOUTHWEST or SW - Moves you to the southwest.')
        print('WEST or W       - Moves you to the west.')
        print('')
        print('FLEE            - Attempt to flee from your current location.')
        print('HONK or Y       - Attempt to scare off all creatures in the same location.')
        print('WAIT            - Do nothing. All other creatures will move around you.')
        print('QUIT            - Ends the game. No questions asked.')
        print('')
        command=input('>> ').upper()
      if command=='LOOK ME':
        print('You are a goose. You are probably quite terrifying.')
        rate=gooserate(goose_item)
        print('In fact, you have a terror rating of: {}'.format(rate))
        print('')
        command=input('>> ').upper()
      if command=='INV':
        if len(goose_item)==0:
          print("You are carrying nothing.")
        else:
          if len(goose_item)==1:
            print('You, a goose, are carrying the following item:')
          else:
            print('You, a goose, are carrying the following items:')
          for itemINV in goose_item:
            n=0
            while n<len(item_list):
              if itemINV==item_list[n].short_name:
                break
              else:
                n+=1
            print(' - {}'.format(item_list[n].item_name))
        print('')
        command=input('>> ').upper()
      #look command
      if command=='LOOK' or command=='L':
        map_print(location_current,location_list)
        print('You are now at: {}.'.format(location_current))
        desc(location_current,location_list)
        fleesee=flee_exit(location_current,location_list) 
        if fleesee==2:
            print('The path to freedom is clear. You can FLEE this place.')
        print('')
        command=input('>> ').upper()
      #move command
      if command=='N' or command=='NORTH':
        direction='north'
        n=location_find(location_current,location_list)
        if direction in location_list[n].direction:
          location_current=movecommand(direction,location_current,location_list)
          print('You move {}, to {}.'.format(direction,location_current))
          abc=0
          while abc<len(creature_list):
            creature_list[abc].health=2
            abc+=1
          chaseract(creature_list,location_current,location_list,goose_item)
          map_print(location_current,location_list)
          print('You are now at: {}.'.format(location_current))
          desc(location_current,location_list)
          fleesee=flee_exit(location_current,location_list) 
          if fleesee==2:
            print('The path to freedom is clear. You can FLEE this place.')
          command_list2=[]
          for a in command_list:
            command_list2.append(a)
          command_list1=command_list2
          (command_list1,item_current)=commandappend(command_list1,location_current,location_list)
          totalitem=ti(goose_item,item_current)
          command_list1=commandlookappend(command_list1,totalitem)
          chaser_list=chaserlistcreate(location_current,location_list)
          command_list1=commandchaserappend(command_list1,chaser_list)
          command_list=list(set(command_list))
          command_list1=list(set(command_list1))
          print('')
          command=input('>> ').upper()
        else:
          print("You can't go that way.")
          print('')
          command=input('>> ').upper()
      if command=='E' or command=='EAST':
        direction='east'
        n=location_find(location_current,location_list)
        if direction in location_list[n].direction:
          location_current=movecommand(direction,location_current,location_list)
          print('You move {}, to {}.'.format(direction,location_current))
          abc=0
          while abc<len(creature_list):
            creature_list[abc].health=2
            abc+=1
          chaseract(creature_list,location_current,location_list,goose_item)
          map_print(location_current,location_list)
          print('You are now at: {}.'.format(location_current))
          desc(location_current,location_list)
          fleesee=flee_exit(location_current,location_list) 
          if fleesee==2:
            print('The path to freedom is clear. You can FLEE this place.')
          command_list2=[]
          for a in command_list:
            command_list2.append(a)
          command_list1=command_list2
          (command_list1,item_current)=commandappend(command_list1,location_current,location_list)
          totalitem=ti(goose_item,item_current)
          command_list1=commandlookappend(command_list1,totalitem)
          chaser_list=chaserlistcreate(location_current,location_list)
          command_list1=commandchaserappend(command_list1,chaser_list)
          command_list=list(set(command_list))
          command_list1=list(set(command_list1))
          print('')
          command=input('>> ').upper()
        else:
          print("You can't go that way.")
          print('')
          command=input('>> ').upper()
      if command=='W' or command=='WEST':
        direction='west'
        n=location_find(location_current,location_list)
        if direction in location_list[n].direction:
          location_current=movecommand(direction,location_current,location_list)
          print('You move {}, to {}.'.format(direction,location_current))
          abc=0
          while abc<len(creature_list):
            creature_list[abc].health=2
            abc+=1
          chaseract(creature_list,location_current,location_list,goose_item)
          map_print(location_current,location_list)
          print('You are now at: {}.'.format(location_current))
          desc(location_current,location_list)
          fleesee=flee_exit(location_current,location_list) 
          if fleesee==2:
            print('The path to freedom is clear. You can FLEE this place.')
          command_list2=[]
          for a in command_list:
            command_list2.append(a)
          command_list1=command_list2
          (command_list1,item_current)=commandappend(command_list1,location_current,location_list)
          totalitem=ti(goose_item,item_current)
          command_list1=commandlookappend(command_list1,totalitem)
          chaser_list=chaserlistcreate(location_current,location_list)
          command_list1=commandchaserappend(command_list1,chaser_list)
          command_list=list(set(command_list))
          command_list1=list(set(command_list1))   
          print('')
          command=input('>> ').upper()
        else:
          print("You can't go that way.")
          print('')
          command=input('>> ').upper()
      if command=='S' or command=='SOUTH':
        direction='south'
        n=location_find(location_current,location_list)
        if direction in location_list[n].direction:
          location_current=movecommand(direction,location_current,location_list)
          print('You move {}, to {}.'.format(direction,location_current))
          abc=0
          while abc<len(creature_list):
            creature_list[abc].health=2
            abc+=1
          chaseract(creature_list,location_current,location_list,goose_item)
          map_print(location_current,location_list)
          print('You are now at: {}.'.format(location_current))
          desc(location_current,location_list)
          fleesee=flee_exit(location_current,location_list) 
          if fleesee==2:
            print('The path to freedom is clear. You can FLEE this place.')
          command_list2=[]
          for a in command_list:
            command_list2.append(a)
          command_list1=command_list2
          (command_list1,item_current)=commandappend(command_list1,location_current,location_list)
          totalitem=ti(goose_item,item_current)
          command_list1=commandlookappend(command_list1,totalitem)
          chaser_list=chaserlistcreate(location_current,location_list)
          command_list1=commandchaserappend(command_list1,chaser_list)
          command_list=list(set(command_list))
          command_list1=list(set(command_list1))
          print('')
          command=input('>> ').upper()
        else:
          print("You can't go that way.")
          print('')
          command=input('>> ').upper()
      if command=='NW' or command=='NORTHWEST':
        direction='northwest'
        n=location_find(location_current,location_list)
        if direction in location_list[n].direction:
          location_current=movecommand(direction,location_current,location_list)
          print('You move {}, to {}.'.format(direction,location_current))
          abc=0
          while abc<len(creature_list):
            creature_list[abc].health=2
            abc+=1
          chaseract(creature_list,location_current,location_list,goose_item)      
          map_print(location_current,location_list)
          print('You are now at: {}.'.format(location_current))
          desc(location_current,location_list)
          fleesee=flee_exit(location_current,location_list) 
          if fleesee==2:
            print('The path to freedom is clear. You can FLEE this place.')
          command_list2=[]
          for a in command_list:
            command_list2.append(a)
          command_list1=command_list2
          (command_list1,item_current)=commandappend(command_list1,location_current,location_list)
          totalitem=ti(goose_item,item_current)
          command_list1=commandlookappend(command_list1,totalitem)
          chaser_list=chaserlistcreate(location_current,location_list)
          command_list1=commandchaserappend(command_list1,chaser_list)
          command_list=list(set(command_list))
          command_list1=list(set(command_list1))
          print('')
          command=input('>> ').upper()
        else:
          print("You can't go that way.")
          print('')
          command=input('>> ').upper()
      if command=='NE' or command=='NORTHEAST':
        direction='northeast'
        n=location_find(location_current,location_list)
        if direction in location_list[n].direction:
          location_current=movecommand(direction,location_current,location_list)
          print('You move {}, to {}.'.format(direction,location_current))
          abc=0
          while abc<len(creature_list):
            creature_list[abc].health=2
            abc+=1
          chaseract(creature_list,location_current,location_list,goose_item)
          map_print(location_current,location_list)
          print('You are now at: {}.'.format(location_current))
          desc(location_current,location_list)
          fleesee=flee_exit(location_current,location_list) 
          if fleesee==2:
            print('The path to freedom is clear. You can FLEE this place.')
          command_list2=[]
          for a in command_list:
            command_list2.append(a)
          command_list1=command_list2
          (command_list1,item_current)=commandappend(command_list1,location_current,location_list)
          totalitem=ti(goose_item,item_current)
          command_list1=commandlookappend(command_list1,totalitem)
          chaser_list=chaserlistcreate(location_current,location_list)
          command_list1=commandchaserappend(command_list1,chaser_list)
          command_list=list(set(command_list))
          command_list1=list(set(command_list1))
          print('')
          command=input('>> ').upper()
        else:
          print("You can't go that way.")
          print('')
          command=input('>> ').upper()
      if command=='SE' or command=='SOUTHEAST':
        direction='southeast'
        n=location_find(location_current,location_list)
        if direction in location_list[n].direction:
          location_current=movecommand(direction,location_current,location_list)
          print('You move {}, to {}.'.format(direction,location_current))
          abc=0
          while abc<len(creature_list):
            creature_list[abc].health=2
            abc+=1
          chaseract(creature_list,location_current,location_list,goose_item)
          map_print(location_current,location_list)
          print('You are now at: {}.'.format(location_current))
          desc(location_current,location_list)
          fleesee=flee_exit(location_current,location_list) 
          if fleesee==2:
            print('The path to freedom is clear. You can FLEE this place.')
          command_list2=[]
          for a in command_list:
            command_list2.append(a)
          command_list1=command_list2
          (command_list1,item_current)=commandappend(command_list1,location_current,location_list)
          totalitem=ti(goose_item,item_current)
          command_list1=commandlookappend(command_list1,totalitem)
          chaser_list=chaserlistcreate(location_current,location_list)
          command_list1=commandchaserappend(command_list1,chaser_list)
          command_list=list(set(command_list))
          command_list1=list(set(command_list1))
          print('')
          command=input('>> ').upper()
        else:
          print("You can't go that way.")
          print('')
          command=input('>> ').upper()
      if command=='SW' or command=='SOUTHWEST':
        direction='southwest'
        n=location_find(location_current,location_list)
        if direction in location_list[n].direction:
          location_current=movecommand(direction,location_current,location_list)
          print('You move {}, to {}.'.format(direction,location_current))
          abc=0
          while abc<len(creature_list):
            creature_list[abc].health=2
            abc+=1
          chaseract(creature_list,location_current,location_list,goose_item)
          map_print(location_current,location_list)
          print('You are now at: {}.'.format(location_current))
          desc(location_current,location_list)
          fleesee=flee_exit(location_current,location_list) 
          if fleesee==2:
            print('The path to freedom is clear. You can FLEE this place.')
          command_list2=[]
          for a in command_list:
            command_list2.append(a)
          command_list1=command_list2
          (command_list1,item_current)=commandappend(command_list1,location_current,location_list)
          totalitem=ti(goose_item,item_current)
          command_list1=commandlookappend(command_list1,totalitem)
          chaser_list=chaserlistcreate(location_current,location_list)
          command_list1=commandchaserappend(command_list1,chaser_list)
          command_list=list(set(command_list))
          command_list1=list(set(command_list1))
          print('')
          command=input('>> ').upper()
        else:
          print("You can't go that way.")
          print('')
          command=input('>> ').upper()
      if command=='LOOK HERE':
        n=location_find(location_current,location_list)
        i=0
        if len(location_list[n].item)==0:
          print('There is nothing here.')
        while i<len(location_list[n].item):
          c=maintainlength(location_list[n].item[i].short_name,location_list[n].item[i].item_name)
          print(c)
          i+=1
        print('')
        command=input('>> ').upper()
      for itemcurrent in  item_current:
        if command=='TAKE {}'.format(itemcurrent):
          n=location_find(location_current,location_list)
          i=0
          a=itemcurrent.lower()
          while i<len(location_list[n].item):
            if location_list[n].item[i].short_name==a:
              break
            else:
              i+=1
          print('You pick up the {}.'.format(location_list[n].item[i].item_name))
          goose_item.append(itemcurrent.lower())
          chaseract(creature_list,location_current,location_list,goose_item)
          location_list[n].item.remove(location_list[n].item[i])
          
          command_list1.remove('TAKE {}'.format(itemcurrent.upper()))
          command_list=commanddropappend(command_list,goose_item)
          command_list1=commanddropappend(command_list1,goose_item)
          chaser_list=chaserlistcreate(location_current,location_list)
          command_list1=commandchaserappend(command_list1,chaser_list)
          command_list=list(set(command_list))
          command_list1=list(set(command_list1))
          print('')
          command=input('>> ').upper()
      for itemcandrop in goose_item:
        if command=='DROP {}'.format(itemcandrop.upper()):
          n=0
          while n<len(item_list):
            if itemcandrop==item_list[n].short_name:
              break
            else:
              n+=1
          print('You drop the {}.'.format(item_list[n].item_name))
          goose_item.remove(itemcandrop)
          chaseract(creature_list,location_current,location_list,goose_item)
          
          i=location_find(location_current,location_list)
          location_list[i].item.append(item_list[n])
          command_list.remove('DROP {}'.format(itemcandrop.upper()))
          command_list1.remove('DROP {}'.format(itemcandrop.upper()))
          command_list1.append('TAKE {}'.format(itemcandrop.upper()))
          chaser_list=chaserlistcreate(location_current,location_list)
          command_list1=commandchaserappend(command_list1,chaser_list)
          command_list=list(set(command_list))
          command_list1=list(set(command_list1))
          print('')
          command=input('>> ').upper()
      
      for itemlook in totalitem:
        if command=='LOOK {}'.format(itemlook.upper()):
          n=0
          while n<len(item_list):
            if itemlook==item_list[n].short_name:
              break
            else:
              n+=1
          print("{} - Terror Rating: {}".format(item_list[n].item_name,item_list[n].terror_rating))
          print('')
          command=input('>> ').upper()
      for chaser in chaser_list:
        if command=='LOOK {}'.format(chaser.name.upper()):
          rate=int(gooserate(goose_item))
          if rate>=int(chaser.terror_rating)+5:
            print('{} looks a little on-edge around you.'.format(chaser.name))
          elif int(chaser.terror_rating)>=rate+5:
            print("{} doesn't seem very afraid of you.".format(chaser.name))          
          else:
            print('Hmm. {} is a bit hard to read.'.format(chaser.name))  
          print('')
          command=input('>> ').upper()
      if command=='FLEE':
        if fleesee==1:
          print("There's nowhere you can run or hide! Find somewhere else to FLEE.")
        if fleesee==2:
          print("You slip past the dastardly Goosechasers and run off into the wilderness! Freedom at last!")
          print('========= F R E E D O M =========')
          sys.exit()
        print('')
        command=input('>> ').upper()
      if command=='HONK' or command=='Y':
        n=location_find(location_current,location_list)
        if location_list[n].creature==[]:
          print('All shall quiver before the might of the goose! HONK!')
        else:
          print('You sneak up behind your quarry and honk with all the force of a really angry airhorn! HONK!')
          rate=gooserate(goose_item)
          llist=[]
          for aaa in location_list[n].creature:
            llist.append(aaa)
          for chaser in llist:
            i=chaserfind(chaser,creature_list)
            if rate>int(chaser.terror_rating):
              print('{} is spooked! They flee immediately!'.format(chaser.name))           
              location_list[n].creature.remove(creature_list[i])
              creature_list.remove(creature_list[i])
              if len(creature_list)==0:
                print('')
                print('None can stand against the power of the goose!')
                print('========= V I C T O R Y =========')
                sys.exit()
            else:
              print('{} is not spooked :('.format(chaser.name))
        chaseract(creature_list,location_current,location_list,goose_item)
        chaser_list=chaserlistcreate(location_current,location_list)
        command_list1=commandchaserappend(command_list1,chaser_list)
        print('')
        command=input('>> ').upper()
      if command=='WAIT':
        print('You lie in wait.')
        chaseract(creature_list,location_current,location_list,goose_item)
        chaser_list=chaserlistcreate(location_current,location_list)
        command_list1=commandchaserappend(command_list1,chaser_list)
        print('')
        command=input('>> ').upper()
        
        
        
print('Game terminated.')
