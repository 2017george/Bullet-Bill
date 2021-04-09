import pygame

class Magikoopa:
  #thses are the varibles that are used in class  
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

  #this is the hit box for the koppa 
  def get_bounds(self): 
    return pygame.Rect(self.__xpos, self.__ypos, self.__width, self.__height)

  #this gets the right picture depending on which way you are facing 
  def get_img(self): 
    if self.__direction == 'east':
      return self.__imgEast
      
    if self.__direction == 'west':
      return self.__imgWest
      
  #this gets the height of koppa
  def get_height(self): 
    return self.__height
  
  #this gets the width of the koppa 
  def get_width(self): 
    return self.__width
  
  #this gets the x postion of the koppa 
  def getX(self): 
    return self.__xpos
  #this gets the y postion of the koppa
  def getY(self): 
    return self.__ypos
    
  #this makes sure you move up when the up key is pressed. 
  def move_up(self, y): 
    self.__ypos -= y
    
  #this makes sure you move down when the down key is pressed. 
  def move_down(self, y): 
    self.__ypos += y
    
  #this makes sure you move left when the left key is pressed.
  def move_left(self, x):
    self.__xpos -= x
    self.__direction = 'west'
  
  #this makes sure you move right when the right key is pressed.
  def move_right(self, x): 
    self.__xpos += x
    self.__direction = 'east'
  
  #this changes the picture of the koppa to the dead verison 
  def dead(self, dead): 
    if dead == True:
      if self.__direction == 'west':
        return self.__imgDeadWest

      if self.__direction == 'east':
        return self.__imgDeadEast
  
  #reset the koopa back to where he started when he losses a life
  
  def reset(self, x = 0, y = 220.5): 
      self.__xpos = x
      self.__ypos = y

  #this sets the x postion 
  def setX(self, x): 
    self.__xpos = x
    
  #this sets the y position 
  def setY(self, y): 
    self.__ypos = y

  #this overall sets the border for the game 
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
          
        