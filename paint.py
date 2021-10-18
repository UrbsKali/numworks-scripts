from kandinsky import *
from ion import * 
from time import sleep

x_cursor = 100
y_cursor = 100
x_max = 320
y_max = 220
draw = False
speed = 0.01
old_color = ['white','white','white','white']
fill_rect(0,0,400,400, 'white')
 
  
def draw_cursor(x, y, color='red'):
  old_color[0] = get_pixel(x+5, y)
  old_color[1] = get_pixel(x-5, y)
  old_color[2] = get_pixel(x, y+5)
  old_color[3] = get_pixel(x, y-5)
  if color == 'white':
    if old_color[0] == (248,0,0) : set_pixel(x+5, y, color)
    if old_color[1] == (248,0,0) :set_pixel(x-5, y, color)
    if old_color[2] == (248,0,0):set_pixel(x, y+5, color)
    if old_color[3] == (248,0,0) :set_pixel(x, y-5, color)

  else:
    if old_color[0] == (248,252,248) : set_pixel(x+5, y, color)
    if old_color[1] == (248,252,248) :set_pixel(x-5, y, color)
    if old_color[2] == (248,252,248):set_pixel(x, y+5, color)
    if old_color[3] == (248,252,248) :set_pixel(x, y-5, color)

  

while True:
  draw_cursor(x_cursor, y_cursor)

  if keydown(KEY_PLUS):
    speed += 0.01
  elif keydown(KEY_MINUS):
    speed -= 0.01
  if keydown(KEY_UP) and y_cursor > 0:
    draw_cursor(x_cursor, y_cursor, 'white')
    y_cursor -= 1
  elif keydown(KEY_DOWN) and y_cursor < y_max:
    draw_cursor(x_cursor, y_cursor, 'white')
    y_cursor += 1
  elif keydown(KEY_LEFT) and x_cursor > 0:
    draw_cursor(x_cursor, y_cursor, 'white')
    x_cursor -= 1
  elif keydown(KEY_RIGHT) and x_cursor < x_max:
    draw_cursor(x_cursor, y_cursor, 'white')
    x_cursor += 1
  if keydown(KEY_OK):
    draw = True
    set_pixel(x_cursor, y_cursor, 'black')
  else:
    draw = False
  if keydown(KEY_BACKSPACE):
    fill_rect(0,0,400,400, 'white')
  sleep(speed)
