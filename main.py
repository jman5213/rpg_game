print('''
Explorer Game
V2.0
Created By:
Jman5213
--------------
Instructions:
Type: 
Open Moves
A compass is in
the top left corner.
Use it to find 
your way.''')

places {
  'house':{
    'hall':{
      'north':{
        'wall':'none'
      },
      'south':{
        'south':'kitchen',
        'wall':'door'
      },
      'east':{
        'east':'dining room',
        'wall':'door'
      },
      'west':{
        'west':'stairwell',
        'wall':'stairwell'
      }
    },
    'dining room':{
      'north':{
        'wall':'none'
      },
      'south':{
        'south':'garden',
        'wall':'door'
      },
      'east':{
        'wall':'none'
      },
      'west':{
        'west':'hall',
        'wall':'door'
      }
  }
}

direction = 1
playerlife = 1
inventory = []
using = nothing
firstline = N
secondline = woe
lastline = s
do = input()
currentplace == house
currentroom == hall

def drawcompass():
  if direction ==1:
    firstline == N 
    secondline == woe
    lastline == s 
  elif direction == 2:
    firstline == n 
    secondline == woE 
    lastline == s 
  elif direction == 3:
    firstline == n 
    secondline == woe
    lastline == S 
  elif direction == 4:
    firstline == n 
    secondline == Woe 
    lastline == s 
  elif direction >= 5:
    print('error w/ changedirection() func. Direction >= 5.')
def changedirection():
  if do == 'go left':
    if direction == 4:
      direction == 1
    elif direction <= 3:
      direction += 1
    drawcompass()
  elif do == 'go right':
    if direction == 1:
      direction == 4
    elif direction >= 2:
      direction -= 1
    drawcompass()
  elif do == 'go forward':
    if places[currentplace[currentroom[direction[direction]]]] != places[]:
      currentroom == places[currentplace[currentroom[direction[direction]]]]
    elif places[currentplace[currentroom[direction[direction]]]] != places[]:
      currentplace == places[currentplace[currentroom[direction[direction]]]]
  elif do == 'go up' and currentroom == places[currentplace[currentroom[direction[direction]]]] == stairs or do == 'go up' and currentroom == places[currentplace[currentroom[direction[direction]]]] == stairwell:
    if places[currentplace[currentroom[direction[direction]]]] != places[]:
      currentroom == places[currentplace[currentroom[direction[direction]]]]
    elif places[currentplace[currentroom[direction[direction]]]] != places[]:
      currentplace == places[currentplace[currentroom[direction[direction]]]]
def drawinventory():
  if do == 'open inventory':
    print('''
         A       B      C      D
        key    sword  posion  food
        ''')
      if do == 'A':
        if key in inventory:
          print('Key being used!')
          using == 'key'
        else:
          print('You don\'t have that!')
      if do == 'B':
        if key in inventory:
          print('Sword being used!')
          using == 'sword'
        else:
          print('You don\'t have that!')   
      if do == 'c':
        if key in inventory:
          print('posion being used!')
          using == 'posion'
        else:
          print('You don\'t have that!')
      if do == 'D':
        if key in inventory:
          print('food being used!')
          using == 'food'
        else:
          print('You don\'t have that!')