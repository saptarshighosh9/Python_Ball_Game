import pygame, sys
from pygame import *
import random
pygame.init()
size=(700,500)
screen=pygame.display.set_mode(size)   
pygame.FULLSCREEN
pygame.display.set_caption("Version 0.1_dev>gooblU_under:>Python_2.7")
#############################################################################
score=0
drop=0
done = False
l=False
p=100
q=390
d=10
ss=240
dd=8
col=(242,225,31)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
black=(0,0,0)



bb=pygame.image.load('ball2.jpg')
aa=pygame.image.load('bck1.jpg')

b1=pygame.image.load('ball2.jpg')
b2=pygame.image.load('ball2.jpg')
b3=pygame.image.load('ball2.jpg')
b5=pygame.image.load('ball2.jpg')
fc=pygame.image.load('pp1.gif')
fcc=pygame.image.load('ball2.png')
font = pygame.font.Font(None, 20)

# Used to manage how fast the screen updates

clock = pygame.time.Clock()
 
star_list=[]
for i in range(50):
       x = random.randrange(0,680)
       y = random.randrange(0,490)
       star_list.append([x,y])
ball_list=[]  
r=0 
ball_list.append([130,r])   
ball_list.append([230,r])
ball_list.append([430,r])
ball_list.append([530,r])




############################################################################# 

while l==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
           pygame.quit()
           sys.exit()
        
    for i in range(len(star_list)):
        pygame.draw.circle(screen, col, star_list[i], 1)
        star_list[i][1] += 1
	if star_list[i][1] > 490:
           y = random.randrange(-50,-10)
           star_list[i][1] = y
	   x = random.randrange(0,680)
 	   star_list[i][0] = x
    b11=pygame.image.load('img1.jpg')  
    screen.blit(b11,[60,100]) 
    text = font.render("Welcome",True,white)
    screen.blit(text, [250,320])
    st1="Thank you for trying this game."
    st2="Build in 'Python 2.7' "
    st3="Developer: Gooblu "
    st4="Press Enter to continue"
    text = font.render(st1,True,white)
    screen.blit(text, [250,330])
    text = font.render(st2,True,red)
    screen.blit(text, [250,350])
    text = font.render(st3,True,green)
    screen.blit(text, [250,370])
    text = font.render(st4,True,white)
    screen.blit(text, [250,100])
	
    keys = pygame.key.get_pressed()
    if keys[K_RETURN]:
       l = True
       
    pygame.display.flip()
    clock.tick(20)   
	      
              
		
          

#########################################################################
while done == False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
           pygame.quit()
           sys.exit()
        if event.type ==pygame.MOUSEBUTTONDOWN:
           m,n=pygame.mouse.get_pos() 	
           if m> 230 and m<360:
              if n>230 and n<290:     
                 done=True	
           
     
    
    screen.fill(black)
    
      
    for i in range(len(star_list)):
        pygame.draw.circle(screen, white, star_list[i], 2)
        star_list[i][1] += 1
	if star_list[i][1] > 490:
           y = random.randrange(-50,-10)
           star_list[i][1] = y
	   x = random.randrange(0,680)
           star_list[i][0] = x
    text = font.render("         Click to Start   ",True,blue)
    screen.blit(text, [250,250])
    text = font.render("Hit the footballs and bounce them back to get points.",True,white)
    screen.blit(text, [250,280])
    text = font.render("Number of misses will be counted.",True,white)
    screen.blit(text, [250,300])
    text = font.render("MIss count if exceed 100,...Game over.",True,white)
    screen.blit(text, [250,320])	
   # pygame.draw.rect(screen,col,[p,q,10,10])
   # pygame.draw.rect(screen,red,[p+2,q+2,6,6])
    b15=pygame.image.load('bl.jpg') 
    screen.blit(b15,[100,ss])
    ss+=dd  
    if ss==336:
       dd=dd*(-1)
    if ss==240:
       dd=dd*(-1)     
       
    pygame.display.flip()
    clock.tick(20)
    
  ########################################################################  
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
           pygame.quit()
           sys.exit()
    
    screen.fill(white)
    vb=False
    pygame.mouse.set_visible(vb)
    pygame.draw.line(screen,red,(7,10),(7,480),3)
    pygame.draw.line(screen,red,(7,10),(680,10),3)
    pygame.draw.line(screen,green,(680,10),(680,480),3)
    pygame.draw.line(screen,green,(7,480),(680,480),3)
    
    screen.blit(b1,ball_list[1])  
    screen.blit(b2,ball_list[2])
    screen.blit(b3,ball_list[3]) 
    screen.blit(b5,ball_list[0]) 	
    ball_list[0][1] += 3	       	
    ball_list[1][1] += 5
    ball_list[2][1] += 2
    ball_list[3][1] += 6
    
    
    
    for i in range(len(ball_list)):
   	if ball_list[i][1] > 480:
           x = random.randrange(10,650)
           ball_list[i][0] = x
           ball_list[i][1] = 0
           drop +=1	
    keys = pygame.key.get_pressed()
 	  
    if keys[K_LEFT]:
       p-=d

    if keys[K_RIGHT]:
       p+=d
    
    if p >621:
       p=620
    elif p<10:
       p=10
       
    screen.blit(fc,[p,q+30])
    #pygame.draw.rect(screen,blue,[p,q+30,60,20])
       
    t=[90,120,120,180,210,240]
    bbb=[90,85,59,45,70,60]
    nm=50
    mn=90
    if ball_list[1][1]==q-30:
       if ball_list[1][0]>p-nm and ball_list[1][0]<p+mn:    
          rr=random.randrange(0,5)
          ball_list[1][1] -= t[rr]
           
          if ball_list[1][0] < 350:
             ball_list[1][0] += bbb[rr] 
          else:
             ball_list[1][0] -= bbb[rr]   
          score+=1
    if ball_list[2][1]==q-30:
       if ball_list[2][0]>p-nm and ball_list[2][0]<p+mn: 	    
          rr=random.randrange(0,5)	        
          ball_list[2][1] -= t[rr]
          if ball_list[2][0] < 350:
             ball_list[2][0] += bbb[rr] 
          else:
             ball_list[2][0] -=bbb[rr] 
          score+=1
    if ball_list[3][1]== q-30:
       if ball_list[3][0]>p-nm and ball_list[3][0]<p+mn:    
          rr=random.randrange(0,5)	  
          ball_list[3][1] -= t[rr]
          if ball_list[3][0] < 350:
             ball_list[3][0] += bbb[rr]
          else:
             ball_list[3][0] -= bbb[rr]	
          score+=1
    if ball_list[0][1]==q-30:
       if ball_list[0][0]>p-nm and ball_list[0][0]<p+mn:	    
          rr=random.randrange(0,5)	    
          ball_list[0][1] -= t[rr]  
          if ball_list[0][0] < 350:
             ball_list[0][0] +=bbb[rr] 
          else:
             ball_list[0][0] -= bbb[rr]
          score+=1
         
        
    
    text = font.render("Score : "+str(score),True,black)
    screen.blit(text, [620,420])
    text = font.render("Drop : "+str(drop),True,black)
    screen.blit(text, [620,450])
    
    if drop>100:
       break  
           
    pygame.display.flip()
    clock.tick(50)
    
     
while True:
    screen.fill(black)
    vb=True
    pygame.mouse.set_visible(vb)
    
    bb=pygame.image.load('gmovr.jpg')
    screen.blit(bb,[0,0])
    text = font.render("Score: "+str(score),True,white)
    screen.blit(text, [100,480])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
           pygame.quit()
           sys.exit()       
       
    pygame.display.flip()
    clock.tick(20) 
    
