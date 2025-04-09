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

def on_key_down(key):
  if key == keys.SPACE:
     bullets.append(Actor("bullet"))
     bullets[-1].x = ship.x
     bullets[-1].y = ship.y - 50

def update():
  global score
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
  for enemy in enemies:
      enemy.y += 5
      if enemy.y >= height:
        enemy.y = -100
        enemy.x = random.randint(50 , width - 50)
      
      for bullet in bullets:
        if enemy.colliderect(bullet):
          score = score + 100
          bullets.remove(bullet)
          enemies.remove(enemy)

          #Creating new bugs
          new_bug = Actor("bug")
          new_bug.x = random.randint(50 , width - 50)
          new_bug.y = random.randint(-100 , 0 )
          enemies.append(new_bug)

def draw():
  screen.clear()
  screen.blit("space" , (0,0))
  for bullet in bullets:
    bullet.draw()
  for enemy in enemies:
    enemy.draw()
  ship.draw()
  display_score()
pgzrun.go()





      


