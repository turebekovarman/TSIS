import pygame
import time
import random

pygame.init()

white=(255,255,255)
yellow=(255,255,102)
black=(0,0,0)
red=(213,50,80)
green=(0,255,0)
blue=(50,153,213)
gold=(255,215,0)


dis_width=600
dis_height=400

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("SNAKE GAME")

clock=pygame.time.Clock()

snake_speed=15

font_style=pygame.font.SysFont(None,30)
score_font=pygame.font.SysFont(None,25)

def Your_score(score1,score2):
    value=score_font.render("B: "+str(score1)+" G: "+str(score2),True,yellow)
    dis.blit(value,[0,0])

def our_snake(number,snake_list): #snake list будет увеличивать змейку когда она кушает
    for position in snake_list:
        x1=position[0] 
        y1=position[1]
        pygame.draw.rect(dis,black,[x1,y1,10,10])

#def snake_2(num)

def snake_2(number, snake_list):
    for position in snake_list:
        x2=position[0]
        y2=position[1]
        pygame.draw.rect(dis,gold,[x2,y2,10,10])

def message(msg,color):
    mesg=font_style.render(msg,True, color)
    dis.blit(mesg,[dis_width/6,dis_height/3])

def gameLoop():
    game_over=False
    game_close=False
#start position of snakes
    x1=300
    y1=200

    x2=150
    y2=150

#на сколько изменяется позиция

    x1_change=0
    y1_change=0

    x2_change=0
    y2_change=0


#здесь хранятся позиции квадратиков змейки
    snake_List=[]
    Length_of_snake=1

    snake_List_2=[]
    Length_of_snake_2=1
#еда для змеек
    foodx=round(random.randrange(0,600-10)/10.0)*10.0
    foody=round(random.randrange(0,400-10)/10.0)*10.0

    foodx_2=round(random.randrange(0,600-10)/10.0)*10.0
    foody_2=round(random.randrange(0,400-10)/10.0)*10.0

    while not game_over:

        while game_close==True:
            dis.fill(blue)
            message("HA LOSER! Press A-Play Again or ESC-QUIT",red)
            Your_score(Length_of_snake-1,Length_of_snake_2-1)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_a:
                        gameLoop()
            #кнопки для змейки 1 и 2
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-10
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=10
                    y1_change=0
                elif event.key==pygame.K_UP:
                    x1_change=0
                    y1_change=-10
                elif event.key==pygame.K_DOWN:
                    x1_change=0
                    y1_change=10
                #начало создания кнопок для второй змейки
                elif event.key==pygame.K_a:
                    x2_change=-10
                    y2_change=0
                elif event.key==pygame.K_d:
                    x2_change=10
                    y2_change=0
                elif event.key==pygame.K_w:
                    x2_change=0
                    y2_change=-10
                elif event.key==pygame.K_s:
                    x2_change=0
                    y2_change=10
                
#при столкновении змеек игра заканчивается для змейки 1
        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close=True
        if x2>=dis_width or x2<0 or y2>=dis_height or y2<0:
            game_close=True
        #изменение координат змейки
        x1+=x1_change
        y1+=y1_change

        x2+=x2_change
        y2+=y2_change

        dis.fill(blue)
        pygame.draw.rect(dis,red,[foodx,foody,10,10])
        
        #координаты змейки 1 сохраняются в массиве
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        #координаты змейки 1 сохраняются в массиве
        snake_Head_2=[]
        snake_Head_2.append(x2)
        snake_Head_2.append(y2)
        snake_List_2.append(snake_Head_2)


        #чтобы все части змейки двигались одновременно
        if len(snake_List)>Length_of_snake:
            del snake_List[0]

        if len(snake_List_2)>Length_of_snake_2:
            del snake_List_2[0]
        #если змейка скушала саму себя то конец игры
        for x in snake_List[:-1]:# координаты проверяются с конца
            if x==snake_Head:
                game_close=True

        for x in snake_List_2[:-1]:
            if x==snake_Head_2:
                game_close=True
        #рисует мою змейку1
        our_snake(10, snake_List)
        Your_score(Length_of_snake-1, Length_of_snake_2-1)

        snake_2(10,snake_List_2)
        

        pygame.display.update()
        #проверка скушала ли змейку еду
        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0, dis_width-10)/10.0)*10.0
            foody=round(random.randrange(0, dis_height-10)/10.0)*10.0
            Length_of_snake+=1
        
        if x2==foodx and y2==foody:
            foodx=round(random.randrange(0,dis_width-10)/10.0)*10.0
            foody=round(random.randrange(0,dis_height-10)/10.0)*10.0
            Length_of_snake_2+=1

        clock.tick(snake_speed)
    pygame.quit()
    quit()

gameLoop()


