import pygame, math
from pygame.locals import *
        

pygame.init()

WINDOWWIDTH = 640 
WINDOWHEIGHT = 480
 
win_center_x = int(WINDOWWIDTH / 2) 
win_center_y = int(WINDOWHEIGHT / 2) 

AMPLITUDE = 100 
xPos = 0
step = 0
index = 0
running = True
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
window.fill((255, 255, 255))
posRecord = {'sin': [], 'cos': []}


while running == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            running=False
            
#     pygame.draw.line(window, (0, 0, 0), (0, win_center_y), (WINDOWWIDTH, win_center_y))
#     pygame.draw.line(window, (0, 0, 0), (win_center_x, 0), (win_center_x, WINDOWHEIGHT))
    
  # sinus
    yPos = -1 * math.sin(step) * AMPLITUDE # -1 * sin(0.008) * 100 = y x = 0.5
    posRecord['sin'].append((int(xPos), int(yPos) + win_center_y)) # [(0, 240), (x, y)]
    if len(posRecord['sin']) >= 2:
        n = len(posRecord['sin']) - 1 # индекс последнего элемента
        start = posRecord['sin'][n - 1] #B  posRecord[n - 1]
        end = posRecord['sin'][n] #C posRecordsin[n]
        pygame.draw.line(window, (128,   0,   0), start, end, 4)
        
  #cosinus
    yPos = -1 * math.cos(step) * AMPLITUDE
    posRecord['cos'].append((int(xPos), int(yPos) + win_center_y))
    if len(posRecord['cos']) >= 2:
        n = len(posRecord['cos']) - 1 
        start = posRecord['cos'][n - 1]
        end = posRecord['cos'][n]
#         draw_dashed_line(window, (255, 255, 255), start, end, index)
        if index % 2 == 0:
            pygame.draw.line(window, (255, 255, 255), start, end, 5)    
        else:
            pygame.draw.line(window, (0, 0, 0), start, end, 5)    
    index += 1
    xPos += 0.5
    step += 0.03
    step %= 2 * math.pi #step = 0.008
    pygame.display.update()
pygame.quit()