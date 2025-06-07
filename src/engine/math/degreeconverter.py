import math

def natToPygameDeg(degrees: float) -> float:
	return (degrees - 90) % 360

def pygameToNatDeg(degrees: float) -> float:
	return (degrees + 90) % 360