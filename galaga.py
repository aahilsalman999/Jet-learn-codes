import pgzrun , random
width = 800
height  = 600
bug = Actor("bug")
ship = Actor("ship")
ship.pos = width //2 , height - 60
speed = 5
speed_s = 10
enemies = []
bullets = []
enemies.append(bug)
enemies[-1].x = 20
enemies[-1].y = -100
score = 0

def display_score():
  screen.draw.text(str(score) , (50,30))

def update():
  if keyboard.left:
    ship.x -= speed_s
  if ship.x <= 0:
    ship.x = 0
  if keyboard.right:
    ship.x += speed_s
  if ship.x >= width:
    ship.x = width
  
  for bullet in bullets:
    if bullet.y <= 0:
      bullets.remove(bullet)
    else:
      bullet.y -= 10
      


