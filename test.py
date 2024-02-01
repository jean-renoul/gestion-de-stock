from shop import Shop
import pygame
from pygame.locals import *

boucherie = Shop()

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Boucherie")
font = pygame.font.Font('police_ecriture.ttf', 15)

background = pygame.image.load('background.png')


def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2

    fontHeight = font.size("police_ecriture.ttf")[1]

    while text:
        i = 1

        if y + fontHeight > rect.bottom:
            break

        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1
     
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        text = text[i:]

    return text

def dialogue(message):
    bubble = pygame.image.load('bulle.png')
    screen.blit(bubble, (150, 30))
    drawText(screen, message, (0, 0, 0), (170, 75, 270, 400), font, True)
    pygame.display.flip()

def prompt(message):
    pygame.draw.rect(screen, (0, 0, 0), (0, 800, 600, 800))
    drawText(screen, message, (255, 255, 255), (10, 610, 790, 790), font, True)
    pygame.display.flip()
message = "Bonjour, je suis le boucher, que voulez-vous faire ?"
running = True
screen.blit(background, (0, 0))
while running:    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.pos[0] > 0 and event.pos[0] < 200 and event.pos[1] > 600 and event.pos[1] < 630:
                message = (str(boucherie.readProducts()))
                pygame.display.flip()
                pygame.time.delay(5000)
            if event.pos[0] > 200 and event.pos[0] < 400 and event.pos[1] > 600 and event.pos[1] < 630:
                print (2)
                pygame.display.flip()
            if event.pos[0] > 400 and event.pos[0] < 600 and event.pos[1] > 600 and event.pos[1] < 630:
                print (3)
                pygame.display.flip()
            if event.pos[0] > 600 and event.pos[0] < 800 and event.pos[1] > 600 and event.pos[1] < 630:
                print (4)
                pygame.display.flip()
    
    
    dialogue(message)
    prompt("Afficher les produits | Ajouter un produit | Modifier un produit | Supprimer un produit | Afficher les catégories | Afficher une catégorie" )
    pygame.display.flip()




