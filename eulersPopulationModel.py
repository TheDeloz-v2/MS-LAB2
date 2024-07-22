import numpy as np
from scipy.optimize import fsolve

# Datos iniciales
P0 = 15
P4 = 56
T = 4   

# Funcion para calcular la poblacion en un tiempo t
def population_model(t, r):
    return P0 * r * t

# Funcion para encontrar la tasa de crecimiento r
def growth_rate(r):
    return population_model(T, r) - P4

r_estimated, = fsolve(growth_rate, 0.1)

def get_population(time):
    Pt = population_model(time, r_estimated)
    return Pt

# Determinar el tiempo cuando la poblacion alcanza x numero de poblacion
def get_time(x):
    
    def get_time_to_population(t):
        return population_model(t, r_estimated) - x
    time, = fsolve(get_time_to_population, 0.1)
    
    return time

P12 = int(get_population(12))
time150 = get_time(150)

print(f"La tasa estimada de crecimiento r es: {r_estimated:.4f}")
print(f"La población estimada en 12 días es: {P12} mariposas.")
print(f"El tiempo estimado para alcanzar 150 mariposas es: {time150:.4f} días.")
