"""
===================================================
                    Astro Run
             A 2D space delivery game
                                   by flying-house
====================================================
"""

import pygame # type: ignore
import sys
from pathlib import Path
from game.entities.ship import Ship, ShipStats
from engine.input.inputhandler import InputHandler, update as updateShip
from engine.graphics.starfield import Starfield
from engine.resources.debugger import Debugger

import sys
sys.path.append(str(Path(__file__).parent))

def main():
    pygame.init()
    screen = pygame.display.set_mode((1500, 1200))
    pygame.display.set_caption("Astro Run")
    inputHandler = InputHandler()
    clock = pygame.time.Clock()

    starField = Starfield(screen.get_width(), screen.get_height())
    basicShip = ShipStats(
        name="Basic Ship",
        mass=2,
        size=7,
        rotSpdDegS=150,
        thrustAccel=300,
        maxThrust=1200,
        maxRotSpdDegS=150,
    )
    ship = Ship(screen, basicShip)
    debugger = Debugger()

    running = True
    while running:
        dt_ms = clock.get_time()
        dt = dt_ms / 1000.0
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        inputHandler.update(events)
        
        updateShip(ship, inputHandler, dt)
        ship.update(dt)
        
        starField.update(ship.vx, ship.vy, dt)

        screen.fill((25, 25, 51))
        starField.draw(screen)
        ship.draw(screen)
        debugger.draw(screen, ship, dt)

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
