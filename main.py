import pygame as pg
import random, time 

width = 800
height = 600
bx = width//2
by = height//2
b_r = 5
b_spdx = 6
b_spdy = 8

def draw_ball():
  pg.draw.circle(screen, (255,255,255), (bx, by), b_r) 

def calc_ball():
  global bx, by, b_spdx, b_spdy
  bx += b_spdx
  by += b_spdy

  if bx > width or bx < 0:
    b_spdx *= -1
  if by > height or by < 0:
    b_spdy *= -1 

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
