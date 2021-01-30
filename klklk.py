import random

import pygame
m=60
pygame.init()
time=150
screen=pygame.display.set_mode([500,500])
b=0
o=random.randint(0,12)*40
x=40
oo=random.randint(0,12)*40
y=40
score=0
caesar=True
ba=0
ca=00
n=0
k=1
kl=0
k0=0
k1=0
k2=0
k3=0
k4=0
r1=0
go=True
body = pygame.image.load("IMG_0043.png")
stop1=False
stop2=False
stop3=False
stop4=False
inter1=[0,0]
inter2=[0,0]
inter3=[0,0]
inter4=[0,0]
ix=[]
iy=[]
push1=-1
push2=-1
push3=-1
push4=-1
recode1=-1
recode11=-1
recode22=-1
recode33=-1
recode44=-1
stop11=False
stop22=False
stop33=False
stop44=False
recode2=-1
recode3=-1
recode4=-1
direction=0
def check():

    global inter1,inter2,inter3,inter4,push1,push2,push3,push4, k1,k2,k3,k4,stop1,stop2,stop3,stop4,recode1,recode2,recode3,recode4,recode11,recode22,recode33,recode44,stop11,stop22,stop33,stop44,stop55
    for iii in range(0, len(ix)):
        if (y == ix[iii][1] + 40 and x == ix[iii][0]):
            k1 = True
            inter1=ix[iii]
            push1=iii
        elif (y == ix[iii][1] - 40 and x == ix[iii][0]):
            inter2=ix[iii]
            k2 = True
            push2=iii
        elif (y == ix[iii][1] and x == ix[iii][0] - 40):
            inter3=ix[iii]
            k3 = True
            push3=iii
        elif (y == ix[iii][1] and x == ix[iii][0] + 40):
            inter4=ix[iii]
            k4 = True
            push4=iii

    for inter in range(0,len(ix)):
        if push1>=0:
            if ix[push1][1]==ix[inter][1]+40 and ix[push1][0]==ix[inter][0] or ix[push1][1]==o+40 and ix[push1][0]==oo:
                stop1=True
                recode1=ix[push1][1]
                recode11=ix[push1][0]
                print("6")
        if push2>=0:
            if ix[push2][1] == ix[inter][1] - 40 and ix[push2][0] == ix[inter][0]  or ix[push2][1] == o-40 and ix[push2][0] ==oo:
                stop2 = True
                recode2=ix[push2][1]
                recode22=ix[push2][0]
        if push3 >= 0:
            if ix[push3][0] == ix[inter][0] - 40 and ix[push3][1] == ix[inter][1]  or ix[push3][0] ==oo-40 and ix[push3][1] ==o:
                stop3 = True
                recode3=ix[push3][0]
                recode33=ix[push3][1]
        if push4 >= 0:
            if ix[push4][0] == ix[inter][0] + 40 and ix[push4][1] == ix[inter][1]  or ix[push4][0] == oo+40 and ix[push4][1] == o:
                stop4 = True
                recode4=ix[push4][0]
                recode44=ix[push4][1]
        if o==ix[inter][1]+40 and oo==ix[inter][0] and kl==1:
            stop11 = True
            recode1 = ix[inter][1] + 40
            recode11=ix[inter][0]
            print("1")
        if o== ix[inter][1] - 40 and oo == ix[inter][0] and kl==2:
            stop22 = True
            recode2 =  ix[inter][1] - 40
            recode22=ix[inter][0]
            print("2")
        if oo == ix[inter][0] - 40 and o == ix[inter][1] and kl==3:
            stop33 = True
            recode3 = ix[inter][0] - 40
            recode33=ix[inter][1]
            print("3")
        if oo == ix[inter][0] + 40 and o == ix[inter][1] and kl==4:
            stop44 = True
            recode4 = ix[inter][0] + 40
            recode44=ix[inter][1]
            print("4")
    if o !=recode1 or oo != recode11 :
        stop11=False
        print("error")
    if o != recode2 or oo !=recode22 :
        stop22=False
        print("?")
    if oo != recode3 or o != recode33:
        stop33=False
    if oo!=recode4 or o!=recode44 :
        stop44=False
    if push1 >= 0:

        if recode1!=y-40 or recode11!=x :
            stop1=False
            print("5")
    if push2 >= 0:
        print(ix[push2])
        if recode2!=y+40 or recode22!=x:
            stop2=False
    if push3 >= 0:
        if recode3!=x+40 or recode33!=y:
            stop3=False
    if push4 >= 0:
        if recode4!=x-40  or recode44!=y:
            stop4=False
    if inter1[1]+40!=y or inter1[0]!=x:
        k1=False

    if inter2[1]-40!=y or inter2[0]!=x:
        k2=False
    if inter3[1]!=y or inter3[0]!=x+40:
        k3=False
    if inter4[1]!=y or inter4[0]!=x-40:
        k4=False

def replace():
    global o,oo
    kp=0
    [oo,o]=[random.randint(0,12)*40,random.randint(0,12)*40]
    for z in range(0, len(ix)):
        if ix[z] ==[oo,o]  or [oo,o] == [240, 120] or [oo,o] == [x, y] :
            kp = 1
    if kp == 1:


        replace()
def makeinterrupt():
    d = [random.randint(0, 12) * 40, random.randint(0, 12) * 40]
    e = 0
    for z in range(0, len(ix)):
        if ix[z] == d or d==[240,120] or d==[x,y] or d==[oo,o]:
            e = 1
    if e == 0:
        ix.append(d)
    else:
        makeinterrupt()
for make in range(0,m):
    makeinterrupt()

def drawCircle(size,c,p):
    pygame.draw.circle(screen,c,p,size)
def showMessage(text,size,colour,p):
    fon=pygame.font.Font(None,size)
    sur=fon.render(text,True,colour)
    screen.blit(sur,p)

def drawRectangular(p,size,c):
    pygame.draw.rect(screen,c,p,size)
hh=0

fps=100

kkk=pygame.time.Clock()
running=True

while running:
    r1=0
    if hh == 0:
        screen.fill((0, 0, 0))

        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                running=False
            #if i.type==pygame.MOUSEBUTTONDOWN:
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_w:
                    body = pygame.image.load("IMG_0043.png")
                    direction=1
                    if k1==True or kl==1:
                        y=y-0

                    else:
                        y=y-40
                if i.key == pygame.K_a:
                    body = pygame.image.load("IMG_0044.png")
                    direction=4
                    if k4==True or kl==4:
                        x=x-0

                    else:
                        x = x - 40
                if i.key == pygame.K_d:
                    body = pygame.image.load("IMG_0046.png")
                    direction=3
                    if k3==True or kl==3:
                        x=x+0

                    else:
                        x = x + 40
                if i.key == pygame.K_s:
                    direction=2
                    body = pygame.image.load("IMG_0045.png")
                    if k2==True or kl==2:
                        y=y+0

                    else:
                        y = y + 40
                if i.key==pygame.K_q:
                    if k0==True:
                        o=o

                    elif kl==1 and direction==1 and stop11==False:
                        o=o-40
                    elif kl==2 and direction==2 and stop22==False:
                        o=o+40
                    elif kl==3 and direction==3 and stop33==False:
                        oo=oo+40
                    elif kl==4 and direction==4 and stop44==False:
                        oo=oo-40
                    if k1==True and direction==1 and stop1==False:
                        ix[push1][1]-=40
                    elif k2==True and direction==2 and stop2==False:
                        ix[push2][1]+=40
                    elif k3==True and direction==3 and stop3==False:
                        ix[push3][0]+=40
                    elif k4==True and direction==4 and stop4==False:
                        ix[push4][0]-=40
        hole = drawCircle(20, (255, 50, 255), [240, 120])

        bodysize=pygame.transform.scale(body,(40,40))
        bodyxy = bodysize.get_rect(center=(x,y))
        screen.blit(bodysize, bodyxy)
        aaaa=drawCircle(20, (255, 0, 0), [oo, o])
        for make in range(0,m):

            drawCircle(20, (25, 100, 255), ix[make])
        showMessage("time="+str(time), 30, (0, 255, 29), [20, 20])
        showMessage("score= " + str(score), 30, (255, 255, 0), [400, 20])
        if (y == o + 40 and x == oo):
            kl=1
        elif (y == o - 40 and x == oo):
            kl=2
        elif (x == oo - 40 and y == o):
            kl=3
        elif (x == oo + 40 and y == o) :
            kl=4
        else:
            kl=0

        check()

        if oo==240 and o==120:
            replace()
            score=score+1
        if time==0:
            hh=1
    else:
        screen.fill((254, 254, 254))
        showMessage("score= "+str(score),30,(255,0,0),[150,150])
        showMessage("good game", 30, (255, 0, 0), [150, 200])
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                running=False
    kkk.tick(fps)

    b = b + 1
    if b %100==0:
        time=time-1
    if n == 430:
            k = 0
    if k == 0:
            n = n - 1
    if k == 1:
            n = n + 1
    if n == 0:
            k = 1



    pygame.display.flip()

pygame.quit()