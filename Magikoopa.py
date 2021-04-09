import pygame

class Magikoopa:

  def __init__(self):

    self.__imgbackground = pygame.image.load('images/game-background.png')
    self.__surface = pygame.display.set_mode((self.__imgbackground.get_width(), self.__imgbackground.get_height()))

    self.__imgEast = pygame.image.load('images/koopaEast.png')
    self.__imgWest = pygame.image.load('images/koopaWest.png')
    self.__imgDeadEast = pygame.image.load('images/deadEast.png')
    self.__imgDeadWest = pygame.image.load('images/deadWest.png')

    self.__width = self.__imgEast.get_width()
    self.__height = self.__imgEast.get_height()

    self.__xpos = 0
    self.__ypos = (self.__imgbackground.get_height() / 2) - (self.__height / 2)

    self.__direction = 'east'
    self.__dead = False
  
  def get_bounds(self): 
    pygame.draw.rect(self.__xpos, self.__ypos, self.__width, self.__height)

  def get_img(self): 
    if self.__direction == 'east':
      return self.__imgEast
    if self.__direction == 'west':
      return self.__imgWest
    
  def get_height(self): 
    return self.__height

  def get_width(self): 
    return self.__width

  def getX(self): 
    return self.__xpos

  def getY(self): 
    return self.__ypos

  def move_up(self, y): 
    self.__ypos -= y

  def move_down(self, y): 
    self.__ypos += y

  def move_left(self, x):
    self.__xpos -= x
    self.__direction = 'west'

  def move_right(self, x): 
    self.__xpos += x
    self.__direction = 'east'

  def is_dead(self, dead): 
    if dead == True:

      if self.__direction == 'west':
        surface.blit(self.__imgDeadWest, (self.__xpos, self.__ypos))

      if self.__direction == 'east':
        surface.blit(self.__imgDeadEast, (self.__xpos, self.__ypos))
  '''
  def reset(self, x = 0, y = (self.__imgbackground.get_height() / 2) - (self.__height / 2)): 
    if self.__ypos == 400:
      dead = False
      self.__xpos = x
      self.__ypos = y
  '''
  def setX(self, x): 
    self.__xpos = x

  def setY(self, y): 
    self.__ypos = y

  def border(self):
    #this is for the right wall
    if self.__xpos + self.__width >  self.__imgbackground.get_width():
      self.__xpos = 570 
    
    #this is for the left wall
    if self.__xpos + self.__width <= 80:
      self.__xpos = -10
    
    #this is for the roof
    if self.__ypos + self.__height <= 100:
      self.__ypos = 50   

    #this is for the floor 
    if self.__ypos + self.__height >= 450:
      self.__ypos = 400
      dead = True 
          
        