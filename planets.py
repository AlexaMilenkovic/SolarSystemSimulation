import math
import random

distance_scale = 0.01  
size_scale = 0.005
class NebeskaTela:
    def __init__(self, name, distance, radius, color, orbit_speed, height, angle):
        self.name = name
        self.distance = distance
        self.radius = radius
        self.color = color
        self.orbit_speed = orbit_speed
        self.height = height
        self.angle = angle

class Zvezda(NebeskaTela):
    def __init__(self, name, radius, color):
        super().__init__(name, 0, radius, color, 0, 0, 0)

class Planete(NebeskaTela):
    def __init__(self, name, distance, radius, color, orbit_speed, height, angle=0):
        super().__init__(name, distance, radius, color, orbit_speed, height, angle)

class Asteroidi(NebeskaTela):
    def __init__(self, name, distance, radius, color, orbit_speed, height, angle):
        super().__init__(name, distance, radius, color, orbit_speed, height, angle)

planete_podaci = [
    {"name": "Mars", "distance": (100 + 49.6) * distance_scale, "radius": 2.44 * size_scale, "color": (0.5, 0.5, 0.5), "orbit_speed": 4.15, "height": 0},
    {"name": "Venera", "distance": (100 + 108) * distance_scale, "radius": 6.05 * size_scale, "color": (1.0, 0.8, 0.0), "orbit_speed": 1.62, "height": 0.01},
    {"name": "Zemlja", "distance": (100 + 151) * distance_scale, "radius": 6.37 * size_scale, "color": (0.0, 0.0, 1.0), "orbit_speed": 1.0, "height": 0.075},
    {"name": "Mars", "distance": (100 + 206) * distance_scale, "radius": 3.39 * size_scale, "color": (1.0, 0.0, 0.0), "orbit_speed": 0.53, "height": 0.15},
    {"name": "Jupiter", "distance": (100 + 754) * distance_scale, "radius": 69.9 * size_scale, "color": (1.0, 0.5, 0.0), "orbit_speed": 0.08, "height": 0.5},
    {"name": "Saturn", "distance": (100 + 1445) * distance_scale, "radius": 58.2 * size_scale, "color": (1.0, 1.0, 0.5), "orbit_speed": 0.03, "height": 0.75},
    {"name": "Uranus", "distance": (100 + 2927) * distance_scale, "radius": 25.4 * size_scale, "color": (0.0, 1.0, 1.0), "orbit_speed": 0.011, "height": 0.375},
    {"name": "Neptun", "distance": (100 + 4471) * distance_scale, "radius": 24.6 * size_scale, "color": (0.0, 0.0, 1.0), "orbit_speed": 0.006, "height": 0.6125}
]
celestial_bodies = [Planete(**data) for data in planete_podaci]
celestial_bodies.insert(0, Zvezda("Sunce", 1391 * size_scale / 5, (1.0, 1.0, 0.0)))

asteroid_count = 36 * 6
asteroid_distance = (((100 + 206) + (100 + 754)) / 2) * distance_scale
asteroid_orbit_speed = (1.0 + 0.53) / 2  
asteroid_radius = (2.44 + 2 * random.random()) * size_scale
asteroid_color = (0.3, 0.3, 0.3)

for i in range(asteroid_count):
    angle = random.uniform(0, 360)
    height = random.uniform(-0.2, 0.2)
    celestial_bodies.append(Asteroidi("Asteroid", asteroid_distance, asteroid_radius, asteroid_color, asteroid_orbit_speed, height, angle))

outer_asteroid_count = 36 * 30
outer_asteroid_distance = (((100 + 4471) * 2 + (100 + 4471)) / 2) * distance_scale
outer_asteroid_orbit_speed = 0.003  
outer_asteroid_radius = (2.44 + random.uniform(5, 20)) * size_scale
outer_asteroid_color = (0.3, 0.3, 0.3)

for i in range(outer_asteroid_count):
    angle = random.uniform(0, 360)
    height = random.uniform(-0.5, 0.5)
    celestial_bodies.append(Asteroidi("Asteroid", outer_asteroid_distance, outer_asteroid_radius, outer_asteroid_color, outer_asteroid_orbit_speed, height, angle))
