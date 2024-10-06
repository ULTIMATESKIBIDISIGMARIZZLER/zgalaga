import pgzrun
import random
#W and H
WIDTH=1200
HEIGHT=600
#colors
White=(255,255,255)
Blue=(0,0,255)

# the sprites
ship=Actor("ship")
bug=Actor("bug")
ship.pos=(WIDTH//2,HEIGHT-60)
speed=5

#define a list of bullets and enemies
bullets=[]
enemies=[]

#we want enemies in 8 by 4
for i in range(8):
    for j in range(4):
        enemies.append(Actor("bug"))
        #enemies have to be in a straight line
        enemies[-1].x=100+50*i
        enemies[-1].x=80+50*j

score=0
direction=1
ship.dead=False
ship.countdown=90
def displayScore():
    screen.draw.text(str(score),(50,30))

def game_over():
    screen.draw.text("Game over", (250,300)
                     )

def on_key_down(key):
    if ship.dead==False:
        if key== keys.SPACE:
            bullets.append(Actor("bullet"))
            bullets[-1].x=ship.x
            bullets[-1].y=ship.y-50

def update():
    global score
    global direction
    moveDown=False
    if ship.dead==False:
        if keyboard.left:
            ship.x-=speed
            if ship.x<=0:
                ship.x=0

        elif keyboard.right:
            ship.x+=speed
            if ship.x>=WIDTH:
                ship.x=WIDTH
        
    
    for bullet in bullets:
        if bullet.y<=0:
            bullets.remove(bullet)
        else:
            bullet.y-=10

    if len(enemies)==0:
        game_over()

    if len(enemies)>0 and (enemies[-1].x> WIDTH-80 or enemies[0].x<80):
        moveDown=True
        direction=direction*-1

    for enemy in enemies:
        enemy.x+=5*direction
        if moveDown==True:
            enemy.y+=100
        if enemy.y> HEIGHT:
            enemies.remove(enemy)

        for bullet in bullets:
            if enemy.colliderect(bullet):
               score+=100
               bullets.remove(bullet)
               enemies.remove(enemy)
               if len(enemies)==0:
                  game_over
  
        if enemy.colliderect(ship):
           ship.dead=True
    
    if ship.dead:
       ship.countdown-=1
    if ship.countdown==0:
       ship.dead=False
       ship.countdown=90

def draw():
    screen.clear()
    screen.fill(Blue)
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    if ship.dead==False:
        ship.draw()
    displayScore()
    if len(enemies)==0:
        game_over

pgzrun.go()