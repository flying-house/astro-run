import pygame # type: ignore
import random
from dataclasses import dataclass
from typing import List

@dataclass
class Star:
    x: float
    y: float
    brightness: int

class StarLayer:
    def __init__(self, screen_width: int, screen_height: int, 
                 star_count: int, parallax_speed: float, brightness_range: tuple):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.parallax_speed = parallax_speed / 1000
        self.stars: List[Star] = []
        
        for _ in range(star_count):
            self.stars.append(Star(
                x=random.uniform(0, screen_width),
                y=random.uniform(0, screen_height),
                brightness=random.randint(*brightness_range)
            ))
    
    def update(self, ship_vx: float, ship_vy: float, dt: float):
        for star in self.stars:
            star.x -= ship_vx * self.parallax_speed * dt
            star.y -= ship_vy * self.parallax_speed * dt
            
            if star.x < 0:
                star.x = self.screen_width
            elif star.x > self.screen_width:
                star.x = 0
                
            if star.y < 0:
                star.y = self.screen_height
            elif star.y > self.screen_height:
                star.y = 0
    
    def draw(self, screen: pygame.Surface):
        for star in self.stars:
            color = (star.brightness, star.brightness, star.brightness)
            pygame.draw.circle(screen, color, (int(star.x), int(star.y)), 1)

class Starfield:
    def __init__(self, screen_width: int, screen_height: int):
        self.layers = [
            StarLayer(screen_width, screen_height, 3, 1, (10, 20)),
            StarLayer(screen_width, screen_height, 3, 2, (15, 25)),
            StarLayer(screen_width, screen_height, 3, 3, (30, 55)),
            StarLayer(screen_width, screen_height, 4, 6, (40, 85)),
            StarLayer(screen_width, screen_height, 6, 8, (100, 155)),
            StarLayer(screen_width, screen_height, 10, 10, (180, 255))
        ]
    
    def update(self, ship_vx: float, ship_vy: float, dt: float):
        for layer in self.layers:
            layer.update(ship_vx, ship_vy, dt)
    
    def draw(self, screen: pygame.Surface):
        for layer in self.layers:
            layer.draw(screen)