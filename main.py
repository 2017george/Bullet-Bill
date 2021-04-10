import pygame, os
from tkinter import Tk, messagebox
from BulletBill import Bullet_Bill
from Magikoopa import Magikoopa
from pygame.locals import *

#this both add's and take the messagebox window away
root = Tk()
root.withdraw()

#this varbile is for the score and makes the start game false
startgame = False
score = 0

#these will load in the sound effects and the sound
# pygame.mixer.init()
# death_sound = pygame.mixer.Sound("death.mp3")
# point_sound = pygame.mixer.Sound("Score.mp3")
# pygame.mixer.music.load("Music.mp3")

os.environ['SDL_VIDEO_CENTERED'] = '1'

#this will intialize pygame change the name of the window and take the mouse away when you are on the game application
pygame.init()
pygame.display.set_caption('Bullet Bill')
pygame.mouse.set_visible(False)
pygame.key.set_repeat(50)



#this will give you the background for the game and the title of it
imgbackground = pygame.image.load('images/game-background.png')

imgtitle = pygame.image.load('images/title.png')

#this is our surface varible
surface = pygame.display.set_mode((imgbackground.get_width(), imgbackground.get_height()))

#these give us our game font and the score font
score_font = pygame.font.Font('magicdreams.ttf', 28)
game_font = pygame.font.Font('magicdreams.ttf', 48)

#these varibles is for the click the space bar and it out puts the score and the click the spcae bar also the gameover
start_output = game_font.render('CLICK SPACEBAR TO START', True, pygame.Color('#426b94'))

score_output = score_font.render("{:<8s}{:<5d}".format('SCORE:', score), True, pygame.Color('#426b94'))

gameover_output = game_font.render('GAME OVER', True, pygame.Color('#426b94'))

done = False


TOP_BORDER, BOTTOM_BORDER = 50, pygame.display.get_surface().get_height() - 30

#this is the img of lives in a list.
imglives = [None] * 4
numlives = 3

#this is just the Koopa imagie
koopa =  pygame.image.load('images/koopaEast.png')

M = Magikoopa()

#list of bullets
bullet_list = []
for i in range(20):
    b =  Bullet_Bill()
    for i in bullet_list:
        while b.get_bounds().colliderect(i.get_bounds()):
            b.position()

    bullet_list.append(b)

clock = pygame.time.Clock()

#timer for Koopa
pygame.time.set_timer(pygame.USEREVENT, 500)

#timer for Bullet Bill
pygame.time.set_timer(pygame.USEREVENT + 1, 500)

global dead
dead = False
keys = True



while not done:
  #list for Koopa lives
  for i in range(len(imglives)):
    imglives[i] = pygame.image.load('images/lives' + str(i) + '.png')

  #creates a funcional X button for the window on the top right of the window.
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

    #key inputs
    if event.type == pygame.KEYDOWN:
      #when the space bar is pressed, the game starts.
      if event.key == pygame.K_SPACE:
        startgame = True
        #pygame.mixer.music.play(-1)

    if startgame == True:
      #this code is the timer that makes the Magikoopa have gravity.
      if event.type == pygame.USEREVENT:
        if dead == True:
          M.move_down(25)
        else:
          M.move_down(10)

      #this code is the timer that makes the Bullet Bill move from right to left of the screen.
      if event.type == pygame.USEREVENT + 1:
        for i in bullet_list:
          i.move(20)

      if keys == True:
        if event.type == pygame.KEYDOWN:
          #when the right arrow or the d key is pressed, the koopa moves right by how much units is inputted.
          if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            M.move_right(10)

          #when the left arrow or the a key is pressed, the koopa moves left by how much units is inputted.
          if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            M.move_left(10)

          #when the up arrow or the w key is pressed, the koopa moves up by how much units is inputted.
          if event.key == pygame.K_UP or event.key == pygame.K_w:
            M.move_up(10)

          #when the down arrow or the s key is pressed, the koopa moves down by how much units is inputted.
          if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            M.move_down(10)

  #outputs the background
  surface.blit(imgbackground, (0, 0))
  #outputs the title of the game on the top middle of the window.
  surface.blit(imgtitle, (pygame.display.get_surface().get_width() // 2 - imgtitle.get_width() // 2, 10))

  #outputs the number of lives on the top right corner of the window.
  surface.blit(imglives[numlives], (pygame.display.get_surface().get_width() - imglives[numlives].get_width() - 10, 15))

  score_output = score_font.render("{:<8s}{:<5d}".format('SCORE:', score), True, pygame.Color('#426b94'))

  #outputs the score on the top left of the window.
  surface.blit(score_output, (15, 15))

  #this part of the program will print out the text that tells the user to click the space bar to start the game.
  if startgame == False:
    surface.blit(start_output, (pygame.display.get_surface().get_width() // 2 - start_output.get_width() // 2,pygame.display.get_surface().get_height() // 2 - 115))

  #this is going to get rid of the text when space bar is clicked
  if startgame == True:
    M.border()

    #outputs the Magikoopa
    if dead == False:
      surface.blit(M.get_img(),(M.getX(), M.getY()))

    #resets the x and y coordinates when the bullet reaches an x value less than 0. The score increases by 100 and makes a sound for scoring points.
    for B in bullet_list:
      if B.getX() < 0:
        B.position()
        for i in bullet_list:
            for x in range(10):
                if B.get_bounds().colliderect(i.get_bounds()):
                    B.position()
                    print("working")
                else:
                    break
        score += 100
        # point_sound = pygame.mixer.Sound("Score.mp3")

      #outputting the Bullet Bills
      surface.blit(B.get_img(), (B.getX(), B.getY()))

      #collision for when the koopa hits the Bullet Bills
      if M.get_bounds().colliderect(B.get_bounds()):
        pygame.time.set_timer(USEREVENT + 1, 0)
        dead = True
        keys = False

      #this makes him die when he hits the ground
      if M.getY() == 400:
        dead = True

      #when dead, the dead koopa image is outputed
      if dead == True:
        surface.blit(M.dead(dead),(M.getX(), M.getY()))

        if M.getY() == 400:
          M.reset()
          numlives -= 1
          dead = False
          keys = True
          B.position()
          pygame.time.set_timer(pygame.USEREVENT + 1, 500)





    if M.getX() == 400:
      messagebox.showinfo('Bullet Bill', "You chrash landed!")


    if numlives == 0 :
        if messagebox.askyesno("", "would you like play agian"):
            numlives = 3
            startgame = True
        else:
            quit()
            startgame = False
            done = True
            quit()







    #this outputs the gameover once lives are Zero
    if numlives == 0:
      surface.blit(gameover_output, (pygame.display.get_surface().get_width() // 1 - start_output.get_width() // 1 ,pygame.display.get_surface().get_height() // 2 - 115))
      startgame = False




  clock.tick(60)

  #this updates the window
  pygame.display.update()
  surface.blit(imgbackground, (0, 0))
