import pygame # type: ignore
from game.entities.ship import Ship

class Debugger:
    def __init__(self):
        self.font = pygame.font.SysFont('monospace', 16)
        self.frame_count = 0
        self.update_interval = 5
        self.cached_text_surfaces = []

    def draw(self, screen: pygame.Surface, ship: Ship, dt: float):	
        self.frame_count += 1
        
        if self.frame_count >= self.update_interval:
            self.updateText(ship, dt)
            self.frame_count = 0
        
        y_offset = 10
        for text_surface in self.cached_text_surfaces:
            screen.blit(text_surface, (10, y_offset))
            y_offset += 20

    def updateText(self, ship: Ship, dt: float):
        speed = ship.velocity.length()
        fps = 1.0 / dt if dt > 0 else 0

        debug_lines = [
            f"FPS:        {fps:.1f}",
            f"Rotation:   {ship.rotation:.1f}°",
            f"Speed:      {speed:.1f}"
        ]
        
        self.cached_text_surfaces = []
        for line in debug_lines:
            text_surface = self.font.render(line, True, (255, 255, 0))
            self.cached_text_surfaces.append(text_surface)