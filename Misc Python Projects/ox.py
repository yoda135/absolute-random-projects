import pygame
from playsound import playsound

def in_position(x, y):

    res = -1

    #print(x,y)

    if y > 150 and y < 250:
        if x > 250 and x < 350:
            return 0
        elif x > 350 and x < 450:
            return 1
        elif x > 450 and x < 550:
            return 2
    elif y > 250 and y < 350:
        if x > 250 and x < 350:
            return 3
        elif x > 350 and x < 450:
            return 4
        elif x > 450 and x < 550:
            return 5
    elif y > 350 and y < 450:
        if x > 250 and x < 350:
            return 6
        elif x > 350 and x < 450:
            return 7
        elif x > 450 and x < 550:
            return 8    
    return res

def draw_naught(Position):

    x = 0
    y = 0

    if Position == 0:
        x = 300
        y = 200
    elif Position == 1:
        x = 400
        y = 200
    elif Position == 2:
        x = 500
        y = 200
    elif Position == 3:
        x = 300
        y = 300
    elif Position == 4:
        x = 400
        y = 300
    elif Position == 5:
        x = 500
        y = 300
    elif Position == 6:
        x = 300
        y = 400
    elif Position == 7:
        x = 400
        y = 400
    elif Position == 8:
        x = 500
        y = 400
    pygame.draw.circle(gameDisplay, red, (x,y), 35)
    pygame.draw.circle(gameDisplay, white, (x,y), 25)    

def draw_cross(Position):

    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    
    if Position == 0:
        x1 = 330
        y1 = 230
        x2 = 270
        y2 = 170
    elif Position == 1:
        x1 = 430
        y1 = 230
        x2 = 370
        y2 = 170
    elif Position == 2:
        x1 = 530
        y1 = 230
        x2 = 470
        y2 = 170
    elif Position == 3:
        x1 = 330
        y1 = 330
        x2 = 270
        y2 = 270
    elif Position == 4:
        x1 = 430
        y1 = 330
        x2 = 370
        y2 = 270
    elif Position == 5:
        x1 = 530
        y1 = 330
        x2 = 470
        y2 = 270
    elif Position == 6:
        x1 = 330
        y1 = 430
        x2 = 270
        y2 = 370
    elif Position == 7:
        x1 = 430
        y1 = 430
        x2 = 370
        y2 = 370
    elif Position == 8:
        x1 = 530
        y1 = 430
        x2 = 470
        y2 = 370
        
    pygame.draw.line(gameDisplay, blue, (x1,y1), (x2,y2),15)
    pygame.draw.line(gameDisplay, blue, (x2,y1), (x1,y2),15)


def check_win(Tracker):

    tester = 0
    while tester < 2:

        x = 0
        while x < 9:
            if Tracker[x] == tester and Tracker[x+1] == tester and Tracker[x+2] == tester:
                pygame.draw.line(gameDisplay, light_blue, (250,(200 + (x * 33))), (550,(200 + (x * 33))),5)
                return tester
            x = x + 3
        x = 0    
        while x < 4:
            if Tracker[x] == tester and Tracker[x+3] == tester and Tracker[x+6] == tester:
                pygame.draw.line(gameDisplay, light_blue, (300 + (x * 100),150), (300 + (x * 100),450),5)
                return tester
            x = x + 1

        if Tracker[0] == tester and Tracker[4] == tester and Tracker[8] == tester:
            pygame.draw.line(gameDisplay, light_blue, (250,150), (550,450),5)
            return tester
        if Tracker[2] == tester and Tracker[4] == tester and Tracker[6] == tester:
            pygame.draw.line(gameDisplay, light_blue, (550,150), (250,450),5)

            return tester
        
        tester = tester + 1

    return -1
    

pygame.init()

white = (255,255,255)
black = (0,0,0)
0
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,165,0)
dark_blue = (21, 0, 255)
light_blue = (63, 252, 238)

myfont = pygame.font.SysFont('Comic Sans MS', 30)


while 1:

    gameDisplay = pygame.display.set_mode((800,600))
    gameDisplay.fill(white)

    #pixAr = pygame.PixelArray(gameDisplay)
    #pixAr[10][20] = green

    pygame.draw.line(gameDisplay, black, (350,150), (350,450),10)

    pygame.draw.line(gameDisplay, black, (450,150), (450,450),10)

    pygame.draw.line(gameDisplay, black, (250,250), (550,250),10)

    pygame.draw.line(gameDisplay, black, (250,350), (550,350),10)

    player = 0

    mx = 0
    my = 0
    hitlist = []

    tracker = []
    for i in range(12):
        tracker.append(-1)

    textsurface = myfont.render("O to play", False, orange)
    gameDisplay.blit(textsurface,(0,0))
    gameon = True

    while gameon:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    mx, my = pygame.mouse.get_pos()
                    
                    pos = in_position(mx, my)
                    
                    if pos >= 0 and pos not in hitlist:
                        if player == 0:
                            draw_naught(pos)
                            textsurface = myfont.render("X to play", False, orange)
                            pygame.draw.rect(gameDisplay, white, (0,0,500,80))
                            gameDisplay.blit(textsurface,(0,0))
                            player = 1
                            tracker[pos] = 0

                        else:
                            draw_cross(pos)
                            textsurface = myfont.render("O to play", False, orange)
                            pygame.draw.rect(gameDisplay, white, (0,0,500,80))
                            gameDisplay.blit(textsurface,(0,0))
                            player = 0
                            tracker[pos] = 1

                        hitlist.append(pos)
                        win = check_win(tracker)
                        if win >= 0:
                            winner = "O has won! (Press left click to start again)"
                            if win == 1:
                                winner = "X has won! (Press left click to start again)"
                                
                            textsurface = myfont.render(winner, False, green)
                            pygame.draw.rect(gameDisplay, white, (0,0,500,80))
                            gameDisplay.blit(textsurface,(0,0))
                            playsound('win.wav', False)
                            gameon = False

                        elif len(hitlist) >= 9:
                            textsurface = myfont.render("Game is a TIE! (Press left click to start again)", False, green)
                            pygame.draw.rect(gameDisplay, white, (0,0,500,80))
                            gameDisplay.blit(textsurface,(0,0))
                            playsound('tie.wav', False)
                            gameon = False
 
                        else:
                            playsound('go.wav', False)
                        


        pygame.display.update()

    waitclick = 1

    while waitclick == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    waitclick = 0
                    break
        pygame.display.update()


