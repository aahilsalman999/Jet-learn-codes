import pgzrun
import random
width = 500
height = 500
title = "Catch the bus!"
message = ""
bus = Actor("bus")
def draw():
  screen.clear()
  screen.fill(color = "light blue")
  bus.draw()
  screen.draw.text(message , center = (400 , 30) , fontsize = 50 , color = "black")

def place_bus():
  bus.x = random.randint(50 , width - 50)
  bus.y = random.randint(50 , width - 50)

def on_mouse_down(pos):
   global message
   if bus.collidepoint(pos):
     message = "You got the bus!"
     place_bus()
   else:
     message = "You missed the bus!"
     place_bus()
pgzrun.go()
