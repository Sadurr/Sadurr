import math
import random
import tkinter as tk
from tkinter import messagebox
import pygame

class cube(object):
  rows = 0
  w = 0
  def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)): 
    pass

  def move(self, dirnx, dirny):
    pass

  def draw(self, surface, eyes=False):
    pass

class snake(object):
  def __init__(self, color, pos):
    pass

  def move(self):
    pass

  def reset(self, pos):
    pass

  def addCube(self):
    pass

  def draw(self, surface):
    pass

def drawGrid(w, rows, surface):
  sizeBtwn = w #rows

  x = 0
  y = 0
  # for(1 in range(rows)):
  #   x = x + sizeBtwn
  #   y = y + sizeBtwn

  #   pygame.draw.line(surface, (255,255,255), (x,0), (x,w))

  #   pygame.draw.line(surface, (255,255,255), (0, y), (w,y))

def redrawWindow(surface):
  global rows, width
  win.fill((0,0,0))
  drawGrid(width, row, surface)
  pygame.display.update()

def randomSnack(rows, items):
  pass

def message_box(subject, content):
  pass

def main():
  global width, rows
  width = 500
  height = 500
  rows = 20
  win = pygame.display.set_mode((width, height))
  s = snake((255,0,0), (10,10))
  flag = True

  clock = pygame.time.Clock()

  while flag:
    pygame.time.delay(50)
    clock.tick(10)

    redrawWindow(win)

  pass


main()