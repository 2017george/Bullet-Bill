import pygame
import random

class Bullet_Bill:
#these are all the varibles we use in this class
  def __init__(self):
    self.__imgbackground = pygame.image.load('images/game-background.png')
    self.__surface = pygame.display.set_mode((self.__imgbackground.get_width(), self.__imgbackground.get_height()))

    self.__imgBullet = pygame.image.load('images/bulletWest.png')

    self.__width = self.__imgBullet.get_width()
    self.__height = self.__imgBullet.get_height()

    self.__xpos = random.randint(580, 3600)
    self.__ypos = random.randint(100, 397)

  #this is used for the hit of the Bullet Bill.
  def get_bounds(self):
    return pygame.Rect(self.__xpos-10, self.__ypos+10, self.__imgBullet.get_width()+10,self.__imgBullet.get_height()-10)

  #this gets the image of the bullet bill
  def get_img(self):
    return self.__imgBullet

  #this gets the height of the bullet bill
  def get_height(self):
    return self.__height

  #this gets the width of the Bullet Bill
  def get_width(self):
    return self.__width

  #This gets the x coordinate of the bullet bill
  def getX(self):
    return self.__xpos

  #This gets the y coordinate of the bullet bill
  def getY(self):
    return self.__ypos

  #This move the bullet bill on the x-aixs
  def move(self, x = 5):
    self.__xpos -= x

  #this randomize the position of the bullet bill
  def position(self):
    self.__ypos = random.randint(100, 397)
    self.__xpos = random.randint(580, 3600)

  #this sets the x coordinate of the bullet bill
  def setX(self, x):
    self.__xpos = x

  #this sets the y coordinate of the bullet bill
  def setY(self, y):
    self.__ypos = y
