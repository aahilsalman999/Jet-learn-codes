import pgzrun
import random
width = 600
height = 600
title = "Good Shot"
message =  ""
alien = Actor("alien")
def draw():
  screen.clear()
  screen.fill(color = "blue")
  alien.draw()
  screen.draw.text(message , center = (400 , 10) , fontsize = 30)

def place_alien():
  alien.x = random.randint(50 , width - 50)
  alien.y = random.randint(50 , width - 50)

def on_mouse_down(pos):
   global message
   if alien.collidepoint(pos):
     message = "Good Shot"
     place_alien()
   else:
     message = "You missed"
     place_alien()
pgzrun.go()
