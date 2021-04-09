import pygame
import random

class Bullet_Bill:

  def __init__(self):
    self.__imgbackground = pygame.image.load('images/game-background.png')
    self.__surface = pygame.display.set_mode((self.__imgbackground.get_width(), self.__imgbackground.get_height()))

    self.__imgBullet = pygame.image.load('images/bulletWest.png')

    self.__width = self.__imgBullet.get_width()
    self.__height = self.__imgBullet.get_height()

    self.__xpos = -10
    self.__ypos = 200

  def get_bounds(self):
    pygame.draw.rect(self.__xpos, self.__ypos, self.__imgBullet.get_width(),self.__imgBullet.get_height())

  def get_img(self): 
    return self.__imgBullet

  def get_height(self):
    return self.__height

  def get_width(self):
    return self.__width

  def getX(self):
    return self.__xpos

  def getY(self):
    return self.__ypos

  def move(self, x = 5): 
    self.__xpos -= x

  def position(self):
    self.__ypos = random.randint(100, 450)
    self.__xpos = random.randint(580, 800)

  def setX(self, x): 
    self.__xpos = x

  def setY(self, y): 
    self.__ypos = y


