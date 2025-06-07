import math
import pygame # type: ignore
from dataclasses import dataclass
from engine.math.degreeconverter import natToPygameDeg

@dataclass
class ShipStats:
	name: str
	mass: float
	size: float
	rotSpdDegS: float
	thrustAccel: float
	maxThrust: float
	maxRotSpdDegS: float

	def __init__(self, name: str, mass: float, size: float,
			  rotSpdDegS: float, thrustAccel: float,
			  maxThrust: float, maxRotSpdDegS: float):
		self.name = name
		self.mass = mass
		self.size = size
		self.rotSpdDegS = rotSpdDegS
		self.thrustAccel = thrustAccel
		self.maxThrust = maxThrust
		self.maxRotSpdDegS = maxRotSpdDegS

@dataclass
class Ship:
	x: float
	y: float
	vx: float
	vy: float
	thrust: float
	rotation: float
	mass: float
	size: float

	def __init__(self, screen: pygame.Surface, stats: ShipStats):
		self.x = screen.get_width() * 0.5
		self.y = screen.get_height() * 0.8
		self.vx = 0
		self.vy = 0
		self.velocity = pygame.Vector2(0, 0)
		self.thrust = 0
		self.rotation = 0
		self.size = stats.size
		self.mass = stats.mass
		self.name = stats.name
		self.rotSpdDegS = stats.rotSpdDegS
		self.thrustAccel = stats.thrustAccel
		self.maxThrust = stats.maxThrust
		self.maxRotSpdDegS = stats.maxRotSpdDegS

	def draw(self, screen: pygame.Surface):
		shipPoints = self.getShipPoints(self.rotation, self.size, self.x, self.y)
		
		pygame.draw.polygon(screen, (255, 255, 255), shipPoints)

	def getShipPoints(self, rotation_degrees: float, size: float, x: float, y: float) -> list[tuple[float, float]]:
		points = [
			(0, -size),
			(size * 0.7, size),
			(-size * 0.7, size)
		]
		
		angle_rad = math.radians(rotation_degrees)
		rotated_points = []
		
		for px, py in points:
			rotated_x = px * math.cos(angle_rad) - py * math.sin(angle_rad)
			rotated_y = px * math.sin(angle_rad) + py * math.cos(angle_rad)
			
			final_x = rotated_x + x
			final_y = rotated_y + y
			
			rotated_points.append((final_x, final_y))
		
		return rotated_points
	
	def update(self, dt: float):
		self.velocity = pygame.Vector2(self.vx, self.vy)