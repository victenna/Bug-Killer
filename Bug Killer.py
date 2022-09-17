import pygame,random
from math import *
pygame.init()
screen = pygame.display.set_mode((1024, 900))
#bg = pygame.image.load('bGround.png')
bg = pygame.transform.rotozoom(pygame.image.load('bGround.png'), 0, 1.3)
green = (0, 255, 0)
blue = (0, 0, 128)
clock = pygame.time.Clock()

class Killer(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image=pygame.transform.scale(self.image,(40,80))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    def draw(self):
        screen.blit(self.image,self.rect)
    def shoot(self):
        pygame.sprite.spritecollide(self, bug_group, True)

class Bug(pygame.sprite.Sprite):
    def __init__(self,image,scale):
        super().__init__()
        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image,(scale,scale))
        self.start_image=self.image
        self.rect=self.image.get_rect()
        self.settings()
    def settings(self):
        x=random.randint(100,700)
        y=random.randint(100,700)
        dx=random.randint(-5,5)
        dy=random.randint(-5,5)
        self.x,self.y=x,y
        self.rect.center=(self.x,self.y)
        self.dx,self.dy=dx,dy

    def update(self):
        self.x+=self.dx
        self.y+=self.dy
        if self.x>1150 or self.x<50: self.dx=-self.dx
        if self.y>850 or self.y<50: self.dy=-self.dy
        self.rect.center=(self.x,self.y)
        degree=atan2(-self.dy,self.dx)*180/3.14159-90
        self.image=pygame.transform.rotate(self.start_image,degree)
Q=5
bug_group=pygame.sprite.Group()
killer = Killer('killer.png')
for i in range (Q):
    bug_group.add(Bug('bug1.png',40))

font=pygame.font.Font(None,56)
start_time=pygame.time.get_ticks()

while True:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            killer.shoot()
    killer.update(), killer.draw()
    bug_group.draw(screen)
    bug_group.update()
    if len(bug_group)==0:
        break
    print(len(bug_group))
    Time=(pygame.time.get_ticks()-start_time)//1000
    text=font.render(str(Time),True,(255,255,255))
    screen.blit(text,(800,50))
    pygame.display.update()
    clock.tick(100)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    text3 = font.render('Game Over', True, green, blue)#!!!!!!!!!!!!!!!!!!!!!
    textRect = text3.get_rect()
    textRect.center = (300,800)
    screen.blit(text3, textRect)
    screen.blit(text,(800,50))
    clock.tick(1)
    pygame.display.update()
    




