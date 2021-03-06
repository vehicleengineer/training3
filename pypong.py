import pygame,sys
#定义小球的属性和方法
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"F:\code\py\trash\PyPong\wackyball.bmp")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        global points, score_text
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]

        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            points += 1
            score_text = font.render(str(points), 1 , (0, 0 ,0))
#用黑色矩形块表示球拍
class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self,location=[0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,20])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert() #将屏幕转化为图像
        self.rect = self.image.get_rect()
        self.rect.left , self.rect.top = location

pygame.init()
screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
myBall = MyBallClass([10,5],[50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270,400])
lives = 3
points = 0

font = pygame.font.Font(None, 50)       #font函数创建字体对象显示分数
score_text = font.render(str(points), 1 ,(0, 0 , 0))     #渲染文字
textpos = [10,10]                     #设置文字位置
done = False

while 1:                                     #输入事件MOUSEMOTION，paddle随鼠标移动
    clock.tick(30)
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]
        
    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        myBall.speed[1] = -myBall.speed[1]
    myBall.move()

    if not done:
        screen.blit(myBall.image, myBall.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_text, textpos)
        for i in range(lives):
            width = screen.get_width()
            screen.blit(myBall.image, [width -40*i, 20])
        pygame.display.flip()

    if myBall.rect.top >= screen.get_rect().bottom:
        lives = lives -1

        if lives == 0:
            final_text1 = "Game Over"
            final_text2 = "Your final score is: " + str(points)
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = font.render(final_text1, 1, (0, 0, 0))
            ft2_font = pygame.font.Font(None, 50)
            ft2_surf = font.render(final_text2,1,(0,0,0))
            screen.blit(ft1_surf, [screen.get_width()/2 - ft1_surf.get_width()/2, 100])
            screen.blit(ft2_surf, [screen.get_width()/2 - ft2_surf.get_width()/2, 200])
            pygame.display.flip()
            done =True
        else:
            pygame.time.delay(2000)
            myBall.rect.topleft = [50,50]