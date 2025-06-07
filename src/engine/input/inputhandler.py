import pygame # type: ignore
from typing import Set
from game.entities.ship import Ship
import math

class InputHandler:
    def __init__(self):
        self.keys_pressed: Set[int] = set()
        self.keys_just_pressed: Set[int] = set()
        self.keys_just_released: Set[int] = set()
    
    def update(self, events):
        self.keys_just_pressed.clear()
        self.keys_just_released.clear()
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.keys_just_pressed.add(event.key)
                self.keys_pressed.add(event.key)
            elif event.type == pygame.KEYUP:
                self.keys_just_released.add(event.key)
                self.keys_pressed.discard(event.key)
    
    def is_pressed(self, key: int) -> bool:
        return key in self.keys_pressed
    
    def just_pressed(self, key: int) -> bool:
        return key in self.keys_just_pressed

def handleInput(ship: Ship, input_handler: InputHandler, dt: float):
    rotation_input = 0.0
    if input_handler.is_pressed(pygame.K_a):
        rotation_input = -1.0
    if input_handler.is_pressed(pygame.K_d):
        rotation_input = 1.0
    
    if rotation_input != 0:
        ship.rotation += rotation_input * ship.rotSpdDegS * dt
        ship.rotation = ship.rotation % 360
    
    thrust_input = 0.0
    if input_handler.is_pressed(pygame.K_w):
        thrust_input = 1.0
    if input_handler.is_pressed(pygame.K_s):
        thrust_input = -0.5
    
    if thrust_input != 0:
        angle_rad = math.radians(ship.rotation)
        thrust_force = thrust_input * ship.maxThrust
        
        accel_x = (thrust_force * math.sin(angle_rad)) / ship.mass
        accel_y = -(thrust_force * math.cos(angle_rad)) / ship.mass
        
        ship.vx += accel_x * dt
        ship.vy += accel_y * dt

def update(ship: Ship, input_handler: InputHandler, dt: float):
    handleInput(ship, input_handler, dt)