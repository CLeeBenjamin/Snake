import pygame 
from pygame.locals import *

# Add snake body next 

pygame.init()

#create blank game window 
screen_width = 400 
screen_height = 400 

#gamewindow 
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Snake')

#setup loop with exit event handler 
run = True 

#colors 
bg = (255, 200,150)

def draw_screen():
  screen.fill(bg)

while run: 

  draw_screen()
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      run = False

  pygame.display.update()


pygame.quit()

