import pgzrun , random
width = 900
height  = 600
ship = Actor("ship1")
ship.pos = width //2 , height - 60
speed = 3
speed_s = 10
enemies = []
bullets = []
score = 0

for x in range(8):
  for y in range(4):
   enemies.append(Actor("bug"))
   enemies[-1].x = 100 + 80 * x
   enemies[-1].y = 80 + 50 * y
   
direction = 1
ship.dead = False
ship.countdown = 90

def game_over():
  screen.draw.text("Game Over!" , (width // 2 , height // 2))

def display_score():
  screen.draw.text(str(score) , (50,30))

def on_key_down(key):
  if ship.dead == False:
    if key == keys.SPACE:
      bullets.append(Actor("bullet"))
      sounds.bullet_release.play()
      bullets[-1].x = ship.x
      bullets[-1].y = ship.y - 50

def update():
  global score , direction              
  move_down = False
  if keyboard.left:
    ship.x -= speed_s
    if ship.x <= 0:
      ship.x = 0
  elif keyboard.right:
    ship.x += speed_s
    if ship.x >= width:
      ship.x = width
  
  for bullet in bullets:
    if bullet.y <= 0:
      bullets.remove(bullet)
    else:
      bullet.y -= 10
  if len(enemies) == 0:
    game_over()
  
  if len(enemies) > 0 and (enemies[-1].x > width - 80 or enemies[-1].x < 80):
    move_down = True
    direction = direction * -1

  for enemy in enemies:
      enemy.x += 5 * direction
      if move_down == True:
        enemy.y += 50
      if enemy.y > height:
        enemies.remove(enemy)
      for bullet in bullets:
        if enemy.colliderect(bullet):
          sounds.bullet_hit.play()
          score = score + 100
          bullets.remove(bullet)
          enemies.remove(enemy)
          if len(enemies) == 0:
            game_over()
      if enemy.colliderect(ship):
        ship.dead = True
        ship.y += 200
        ship = None
  if ship.dead:
    ship.countdown -= 1       
  if ship.countdown == 0:
    ship.dead = False
    ship.countdown = 90

          #Creating new bugs
          #new_bug = Actor("bug")
          #new_bug.x = random.randint(50 , width - 50)
          #new_bug.y = random.randint(-100 , 0 )
          #enemies.append(new_bug)

def draw():
  screen.clear()
  screen.blit("space" , (0,0))
  for bullet in bullets:
    bullet.draw()
  for enemy in enemies:
    enemy.draw()
  if ship.dead == False:
    ship.draw()
  display_score()
  if len(enemies) == 0:
    game_over()
pgzrun.go()





      


