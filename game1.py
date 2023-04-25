import pygame
from random import randint
from pygame import mixer
import random 

pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Minions')

running = True
GREEN = (0,200,0)
RED = (255,0,0)
FPS = 60 

WIDTH,HEIGHT=1200,600
clock = pygame.time.Clock()
i=0 

#Size
TUBE_WIDTH = 70
TUBE1_WIDTH =50
TUBE3_WIDTH = - TUBE1_WIDTH - 1000

TUBE_GAP =160
TUBE_HEIGHT=100
TUBE1_WIDTH=25
TUBE1_HEIGHT=250

BIRD_WIDTH=50
BIRD_HEIGHT=50 

TUBE2_WIDTH=1200
TUBE2_HEIGHT=1

BANANA_WIDTH=40
BANANA_HEIGHT=50
 
TREE1_WIDTH = 300
TREE1_HEIGHT= 175

#Coordinates(tọa độ)

tube1_height = 170
tube2_height = randint(170,180)
tube3_height = randint(145,155)
tube4_height = randint(280,300)
tube5_height = randint(120,140)
tube6_height = randint(170,190)

TUBE_X = 2750
TUBE1_X = TUBE_X - 1000
BIRD_X = 100
bird_y = 400

BANANA_x1=1150
BANANA_x2=1750
BANANA_x3=2350
BANANA_y=randint(100,400)

tube1_x = 1000
tube2_x = tube1_x+300
tube3_x = tube1_x+600
tube4_x = tube1_x+900
tube5_x = tube1_x+1200
tube6_x = tube1_x+1500

tube1_y = 0
tube2_y = 70
tube3_y = 55
tube4_y = 125
tube5_y = 90
tube6_y = 100

tree1_x = 2700
tree2_x = 3250

tree1_y = randint(10,20)
tree2_y = randint(60,70)

stone_x = 2700
stone_y = 430

moon_x = 3100
moon_y = randint(60,100)

bird_drop_velocity=0
GRAVITY=0.45   
TUBE_VELOCITY = 3.5

score = 0
banana = 0 
font= pygame.font.SysFont('Segoe', 50)

tube1_pass = False
tube2_pass = False
tube3_pass = False
tube4_pass = False
tube5_pass = False
tube6_pass = False

banana1_pass= False
banana2_pass= False
banana3_pass= False

tree1_pass = False
tree2_pass = False
stone_pass = False
moon_pass = False

pausing= False

#Uplate image
background_image = pygame.image.load("image/bk.png")
background_image = pygame.transform.scale(background_image,(WIDTH, HEIGHT))

bird_image = pygame.image.load("image/icon.png")
bird_image = pygame.transform.scale(bird_image,(BIRD_WIDTH, BIRD_HEIGHT))

tree_image = pygame.image.load("image/tree1.png")
tree_image = pygame.transform.scale(tree_image,(TREE1_WIDTH, TREE1_HEIGHT))

stone_image = pygame.image.load("image/stone.png")
stone_image = pygame.transform.scale(stone_image,(1000,170))

moon_image = pygame.image.load("image/moon.png")
moon_image = pygame.transform.scale(moon_image,(75,75))

gameover_image = pygame.image.load("image/game_over.png")
gameover_image = pygame.transform.scale(gameover_image,(860, HEIGHT))

gameover1_image = pygame.image.load("image/game_over1.png")
gameover1_image = pygame.transform.scale(gameover1_image,(WIDTH, HEIGHT))

banana_image = pygame.image.load("image/bananas.png")
banana_image = pygame.transform.scale(banana_image,(BANANA_WIDTH, BANANA_HEIGHT))

tube_image = pygame.image.load("image/tube.png")
tube_image = pygame.transform.scale(tube_image,(30, BANANA_HEIGHT))

tube1_image = pygame.image.load("image/tube.png")
tube1_image = pygame.transform.scale(tube1_image,(TUBE_WIDTH, tube1_height))
tube1v_image = pygame.transform.scale(tube1_image,(TUBE_WIDTH,HEIGHT-tube1_y-tube1_height-TUBE_GAP ))

tube2_image = pygame.transform.scale(tube1_image,(TUBE_WIDTH, tube2_height))
tube2v_image = pygame.transform.scale(tube1_image,(TUBE_WIDTH,530-tube2_height-TUBE_GAP-tube2_y))

tube3_image = pygame.transform.scale(tube1_image,(TUBE_WIDTH, tube3_height))
tube3v_image = pygame.transform.scale(tube1_image,(TUBE_WIDTH,530-tube3_height-TUBE_GAP-tube3_y))

tube4_image = pygame.transform.scale(tube1_image,(TUBE_WIDTH, tube4_height))

tube5_image = pygame.transform.scale(tube1_image,(TUBE_WIDTH, tube5_height))
tube5v_image = pygame.transform.scale(tube1_image,(TUBE_WIDTH,530-tube5_height-TUBE_GAP-tube5_y))

tube6_image = pygame.transform.scale(tube1_image,(TUBE_WIDTH, tube6_height))
tube6v_image = pygame.transform.scale(tube1_image,(TUBE_WIDTH,530-tube6_height-TUBE_GAP-tube6_y))
#Update image
meme1_list = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png']
random1_file = random.choice(meme1_list)
meme2_list = ['11.png','12.png','13.png','14.png','15.png','16.png','17.png','18.png','19.png','20.png']
random2_file = random.choice(meme2_list)

#Sound
point = pygame.mixer.Sound('sound/point.mp3')
wing = pygame.mixer.Sound('sound/wing.wav')
wing.set_volume(0.4)
music1 = pygame.mixer.Sound('sound/22.wav')
music1.set_volume(0.4)

while running:
     clock.tick(FPS)
     screen.blit(background_image,(i,0))
     screen.blit(background_image,(WIDTH+i,0))
     if i == -WIDTH:
        screen.blit(background_image,(WIDTH+i,0))
        i=0
     i -= 1   
      
     #Draw back, bird, moon(vẽ màn hình, chim , mặt trăng  )
     tube_up_rect = pygame.draw.rect(screen,GREEN, (0,0,1200,1)) 
     tube_down_rect = pygame.draw.rect(screen,GREEN, (0,599,1200,1))
     bird_rect = screen.blit(bird_image, (BIRD_X,bird_y)) 
     moon_rect = screen.blit(moon_image,(moon_x,moon_y))

     #Draw tube 
     tube1_rect = screen.blit(tube1_image, (tube1_x,tube1_y))
     tube2_rect = screen.blit(tube2_image, (tube2_x,tube2_y))
     tube3_rect = screen.blit(tube3_image, (tube3_x,tube3_y))
     tube4_rect = screen.blit(tube4_image, (tube4_x,tube4_y))
     tube5_rect = screen.blit(tube5_image, (tube5_x,tube5_y))
     tube6_rect = screen.blit(tube6_image, (tube6_x,tube6_y))

     #Draw tube inverse 
     tube1_rect_inv = screen.blit(tube1v_image, (tube1_x,tube1_height+TUBE_GAP))
     tube2_rect_inv = screen.blit(tube2v_image, (tube2_x,tube2_y+tube2_height+TUBE_GAP))
     tube3_rect_inv = screen.blit(tube3v_image, (tube3_x,tube3_y+tube3_height+TUBE_GAP))
     tube5_rect_inv = screen.blit(tube5v_image, (tube5_x,tube5_y+tube5_height+TUBE_GAP))
     tube6_rect_inv = screen.blit(tube6v_image, (tube6_x,tube6_y+tube6_height+TUBE_GAP))
     
     #Draw bananas
     banana1_rect  = screen.blit(banana_image, (BANANA_x1,BANANA_y))
     banana2_rect  = screen.blit(banana_image, (BANANA_x2,BANANA_y))
     banana3_rect  = screen.blit(banana_image, (BANANA_x3,BANANA_y))
    
     #Draw tree
     tree1_rect = screen.blit(tree_image,(tree1_x, tree1_y))
     tree2_rect = screen.blit(tree_image,(tree2_x, tree2_y))
     stone_rect = screen.blit(stone_image,(stone_x, stone_y))

     #Move tube to the left    
     tube1_x = tube1_x - TUBE_VELOCITY 
     tube2_x = tube2_x - TUBE_VELOCITY
     tube3_x = tube3_x - TUBE_VELOCITY
     tube4_x = tube4_x - TUBE_VELOCITY
     tube5_x = tube5_x - TUBE_VELOCITY
     tube6_x = tube6_x - TUBE_VELOCITY

     BANANA_x1 = BANANA_x1 -TUBE_VELOCITY
     BANANA_x2 = BANANA_x2 -TUBE_VELOCITY
     BANANA_x3 = BANANA_x3 -TUBE_VELOCITY

     tree1_x   = tree1_x   - TUBE_VELOCITY
     tree2_x   = tree2_x   - TUBE_VELOCITY
     stone_x = stone_x - TUBE_VELOCITY
     moon_x = moon_x - TUBE_VELOCITY

     #Create new tube 
     if tube1_x < - TUBE1_WIDTH:
        tube1_x = TUBE_X
        tube1_height = 170
        tube1_pass = False
     if tube2_x < - TUBE1_WIDTH:
        tube2_x = TUBE_X
        tube2_height = randint(170,180)
        tube2_pass =False
     if tube3_x < - TUBE1_WIDTH:
        tube3_x = TUBE_X
        tube3_height = randint(145,155)
        tube3_pass = False  
     if tube4_x < - TUBE1_WIDTH: 
        tube4_x = TUBE_X
        tube4_height = randint(290,300)
        tube4_pass = False
     if tube5_x < - TUBE1_WIDTH:
        tube5_x = TUBE_X
        tube5_height = randint(100,120)
        tube5_pass = False
     if tube6_x < - TUBE1_WIDTH:
        tube6_x = TUBE_X
        tube6_height = randint(190,200)
        tube6_pass = False

     if tree1_x < TUBE3_WIDTH:
        tree1_x = TUBE1_X
        tree1_y = randint(10,30)
        tree1_pass = False
     if tree2_x < TUBE3_WIDTH:
        tree2_x = TUBE1_X 
        tree2_y = randint(40,80)
        tree2_pass = False
     if stone_x < TUBE3_WIDTH:
        stone_x = TUBE1_X
        stone_pass = False
     if moon_x <TUBE3_WIDTH:
        moon_x = TUBE1_X
        moon_pass = False

     if BANANA_x1 < -TUBE1_WIDTH:
        BANANA_x1 = TUBE_X
        BANANA_y1 = randint(100,500)
        banana1_pass = False
     if BANANA_x2 < -TUBE1_WIDTH:
        BANANA_x2 = TUBE_X
        BANANA_y2 = randint(100,500)
        banana2_pass = False
     if BANANA_x3 < -TUBE1_WIDTH:
        BANANA_x3 = TUBE_X
        BANANA_y3 = randint(100,500)
        banana3_pass=False
            
     #Bird down(Chim rơi )
     bird_y += bird_drop_velocity + 0.5*GRAVITY
     bird_drop_velocity += GRAVITY
     
     #Uplate score (Cập nhât điểm )
     tube_rect  = screen.blit(tube_image, (0,00))
     score_txt=font.render("x"+ str(score),True,RED)
     screen.blit(score_txt,(30,5))
     banana_rect  = screen.blit(banana_image, (250,0))
     score_txt=font.render("x"+ str(banana),True,RED)
     screen.blit(score_txt,(300,5))

     if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass ==False :
        score+=2
        tube1_pass = True
     if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass ==False :
        score+=2
        tube2_pass = True
     if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass ==False :
        score+=2
        tube3_pass = True 
     if tube4_x + TUBE_WIDTH <= BIRD_X and tube4_pass ==False :
        score+=1 
        tube4_pass = True 
     if tube5_x + TUBE_WIDTH <= BIRD_X and tube5_pass ==False :
        score+=2
        tube5_pass = True 
     if tube6_x + TUBE_WIDTH <= BIRD_X and tube6_pass ==False :
        score+=2
        tube6_pass = True 

     if bird_rect.colliderect(banana1_rect)  :
       pygame.mixer.Sound.play(point)
       banana+=1
       BANANA_x1= TUBE_X+200
       BANANA_y1=randint(100,500)
       
     if bird_rect.colliderect(banana2_rect)  :
       pygame.mixer.Sound.play(point)
       banana+=1
       BANANA_x2= TUBE_X+200
       BANANA_y2=randint(50,550)
       
     if bird_rect.colliderect(banana3_rect)  :
       pygame.mixer.Sound.play(point)
       banana+=1
       BANANA_x3= TUBE_X+200
       BANANA_y3=randint(100,500)
       
     if banana == 5  :
       screen.blit(random1_file,(600,0))
     if banana % 15== 0 and banana !=0   :
       screen.blit(random2_file,(600,0))
     if score >=10 and score <= 15: 
       screen.blit(random1_file,(800,0)) 
     if score >=25 and score <= 28: 
       screen.blit(random2_file,(800,0)) 
     if score % 30 ==0  and score != 0:
        screen.blit(random1_file,(800,0))
     #Check Collision( kiểm tra va chạm )
     for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube3_rect_inv,
                  tube4_rect,tube5_rect,tube5_rect_inv,tube6_rect,tube6_rect_inv,
                  tube_up_rect,tube_down_rect, tree1_rect, tree2_rect, stone_rect, moon_rect]:
         if bird_rect.colliderect(tube) :
            pygame.mixer.Sound.play(music1)
            pausing=True
            TUBE_VELOCITY=0
            bird_drop_velocity = 0
            screen.blit(gameover_image,(0,0))
            screen.blit(gameover1_image,(0,0))
            screen.blit(tube_image,(970,260))
            score_txt=font.render(" x"+ str(banana),True,RED)
            screen.blit(score_txt,(1020,210))
            score_txt=font.render(" x"+ str(score),True,RED)
            screen.blit(score_txt,(1020,265))
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
          if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE or event.key == pygame.MOUSELEFT:
               pygame.mixer.Sound.play(wing)
               #Reset
               if pausing:
                 pygame.mixer.Sound.stop(music1) 
                 bird_y=400
                 TUBE_VELOCITY = 3.5
                 tube1_x = 1000
                 tube2_x = 1300
                 tube3_x = 1600
                 tube4_x = 1900
                 tube5_x = 2200
                 tube6_x = 2500

                 BANANA_x1=1150
                 BANANA_x2=1750
                 BANANA_x3=2350

                 tree1_x = 2700
                 tree2_x = 3250
                 moon_x = 3100
                 stone_x = 2700
                 
                 score = 0
                 banana = 0
                 pausing= False

               bird_drop_velocity = 0
               bird_drop_velocity-= 4.

     pygame.display.flip()

pygame.quit()