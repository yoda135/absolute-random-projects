import pygame
from playsound import playsound

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,165,0)
dark_blue = (21, 0, 255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(white)

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green

pygame.draw.line(gameDisplay, black, (400,100), (400,350),10)

pygame.draw.rect(gameDisplay, black, (400,400,50,25))

pygame.draw.circle(gameDisplay, black, (400,50), 50)

pygame.draw.line(gameDisplay, black, (300,150), (500,150),5)

pygame.draw.line(gameDisplay, black, (400,350), (350,400),5)

pygame.draw.line(gameDisplay, black, (400,350), (450,400),5)

#pygame.draw.polygon(gameDisplay, green, ((25,75),(76,125),(250,375),(400,25),(60,540)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        #elif event.type == pygame.MOUSEMOTION:
        #    if event.rel[0] > 0:  # 'rel' is a tuple (x, y). 'rel[0]' is the x-value.
        #        print("You're moving the mouse to the right")
        #    elif event.rel[1] > 0:  # pygame start y=0 at the top of the display, so higher y-values are further down.
        #        print("You're moving the mouse down")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                playsound('Bad guy.mp3', False)
                #print("You pressed the left mouse button")
            elif event.button == 3:
                playsound("dad.wav", False)

    pygame.display.update()
