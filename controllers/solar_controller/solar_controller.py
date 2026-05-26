from controller import Supervisor
import math

robot = Supervisor()
timestep = int(robot.getBasicTimeStep())

self_node = robot.getSelf()
nombre = self_node.getField("name").getSFString()

# Distancia al Sol, velocidad orbital, velocidad de rotacion propia
datos = {
    "sol":      {"distancia": 0,  "orbital": 0,     "rotacion": 0.001},
    "mercurio": {"distancia": 6,  "orbital": 0.047, "rotacion": 0.004},
    "venus":    {"distancia": 9,  "orbital": 0.035, "rotacion": 0.002},
    "tierra":   {"distancia": 13, "orbital": 0.020, "rotacion": 0.010},
    "marte":    {"distancia": 17, "orbital": 0.015, "rotacion": 0.009},
    "jupiter":  {"distancia": 24, "orbital": 0.008, "rotacion": 0.025},
    "saturno":  {"distancia": 32, "orbital": 0.006, "rotacion": 0.022},
    "urano":    {"distancia": 40, "orbital": 0.004, "rotacion": 0.014},
    "neptuno":  {"distancia": 48, "orbital": 0.003, "rotacion": 0.015},
}

info = datos.get(nombre, {"distancia": 10, "orbital": 0.01, "rotacion": 0.01})

distancia = info["distancia"]
vel_orbital = info["orbital"]
vel_rotacion = info["rotacion"]

angulo_orbital = 0.0
angulo_rotacion = 0.0

translation_field = self_node.getField("translation")
rotation_field = self_node.getField("rotation")

while robot.step(timestep) != -1:
    # Orbita alrededor del Sol
    if distancia > 0:
        angulo_orbital += vel_orbital
        x = distancia * math.cos(angulo_orbital)
        z = distancia * math.sin(angulo_orbital)
        translation_field.setSFVec3f([x, 0, z])

    # Rotacion sobre su propio eje
    angulo_rotacion += vel_rotacion
    rotation_field.setSFRotation([0, 1, 0, angulo_rotacion])