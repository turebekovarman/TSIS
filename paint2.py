import pygame 
import time

pygame.init()

BLUE = (0, 0, 255)
width = 500
height = 500

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

isPressed = False   #для контролирования нажатий мышки
prevPoint =pygame.mouse.get_pos()
curPoint =pygame.mouse.get_pos()

yellow=((255,255,102))
font_style=pygame.font.SysFont(None,30)

#0 - pencil, 1 - rectangle
currentTool = 0   # 0 - line, 1 = rect, 2 = circle, 3 - eraser
toolCount = 4  
figure="Line"  
background = pygame.image.load("./Desktop/back.jpg")
background = pygame.transform.scale(background, (500,20))


def Your_figure(figure):
    value=font_style.render("Your Figure: "+str(figure),True,yellow)
    screen.blit(value,[0,0])

def drawRectangle(surface, color, x, y, w, h):
    pygame.draw.rect(surface, color, [x, y, w, h],5)

def drawCircle(surface,color,x,y):
    pygame.draw.circle(surface, color,[x,y], 20)

def drawLine(surface, color, startPos, endPos):  
    pygame.draw.line(surface, color, startPos, endPos, 5)

def drawEraser(surface, x,y):
    pygame.draw.circle(surface, (255, 255, 255), [x,y], 20)


running = True

color = (0,0,0)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                currentTool = (currentTool + 1) % toolCount
            elif event.key==pygame.K_c:
                screen.fill((255,255,255)) 
            elif event.key==pygame.K_y:
                color=(255,255,0)
            elif event.key==pygame.K_g:
                color=(0,255,0)
            elif event.key==pygame.K_r:
                color=(255,0,0)
            elif event.key==pygame.K_b:
                color=(0,0,0)
            elif event.key==pygame.K_o:
                color=(255,69,0)
            elif event.key==pygame.K_p:
                color=(218,112,214)

            elif event.key==pygame.K_s:
                pygame.image.save(screen,"./Desktop/mypaintpictures/paint_image.png") 
        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
            prevPoint = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            prevPoint = pygame.mouse.get_pos()
            isPressed = False
        elif event.type == pygame.MOUSEMOTION and isPressed == True:
            prevPoint = curPoint
            curPoint = pygame.mouse.get_pos()
            
    if currentTool == 0:
        figure="Line"
        drawLine(screen,color, prevPoint, curPoint)
    elif currentTool == 1:
        figure="Rectangle"
        drawRectangle(screen,color, curPoint[0],curPoint[1],100,100)
    elif currentTool == 2:
        figure="Circle"
        drawCircle(screen,color, curPoint[0], curPoint[1]) 
    elif currentTool == 3:
        figure="Eraser"
        drawEraser(screen,curPoint[0],curPoint[1])
        
    clock.tick(60)
    screen.blit(background, (0, 0))
    Your_figure(figure)
    pygame.display.update()
pygame.quit()