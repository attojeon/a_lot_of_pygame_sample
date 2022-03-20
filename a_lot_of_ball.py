import pygame as pg
import random, time 

width = 800
height = 600
bx = width//2
by = height//2
b_r = 5
b_spdx = 6
b_spdy = 8
balls = []

def add_ball():
  x = random.randint(0, width)
  y = random.randint(0, height)
  br = random.randint(2, 10)
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  balls.append( [x,y, b_spdx, b_spdy, br, (r,g,b)] )

def draw_ball():
  for b in balls:
    pg.draw.circle(screen, b[5], (b[0], b[1]), b[4]) 

def calc_ball():
  global bx, by, b_spdx, b_spdy

  for b in balls:
    b[0] += b[2]
    b[1] += b[3] 
    if b[0]> width or b[0]<0:
      b[2] *= -1
    if b[1]> height or b[1]<0:
      b[3] *= -1

pg.init()
screen = pg.display.set_mode( (width, height))

running = True
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_q:
        running = False
      elif event.key == pg.K_SPACE:
        add_ball()
      elif event.key == pg.K_0:
        balls.clear()
      elif event.key == pg.K_5:
        for _ in range(5):
          add_ball()

  # draw bg
  screen.fill( (125, 125, 125))

  # draw objects 
  draw_ball()

  # calc objects
  calc_ball()

  # update display 
  pg.display.update()
  
  time.sleep(0.01)

pg.quit()
