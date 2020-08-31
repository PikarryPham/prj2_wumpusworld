
import pygame

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BRK = (134, 163, 158)
BLUE = (51,82,255)

WIDTH = 60
HEIGHT = 60
MARGIN = 0
#--------------------------ĐIỂM--------------------------------------------------

font = pygame.font.Font('freesansbold.ttf',25)
def ShowScore(x , y , score_value ,screen ) :
    score = font.render("SCORE"+": " + str(score_value), True,(255,255,255))
    screen.blit(score,(x,y))
#-------------------------------


f = open("input.txt","r")
data = f.read()
f.close();
data =[data.split("\n")]
list =[[]]
for i in range(1,11,1) :
    temp = str(data[0][i])

    k = temp.split('.')
    list.append(k)

print(list[10][:])

Height = 750
Width  = 700
gameDisplay = pygame.display.set_mode((Width,Height))
pygame.display.set_caption('GAME SPRITE')


B =  pygame.image.load('B.png').convert_alpha()
BG = pygame.image.load('BG.png').convert_alpha()
BGS = pygame.image.load('BGS.png').convert_alpha()
notBrick = pygame.image.load('brickNotVisible.png').convert_alpha()
brick = pygame.image.load('brickVisible.png').convert_alpha()
BS = pygame.image.load('BS.png').convert_alpha()
agentFront = pygame.image.load('front.png').convert_alpha()
agentLeft = pygame.image.load('left.png').convert_alpha()
agentRight = pygame.image.load('right.png').convert_alpha()
agentBack = pygame.image.load('back.png').convert_alpha()
G = pygame.image.load('G.png').convert_alpha()
GS = pygame.image.load('BS.png').convert_alpha()
P  = pygame.image.load('P.png').convert_alpha()
S = pygame.image.load('S.png').convert_alpha()
W =  pygame.image.load('W.png').convert_alpha()

B = pygame.transform.scale(B, (40, 40))
BG = pygame.transform.scale(BG, (40, 40))
BGS = pygame.transform.scale(BGS, (40, 40))
notBrick = pygame.transform.scale(notBrick, (60, 60))
brick = pygame.transform.scale(brick, (60, 60))
BS = pygame.transform.scale(BS, (40, 40))
agentFront = pygame.transform.scale(agentFront, (60, 60))
agentLeft = pygame.transform.scale(agentLeft, (60, 60))
agentRight = pygame.transform.scale(agentRight, (60, 60))
agentBack = pygame.transform.scale(agentBack, (60, 60))
G = pygame.transform.scale(G, (40, 40))
GS = pygame.transform.scale(GS, (40, 40))
P = pygame.transform.scale(P, (40, 40))
S = pygame.transform.scale(S, (40, 40))
W = pygame.transform.scale(W, (40, 40))

startX =0
startY =0
flag = 0
for i in range(1, 11 , 1) :
    for j in range(0,10,1) :
        if list[i][j] =='A' :
            flag = 1
            startX = i
            startY = j
            break
    if flag :
        break

dir = 0

crashed = True
clock = pygame.time.Clock()
countR = 0
countL = 0
countD = 0
countU = 0
MAP =[[0]*30 for i in range(30)]
MAP[0][0] = 1
print(MAP)
flag = 0
while  crashed :

    gameDisplay.fill(BRK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            list[row][column] = '4'
            print("Click ", pos, "Grid coordinates: ", row, column)
    print("X = " , startX , " Y= " , startY)

    ShowScore(2*(HEIGHT + MARGIN) + MARGIN,12*(WIDTH+MARGIN)+ MARGIN ,0,gameDisplay)
    for row in range(1,11,1) :
        for colums in  range(0,10,1):
            if MAP[row][colums] == 0 :
                Brickx = (MARGIN + WIDTH) * colums + MARGIN
                Bricky = (MARGIN + HEIGHT) * row + MARGIN
                gameDisplay.blit(notBrick, (Brickx, Bricky))
            else:
                if list[row][colums] == 'B':
                    Bx = (MARGIN + WIDTH) * colums + MARGIN
                    By = (MARGIN + HEIGHT) * row + MARGIN
                    gameDisplay.blit(B, (Bx, By))
                elif list[row][colums] == 'BG':
                    BGx = (MARGIN + WIDTH) * colums + MARGIN
                    BGy = (MARGIN + HEIGHT) * row + MARGIN
                    gameDisplay.blit(BG, (BGx, BGy))
                elif list[row][colums] == 'BGS':
                    BGSx = (MARGIN + WIDTH) * colums + MARGIN
                    BGSy = (MARGIN + HEIGHT) * row + MARGIN
                    gameDisplay.blit(BGS, (BGSx, BGSy))
                elif list[row][colums] == 'BS':
                    BSx = (MARGIN + WIDTH) * colums + MARGIN
                    BSy = (MARGIN + HEIGHT) * row + MARGIN
                    gameDisplay.blit(BS, (BSx, BSy))
                elif list[row][colums] == 'G':
                    Gx = (MARGIN + WIDTH) * colums + MARGIN
                    Gy = (MARGIN + HEIGHT) * row + MARGIN
                    gameDisplay.blit(G, (Gx, Gy))
                elif list[row][colums] == 'GS':
                    GSx = (MARGIN + WIDTH) * colums + MARGIN
                    GSy = (MARGIN + HEIGHT) * row + MARGIN
                    gameDisplay.blit(GS, (GSx, GSy))
                elif list[row][colums] == 'P':
                    Px = (MARGIN + WIDTH) * colums + MARGIN
                    Py = (MARGIN + HEIGHT) * row + MARGIN
                    gameDisplay.blit(P, (Px, Py))
                elif list[row][colums] == 'S':
                    Sx = (MARGIN + WIDTH) * colums + MARGIN
                    Sy = (MARGIN + HEIGHT) * row + MARGIN
                    gameDisplay.blit(S, (Sx, Sy))
                elif list[row][colums] == 'W':
                    Wx = (MARGIN + WIDTH) * colums + MARGIN
                    Wy = (MARGIN + HEIGHT) * row + MARGIN
                    gameDisplay.blit(W, (Wx, Wy))

    if flag == 1 :
        continue
    if startY  <= 9 and startX == 1 :
        agentX = (MARGIN + WIDTH) * startY + MARGIN
        agentY = (MARGIN + HEIGHT) * startX + MARGIN
        if list[startX][startY] == 'B':
            Bx = (MARGIN + WIDTH) * startY + MARGIN
            By = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay,BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(B, (Bx, By))
        elif list[startX][startY] == 'BG':
            BGx = (MARGIN + WIDTH) * startY + MARGIN
            BGy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(BG, (BGx, BGy))
        elif list[startX][startY] == 'BGS':
            BGSx = (MARGIN + WIDTH) * startY + MARGIN
            BGSy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(BGS, (BGSx, BGSy))
        elif list[startX][startY] == 'BS':
            BSx = (MARGIN + WIDTH) * startY + MARGIN
            BSy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(BS, (BSx, BSy))
        elif list[startX][startY] == 'G':
            Gx = (MARGIN + WIDTH) * startY + MARGIN
            Gy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(G, (Gx, Gy))
        elif list[startX][startY] == 'GS':
            GSx = (MARGIN + WIDTH) * startY + MARGIN
            GSy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(GS, (GSx, GSy))
        elif list[startX][startY] == 'P':
            Px = (MARGIN + WIDTH) * startY + MARGIN
            Py = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(P, (Px, Py))
        elif list[startX][startY] == 'S':
            Sx = (MARGIN + WIDTH) * startY + MARGIN
            Sy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(S, (Sx, Sy))
        elif list[startX][startY] == 'W':
            Wx = (MARGIN + WIDTH) * startY + MARGIN
            Wy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BLACK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(W, (Wx, Wy))
        gameDisplay.blit(agentRight, (agentX, agentY))
    else:
        startX += 1
        startY =  9
        if startX == 11:
            flag = 1
            rect = pygame.draw.rect(gameDisplay, BLUE, (175, 325, 200, 100))
            gameDisplay.blit(font.render('FINISHED !!!', True, (255, 255, 255)), (190, 360))
            pygame.display.update()
            continue
        if list[startX][startY] == 'B':
            Bx = (MARGIN + WIDTH) * startY + MARGIN
            By = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(B, (Bx, By))
        elif list[startX][startY] == 'BG':
            BGx = (MARGIN + WIDTH) * startY + MARGIN
            BGy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(BG, (BGx, BGy))
        elif list[startX][startY] == 'BGS':
            BGSx = (MARGIN + WIDTH) * startY + MARGIN
            BGSy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(BGS, (BGSx, BGSy))
        elif list[startX][startY] == 'BS':
            BSx = (MARGIN + WIDTH) * startY + MARGIN
            BSy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(BS, (BSx, BSy))
        elif list[startX][startY] == 'G':
            Gx = (MARGIN + WIDTH) * startY + MARGIN
            Gy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(G, (Gx, Gy))
        elif list[startX][startY] == 'GS':
            GSx = (MARGIN + WIDTH) * startY + MARGIN
            GSy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(GS, (GSx, GSy))
        elif list[startX][startY] == 'P':
            Px = (MARGIN + WIDTH) * startY + MARGIN
            Py = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(P, (Px, Py))
        elif list[startX][startY] == 'S':
            Sx = (MARGIN + WIDTH) * startY + MARGIN
            Sy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(S, (Sx, Sy))
        elif list[startX][startY] == 'W':
            Wx = (MARGIN + WIDTH) * startY + MARGIN
            Wy = (MARGIN + HEIGHT) * startX + MARGIN
            pygame.draw.rect(gameDisplay, BRK, [(MARGIN + WIDTH) * startY + MARGIN,
                                                  (MARGIN + HEIGHT) * startX + MARGIN,
                                                  WIDTH,
                                                  HEIGHT
                                                  ])
            gameDisplay.blit(W, (Wx, Wy))

        agentX = (MARGIN + WIDTH) * startY + MARGIN
        agentY = (MARGIN + HEIGHT) * startX + MARGIN
        gameDisplay.blit(agentFront, (agentX, agentY))
    MAP[startX][startY] = 1

    startY += 1

    pygame.display.update()
    clock.tick(60)
    pygame.time.wait(500)
pygame.quit()
quit()