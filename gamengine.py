from math import *
from ion import *
from kandinsky import *
from time import *


deltay=0
grav=2
x=46
y=46
game = True
i=0

# prend des lvls de x*7 (x,y)

def print_screen(lvl,dec=0):
  # lvl : [[x],[x],[x],[x],[x],[x],[x]]
  for y in range(len(lvl)):
    for x in range(len(lvl[y])-dec):
      test=lvl[y][x+dec]
      if test=="X":
        fill_rect(x*32,y*32,32,32,'black')
      elif test=="O" or test=="J":
        fill_rect(x*32,y*32,32,32,'white')
      elif test=="P":
        fill_rect(x*32,y*32,32,32,'green')
      elif test=="L":
        fill_rect(x*32,y*32,32,32,'red')



level=[
["X","O","O","O","O","O","O","O","O","O","O","O","O","O","X"],
["X","O","O","O","O","O","O","O","O","O","O","O","O","O","X"],
["X","O","O","O","O","O","O","O","O","O","O","O","O","P","X"],
["X","O","O","O","O","O","O","O","O","O","O","X","L","X","X"],
["X","X","X","X","O","O","X","O","X","O","O","O","L","O","X"],
["X","O","O","O","O","O","O","O","O","O","O","O","L","O","X"],
["X","L","L","L","L","L","L","L","L","L","L","L","L","L","X"]]      
  
def hit(x1,y1,lvl):
  global i
  global game
  for y in range(len(lvl)):
    for x in range(len(lvl[y])-int(i)):
      test=lvl[y][x+int(i)]          
      if (x*32)-8<=x1<=(x+1)*32 and (y*32)-8<y1<(y+1)*32 and 0<x1<len(lvl[y])*32:
        if test=="X":
          return True
        if test=="P":
          game=False
          draw_string("Victoire",120,100)
        if test=="L":
          game=False
          draw_string("Defaite",120,100)
          
                   
  return False     
def player():
  global x
  global y
  global level
  global deltay
  if keydown(KEY_RIGHT) and x<=(len(level[0])*32):
    move(1)
  elif keydown(KEY_LEFT) and 32<x:
    move(-1)
  if keydown(KEY_UP) and hit(x,y,level):
    deltay=14
  if not hit(x,y,level):
    move("g")
  if not deltay==0:
    move("deltay")
    
  sleep(0.02)  
  
def move(input):
  global x
  global deltay
  global grav
  global y
  if input=="deltay":
    fill_rect(x,y,8,8,"white")
    y-=deltay
    fill_rect(x,y,8,8,"blue")
    deltay-=1
    
  elif type(input)== int:
    fill_rect(x,y,8,8,"white")
    x+=input
    fill_rect(x,y,8,8,"blue")
    
  elif input=="g":
    fill_rect(x,y,8,8,"white")
    y+=grav
    fill_rect(x,y,8,8,"blue")
    
      
      

#fill_rect(x,y,8,8,"blue")
print_screen(level,int(i))
while game:    
  if keydown(KEY_LEFT) and i>0:
   i-=0.04
   print_screen(level,int(i)) 
  elif keydown(KEY_RIGHT):
    i+=0.04
    print_screen(level,int(i))
  player()
