"""
=============================================================
Astro Run
A 2D space cargo delivery game by theFlyingHouse
=============================================================
"""

import pygame # type: ignore
import sys
from pathlib import Path

import sys
sys.path.append(str(Path(__file__).parent))

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((1500, 1200))
    pygame.display.set_caption("Astro Run")
    
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        screen.fill((25, 25, 51))
        
        # TODO: Game rendering       

        pygame.display.flip()
        
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()