import pygame
import time

pygame.init()
clock = pygame.time.Clock()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255,0,0)
black = (0,0,0)

X = 900
Y = 600

display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 52)
text = font.render('Oh, Kay Gandang Pagmasdan', True, 'royalblue')
textRect = text.get_rect()
textRect.center = (X // 2, Y // 3)
textVX,textVY,textX,textY, = textRect


empty_surface = pygame.Surface((textX,300), pygame.SRCALPHA)
empty_surface.fill('grey')
empty_surfaceRect = empty_surface.get_rect().center
print(empty_surface.get_rect())

frontfont = pygame.font.Font('freesansbold.ttf', 52)
fronttext = frontfont.render('Oh, Kay Gandang Pagmasdan', True, 'white')
fronttextRect = text.get_rect()
fronttextVX,fronttextVY,fronttextX,fronttextY, = fronttextRect

addcount = 0
minuscount = 0
asyncc = True
while True:
    if not addcount >= textX:
        addcount = addcount + 1/7
        print(int(addcount))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    display_surface.fill('grey')
    display_surface.blit(text, textRect)


    empty_surface = pygame.Surface((textX,textY), pygame.SRCALPHA)
    #empty_surface.fill('black')
    empty_surfaceRect = empty_surface.get_rect().center

    newtext = pygame.transform.chop(fronttext, (0, 0, addcount, 0))
    empty_surface.blit(newtext, (addcount, fronttextVY))

    display_surface.blit(empty_surface, (textVX,textVY))




    pygame.display.update()


    #clock.tick(30)
















print("Done")
