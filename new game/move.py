#球和边框的尺寸皆为50*50 4行4列 则屏幕大小为200*200
import pygame
import sys
import traceback
from pygame.locals import *
from random import *

#定义边框类
class Glass(pygame.sprite.Sprite):
    def __init__(self,glass_image,position,line,column,level):
        pygame.sprite.Sprite.__init__(self)
        self.glass_image = pygame.image.load(glass_image).convert()
        self.rect = self.glass_image.get_rect()
        self.rect.left,self.rect.top = position
        self.line = line
        self.column = column
        self.possess = False
        self.level = level

class Ball(pygame.sprite.Sprite):
    def __init__(self,ball_image,position,line,column,level):
        pygame.sprite.Sprite.__init__(self)
        self.ball_image = pygame.image.load(ball_image).convert_alpha()
        self.rect = self.ball_image.get_rect()
        self.rect.left,self.rect.top = position
        self.line = line
        self.column = column
        self.level = level
       
        
def main():
    #初始化pygame和混音器
    pygame.init()
    pygame.mixer.init()


    #设定小球图片
    one_ball = '1.png'
    two_ball = '2.png'
    three_ball = '3.png'
    four_ball = '4.png'
    five_ball = '5.png'
    six_ball = '6.png'
    seven_ball = '7.png'
    eight_ball = '8.png'
    nine_ball = '9.png'
    ten_ball = '10.png'
    eleven_ball = '11.png'
    #设定玻璃图片
    glass_image = 'ui.png'

    defeated_image = 'defeated.png'
    win_img = 'win.png'

    #设定游戏界面尺寸
    bg_size = width,height = 200,200
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('移动篮球')
    #使游戏可以开始的标志running
    running = True

    glasses = []
    balls = []

    #创建游戏背景
    for i in range(4):
        for p in range(4):
            position = p*50,i*50
            glass = Glass(glass_image,position,p,i,0)
            glasses.append(glass)

    #显示背景边框
    for each in glasses:
        screen.blit(each.glass_image,each.rect)

    #创建小球
    for i in range(2):
        line = randint(0,3)
        column = randint(0,3)
        for each in balls:
            while line == each.line and column == each.column:
                line = randint(0,3)
                column = randint(0,3)
        position = glasses[line*4+column].rect.left,glasses[line*4+column].rect.top
        glasses[line*4+column].level=1
        ball = Ball(one_ball,position,line,column,1)
        balls.append(ball)
        glasses[line*4+column].possess = True

    #显示小球
    for each in balls:
        screen.blit(each.ball_image,each.rect)    

    while running:
        for each in glasses:
            if len(balls) == 16:
                pygame.time.delay(3000)
                lose = pygame.image.load('defeated.png').convert_alpha()
                screen.blit(lose,(width - lose.get_width()//2,height - lose.get_height()//2))
            if each.level == 11:
                pygame.time.delay(3000)
                win = pygame.image.load('win.png').convert.alpha()
                screen.blit(win,(width - win.get_width()//2,height - win.get_height()//2))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
    


                #w键向上
                if event.key == K_w:
                    for each in balls:
                        #判断等级是否一样的标志rank
                        rank = False
                        screen.blit(glasses[0].glass_image,(each.rect.left,each.rect.top))
                        for i in range(each.line):
                            if each.line != 0:
                                glasses[each.line*4+each.column].possess = False
                                if not glasses[(each.line-1)*4+each.column].possess:
                                    each.line = each.line-1
                                    each.rect.top = (each.line)*50
                                    glasses[each.line*4+each.column].possess = True
                                    glasses[each.line*4+each.column].level = each.level                             
                                else:
                                    if glasses[each.line*4+each.column].level == glasses[(each.line-1)*4+each.column].level:
                                        rank = True
                                        glasses[(each.line-1)*4+each.column].level = glasses[(each.line-1)*4+each.column].level + 1
                                        screen.blit(glasses[0].glass_image,(each.rect.left,each.rect.top))
                                        if glasses[(each.line-1)*4+each.column].level == 1:
                                            picture = one_ball
                                        if glasses[(each.line-1)*4+each.column].level == 2:
                                            picture = two_ball
                                        if glasses[(each.line-1)*4+each.column].level == 3:
                                            picture = three_ball
                                        if glasses[(each.line-1)*4+each.column].level == 4:
                                            picture = four_ball
                                        if glasses[(each.line-1)*4+each.column].level == 5:
                                            picture = five_ball
                                        if glasses[(each.line-1)*4+each.column].level == 6:
                                            picture = six_ball
                                        if glasses[(each.line-1)*4+each.column].level == 7:
                                            picture = seven_ball
                                        if glasses[(each.line-1)*4+each.column].level == 8:
                                            picture = eight_ball
                                        if glasses[(each.line-1)*4+each.column].level == 9:
                                            picture = nine_ball
                                        if glasses[(each.line-1)*4+each.column].level == 10:
                                            picture = ten_ball
                                        if glasses[(each.line-1)*4+each.column].level == 11:
                                            picture = eleven_ball
                                        ball = Ball(picture,(glasses[(each.line-1)*4+each.column].rect.left,glasses[(each.line-1)*4+each.column].rect.top),each.line-1,each.column,glasses[(each.line-1)*4+each.column].level)
                                        balls.append(ball)
                                        balls.remove(each)
                                    else:
                                        glasses[each.line*4+each.column].possess = True
                                        glasses[each.line*4+each.column].level = each.level

                                    break
                        if not rank:
                            screen.blit(each.ball_image,(each.rect.left,each.rect.top))

                        if rank:
                            screen.blit(ball.ball_image,(ball.rect.left,ball.rect.top))

                    #先进行移动 移动之后再创建新球
                    line = randint(0,3)
                    column = randint(0,3)
                    for each in balls:
                        while line == each.line and column == each.column:
                            line = randint(0,3)
                            column = randint(0,3)
                    position = glasses[line*4+column].rect.left,glasses[line*4+column].rect.top
                    ball = Ball(one_ball,position,line,column,1)
                    balls.append(ball)
                    glasses[line*4+column].possess = True
                    glasses[line*4+column].level = 1
                    screen.blit(ball.ball_image,(ball.rect.left,ball.rect.top))

                #s键向下
                if event.key == K_s:
                    for each in balls:
                        #判断等级是否一样的标志rank
                        rank = False
                        screen.blit(glasses[0].glass_image,(each.rect.left,each.rect.top))
                        if each.line != 3:
                            for i in range(3-each.line):
                                glasses[each.line*4+each.column].possess = False
                                if not glasses[(each.line+1)*4+each.column].possess:
                                    each.line = each.line+1
                                    each.rect.top = (each.line)*50
                                    glasses[each.line*4+each.column].possess = True
                                    glasses[each.line*4+each.column].level = each.level
                                else:
                                    if glasses[each.line*4+each.column].level == glasses[(each.line+1)*4+each.column].level:                                       
                                        rank = True
                                        glasses[(each.line+1)*4+each.column].level = glasses[(each.line+1)*4+each.column].level + 1
                                        screen.blit(glasses[0].glass_image,(each.rect.left,each.rect.top))
                                        if glasses[(each.line+1)*4+each.column].level == 1:
                                            picture = one_ball
                                        if glasses[(each.line+1)*4+each.column].level == 2:
                                            picture = two_ball
                                        if glasses[(each.line+1)*4+each.column].level == 3:
                                            picture = three_ball
                                        if glasses[(each.line+1)*4+each.column].level == 4:
                                            picture = four_ball
                                        if glasses[(each.line+1)*4+each.column].level == 5:
                                            picture = five_ball
                                        if glasses[(each.line+1)*4+each.column].level == 6:
                                            picture = six_ball
                                        if glasses[(each.line+1)*4+each.column].level == 7:
                                            picture = seven_ball
                                        if glasses[(each.line+1)*4+each.column].level == 8:
                                            picture = eight_ball
                                        if glasses[(each.line+1)*4+each.column].level == 9:
                                            picture = nine_ball
                                        if glasses[(each.line+1)*4+each.column].level == 10:
                                            picture = ten_ball
                                        if glasses[(each.line+1)*4+each.column].level == 11:
                                            picture = eleven_ball
                                        ball = Ball(picture,(glasses[(each.line+1)*4+each.column].rect.left,glasses[(each.line+1)*4+each.column].rect.top),each.line+1,each.column,glasses[(each.line-1)*4+each.column].level)
                                        balls.append(ball)
                                        balls.remove(each)
                                    else:
                                        glasses[each.line*4+each.column].possess = True
                                        glasses[each.line*4+each.column].level = each.level
                                    break
                        if not rank:
                            screen.blit(each.ball_image,(each.rect.left,each.rect.top))

                        if rank:
                            screen.blit(ball.ball_image,(ball.rect.left,ball.rect.top))

                        elif each.line == 3:
                            pass

                    #先进行移动 移动之后再创建新球
                    line = randint(0,3)
                    column = randint(0,3)
                    for each in balls:
                        while line == each.line and column == each.column:
                            line = randint(0,3)
                            column = randint(0,3)
                    position = glasses[line*4+column].rect.left,glasses[line*4+column].rect.top
                    ball = Ball(one_ball,position,line,column,1)
                    balls.append(ball)
                    glasses[line*4+column].possess = True
                    glasses[line*4+column].level = 1
                    screen.blit(ball.ball_image,(ball.rect.left,ball.rect.top))
                    
                        

                #a键向左
                if event.key == K_a:
                    for each in balls:
                        #判断等级是否一样的标志rank
                        rank = False
                        screen.blit(glasses[0].glass_image,(each.rect.left,each.rect.top))
                        for i in range(each.column):
                            if each.column != 0:
                                glasses[each.line*4+each.column].possess = False
                                if not glasses[each.line*4+each.column-1].possess:
                                    each.column = each.column-1
                                    each.rect.left = (each.column)*50
                                    glasses[each.line*4+each.column].possess = True
                                    glasses[each.line*4+each.column].level = each.level                             
                                else:
                                    if glasses[each.line*4+each.column].level == glasses[each.line*4+each.column-1].level:
                                        rank = True
                                        glasses[each.line*4+each.column-1].level = glasses[each.line*4+each.column-1].level + 1
                                        screen.blit(glasses[0].glass_image,(each.rect.left,each.rect.top))
                                        if glasses[each.line*4+each.column-1].level == 1:
                                            picture = one_ball
                                        if glasses[each.line*4+each.column-1].level == 2:
                                            picture = two_ball
                                        if glasses[each.line*4+each.column-1].level == 3:
                                            picture = three_ball
                                        if glasses[each.line*4+each.column-1].level == 4:
                                            picture = four_ball
                                        if glasses[each.line*4+each.column-1].level == 5:
                                            picture = five_ball
                                        if glasses[each.line*4+each.column-1].level == 6:
                                            picture = six_ball
                                        if glasses[each.line*4+each.column-1].level == 7:
                                            picture = seven_ball
                                        if glasses[each.line*4+each.column-1].level == 8:
                                            picture = eight_ball
                                        if glasses[each.line*4+each.column-1].level == 9:
                                            picture = nine_ball
                                        if glasses[each.line*4+each.column-1].level == 10:
                                            picture = ten_ball
                                        if glasses[each.line*4+each.column-1].level == 11:
                                            picture = eleven_ball
                                        ball = Ball(picture,(glasses[each.line*4+each.column-1].rect.left,glasses[each.line*4+each.column-1].rect.top),each.line,each.column-1,glasses[each.line*4+each.column-1].level)
                                        balls.append(ball)
                                        balls.remove(each)
                                    else:
                                        glasses[each.line*4+each.column].possess = True
                                        glasses[each.line*4+each.column].level = each.level

                                    break
                        if not rank:
                            screen.blit(each.ball_image,(each.rect.left,each.rect.top))

                        if rank:
                            screen.blit(ball.ball_image,(ball.rect.left,ball.rect.top))

                    #先进行移动 移动之后再创建新球
                    line = randint(0,3)
                    column = randint(0,3)
                    for each in balls:
                        while line == each.line and column == each.column:
                            line = randint(0,3)
                            column = randint(0,3)
                    position = glasses[line*4+column].rect.left,glasses[line*4+column].rect.top
                    ball = Ball(one_ball,position,line,column,1)
                    balls.append(ball)
                    glasses[line*4+column].possess = True
                    glasses[line*4+column].level = 1
                    screen.blit(ball.ball_image,(ball.rect.left,ball.rect.top))


                 #d键向右
                if event.key == K_d:
                    for each in balls:
                        #判断等级是否一样的标志rank
                        rank = False
                        screen.blit(glasses[0].glass_image,(each.rect.left,each.rect.top))
                        if each.column != 3:
                            for i in range(3-each.column):
                                glasses[each.line*4+each.column].possess = False
                                if not glasses[each.line*4+each.column+1].possess:
                                    each.column = each.column+1
                                    each.rect.left = (each.column)*50
                                    glasses[each.line*4+each.column].possess = True
                                    glasses[each.line*4+each.column].level = each.level
                                else:
                                    if glasses[each.line*4+each.column].level == glasses[each.line*4+each.column+1].level:                                       
                                        rank = True
                                        glasses[each.line*4+each.column+1].level = glasses[each.line*4+each.column+1].level + 1
                                        screen.blit(glasses[0].glass_image,(each.rect.left,each.rect.top))
                                        if glasses[each.line*4+each.column+1].level == 1:
                                            picture = one_ball
                                        if glasses[each.line*4+each.column+1].level == 2:
                                            picture = two_ball
                                        if glasses[each.line*4+each.column+1].level == 3:
                                            picture = three_ball
                                        if glasses[each.line*4+each.column+1].level == 4:
                                            picture = four_ball
                                        if glasses[each.line*4+each.column+1].level == 5:
                                            picture = five_ball
                                        if glasses[each.line*4+each.column+1].level == 6:
                                            picture = six_ball
                                        if glasses[each.line*4+each.column+1].level == 7:
                                            picture = seven_ball
                                        if glasses[each.line*4+each.column+1].level == 8:
                                            picture = eight_ball
                                        if glasses[each.line*4+each.column+1].level == 9:
                                            picture = nine_ball
                                        if glasses[each.line*4+each.column+1].level == 10:
                                            picture = ten_ball
                                        if glasses[each.line*4+each.column+1].level == 11:
                                            picture = eleven_ball
                                        ball = Ball(picture,(glasses[each.line*4+each.column+1].rect.left,glasses[each.line*4+each.column+1].rect.top),each.line,each.column+1,glasses[each.line*4+each.column+1].level)
                                        balls.append(ball)
                                        balls.remove(each)
                                    else:
                                        glasses[each.line*4+each.column].possess = True
                                        glasses[each.line*4+each.column].level = each.level
                                    break
                        if not rank:
                            screen.blit(each.ball_image,(each.rect.left,each.rect.top))

                        if rank:
                            screen.blit(ball.ball_image,(ball.rect.left,ball.rect.top))

                        elif each.line == 3:
                            pass

                    #先进行移动 移动之后再创建新球
                    line = randint(0,3)
                    column = randint(0,3)
                    for each in balls:
                        while line == each.line and column == each.column:
                            line = randint(0,3)
                            column = randint(0,3)
                    position = glasses[line*4+column].rect.left,glasses[line*4+column].rect.top
                    ball = Ball(one_ball,position,line,column,1)
                    balls.append(ball)
                    glasses[line*4+column].possess = True
                    glasses[line*4+column].level = 1
                    screen.blit(ball.ball_image,(ball.rect.left,ball.rect.top))
                        
                                
    
        pygame.display.flip()

        

#执行主程序
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()

