# py00_PyGame_template.py
import pygame 
from pygame.locals import QUIT 
import sys 

pygame.init()
Surface = pygame.display.set_mode((640, 400)) 
FRSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Basic')

def main():
    while True:
        Surface.fill(color='black') # Surface((0, 0, 0))
        for event in pygame.event.get() :
            if event.type == QUIT: 
                pygame.quit()  
                sys.exit()   

        pygame.display.update() 
        FRSCLOCK.tick(30) 

if __name__=='__main__':
    main()