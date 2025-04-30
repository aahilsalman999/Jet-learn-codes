import pgzrun , random
width = 900
height  = 600
player = Actor("player")
player.pos = width //2 , height - 60
speed = 3
speed_p = 10
enemies = []
bullets = []
score = 0

for x in range(8):
  for y in range(1):
   enemies.append(Actor("trophy"))
   enemies[-1].x = 100 + 80 * x
   enemies[-1].y = 80 + 50 * y
   
direction = 1
player.dead = False
player.countdown = 90

def game_over():
  screen.draw.text("Game Over!" , (width // 2 , height // 2))

def display_score():
  screen.draw.text(str(score) , (50,30))

def on_key_down(key):
  if player.dead == False:
    if key == keys.SPACE:
      bullets.append(Actor("football"))
      sounds.football_kick.play()
      bullets[-1].x = player.x
      bullets[-1].y = player.y - 50

def update():
  global score , direction ,player              
  move_down = False
  if keyboard.left:
    player.x -= speed_p
    if player.x <= 0:
      player.x = 0
  elif keyboard.right:
    player.x += speed_p
    if player.x >= width:
      player.x = width
  
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
          score = score + 100
          bullets.remove(bullet)
          enemies.remove(enemy)
          if len(enemies) == 0:
            game_over()
      if enemy.colliderect(player):
        player.dead = True
        player.y += 200
        player = None
  if player.dead:
    player.countdown -= 1       
  if player.countdown == 0:
    player.dead = False
    player.countdown = 90

          #Creating new bugs
          #new_bug = Actor("bug")
          #new_bug.x = random.randint(50 , width - 50)
          #new_bug.y = random.randint(-100 , 0 )
          #enemies.append(new_bug)

def draw():
  screen.clear()
  screen.fill("Dark green")
  for bullet in bullets:
    bullet.draw()
  for enemy in enemies:
    enemy.draw()
  if player.dead == False:
    player.draw()
    display_score()
  if len(enemies) == 0:
    game_over()
pgzrun.go()





      


