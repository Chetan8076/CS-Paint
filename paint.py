import pygame
from pygame.locals import*
import sys
RED=(255,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
bottomColor=(0,0,0)
HEIGHT=25
WIDTH=25
MARGIN=0
color=BLACK
COLORS1=[(26, 188, 156),(205, 97, 85),(27, 38, 49),(29, 131, 72),(165, 105, 189),(84, 153, 199),(236, 112, 99),(108, 52, 131),(171, 178, 185),(245, 176, 65)]
COLORS2=[(0, 77, 64),(1, 87, 155),(26, 35, 126),(74, 20, 140),(136, 14, 79),(183, 28, 28),(62, 39, 35),(230, 81, 0),(245, 127, 23),(130, 119, 23)]
lst=[]
temp=[]
grid=[[1 for a in range(21)] for b in range(21) ]


def areaFill(x,y,grid):
    cubeFill=[]
    cubeFill=[(x//WIDTH,y//HEIGHT)]
    print(cubeFill)
    while True:
        if len(cubeFill)==0:
            return False
        else:
            
            x=cubeFill[0][0]
            y=cubeFill[0][1]
            if grid[x][y]:

                cubeFill.append((x,y-1))
                cubeFill.append((x,y+1))
                cubeFill.append((x-1,y))
                cubeFill.append((x+1,y))
                pygame.draw.rect(SCREEN,color,[WIDTH*(x),HEIGHT*(y),WIDTH,HEIGHT])
                print(cubeFill[0])
                cubeFill.remove(cubeFill[0])
                grid[x][y]=0
                

            else:
                cubeFill.remove(cubeFill[0])
            
                



def redraw():
    
    for row in range(21):
            for column in range(21):
                pygame.draw.rect(SCREEN,
                                 BLACK,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])  
    #             pygame.draw.circle(SCREEN,WHITE,((WIDTH*column),(HEIGHT*row)),5)

    pygame.draw.line(SCREEN,bottomColor,(0,499),(500,499))
   
    pygame.draw.rect(SCREEN,
                     WHITE,
                     [0,500,500,100])
    # pygame.draw.circle(SCREEN,GREEN,(200,550),20)
    # pygame.draw.circle(SCREEN,RED,(250,550),20)
    # pygame.draw.circle(SCREEN,BLUE,(300,550),20)
    for i,colors in zip(range(300,500,20),COLORS1):
        pygame.draw.rect(SCREEN,colors,[i,500,20,20])
    for i,colors in zip(range(300,500,20),COLORS2):
        pygame.draw.rect(SCREEN,colors,[i,520,20,20])
    pygame.draw.rect(SCREEN,BLACK,[460,545,30,30])
    pygame.draw.rect(SCREEN,WHITE,[461,546,28,28])
    showChar=myFont.render('C',1,BLACK)
    SCREEN.blit(showChar,(465,546))
    pygame.draw.rect(SCREEN,BLACK,[430,545,30,30])
    pygame.draw.rect(SCREEN,WHITE,[431,546,28,28])
    SCREEN.blit(pygame.image.load('eraser1.jpg'),(438,547))
    pygame.draw.rect(SCREEN,BLACK,[400,545,30,30])
    pygame.draw.rect(SCREEN,WHITE,[401,546,28,28])
    showChar=myFont.render('F',1,BLACK)
    SCREEN.blit(showChar,(405,546))



    






if __name__ == '__main__':

    pygame.init()
    SCREEN=pygame.display.set_mode((500,600))
    SCREEN.fill(WHITE)
    myFont = pygame.font.SysFont("Times New Roman", 25)
    areaFillFlag=False

    

    redraw()

    while True:
        x,y=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif y<(500-HEIGHT) and pygame.mouse.get_pressed()[0]:
                if areaFillFlag:
                    areaFill(x,y,grid)
                    print(areaFillFlag)
                    areaFillFlag=False
                    print(areaFillFlag)
                    
                else:   
                    pygame.draw.rect(SCREEN,
                                     color,
                                     [(MARGIN + WIDTH) * ((x//WIDTH)) + MARGIN,
                                      (MARGIN + HEIGHT) * ((y//HEIGHT))+ MARGIN,
                                      WIDTH,
                                      HEIGHT])
                    grid[x//WIDTH][y//HEIGHT]=0
                    # pygame.draw.circle(SCREEN,color,(x,y),4)
                    # pygame.draw.circle(SCREEN,color,(x,y-1),4)


            
            elif x>=300 and x<=500 and y>=500 and y<=520 and pygame.mouse.get_pressed()[0]:
                a=(int((x-300)/20))
                if a==0:
                    color=COLORS1[0]
                else:
                    color=COLORS1[a]
            elif x>=300 and x<=500 and y>=520 and y<=540 and pygame.mouse.get_pressed()[0]:
                # a=(int((x-300)/20))
                # if a==0:
                #     color=COLORS2[0]
                # else:
                #     color=COLORS2[a]
                color=COLORS2[int((x-300)/20)]
            elif x>=460 and x<=490 and y>=540 and y<=570 and pygame.mouse.get_pressed()[0]:
                SCREEN.fill(WHITE)
                grid=[[1 for a in range(21)] for b in range(21) ]
                areaFillFlag=False

                redraw()
            elif x>=430 and x<460 and y>=540 and y<=570 and pygame.mouse.get_pressed()[0]:
                color=WHITE
            elif x>=400 and x<430 and y>=540 and y<=570 and pygame.mouse.get_pressed()[0]:
                areaFillFlag=True
                # areaFill(x,y,grid)






               
        # for row in range(50):
        #     for column in range(50):
        #         pygame.draw.rect(SCREEN,
        #                          WHITE,
        #                          [(MARGIN + WIDTH) * column + MARGIN,
        #                           (MARGIN + HEIGHT) * row + MARGIN,
        #                           WIDTH,
        #                           HEIGHT])
        pygame.display.update()
            
                
