import pgzrun
import random
Width = 300
Height = 300
def draw():
  r = 255
  g = 0 
  b = random.randint(120,255)
  width = Width
  height = Height - 200 
  for i in range(20):
    rect = Rect((0 , 0),(width , height))
    rect.center = 150,150
    screen.draw.rect(rect,(r,g,b))
    r -= 10
    g += 10
    width -= 10
    height += 10
pgzrun.go()