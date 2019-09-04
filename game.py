import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('the game')

WalkRight=[pygame.image.load("R1.png"),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
WalkLeft=[pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
bg=pygame.image.load('bg.jpg')
char=pygame.image.load('standing.png')

clock=pygame.time.Clock()

x=40
y=425
width=64
height=64
vel=5
isJump=False
JumpCount=10
Left=False
Right=False
WalCount=0

def redraw():
    global WalkCount
    win.blit(bg,(0,0))
    if WalkCount+1==27:
        WalkCount=0
    if Left:
        win.blit(WalkLeft[WalkCount//3],(x,y))
        WalkCount+=1
    elif Right:
        win.blit(WalkRight[Walkcount//3],(x,y))
        WalkCount+=1
    else:
        win.blit(char,(x,y))
        WalkCount=0
    pygame.display.update()

run=True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>vel:
        x-=vel
        Left=True
        Right=False
    elif keys[pygame.K_RIGHT] and x<500-width-vel:
        x+=vel
        Right=True
        Left=False
    else:
        Right=False
        Left=False
        WalkCount=0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump=True
            Right=False
            Left=False
            WalkCount=0
    else:
        if JumpCount>=-10:
            neg=-1
            if JumpCount<0:
                neg=1
            y-=(JumpCount**2)*0.5*neg
            JampCount-=1
        else:
            isJump=False
            JumpCount=10

pygame.quit()
        



