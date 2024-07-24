import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Datos iniciales
y0 = 15
y4 = 56
N = 300  

# Funcion para calcular la poblacion en un tiempo t
def population(t, k, y0, N):
    return N / (1 + ((N - y0) / y0) * np.exp(-k * t))

# Funcion para encontrar la tasa de crecimiento k
def growth_rate(k):
    return y4 - (N / (1 + ((N - y0) / y0) * np.exp(-k * 4)))

# Determinar el tiempo cuando la poblacion alcanza x numero de poblacion
def equation_for_time(t):
    return population(t, k, y0, N) - 150

k_initial_guess = 0.1
k = fsolve(growth_rate, k_initial_guess)[0]

y12 = population(12, k, y0, N)

t_initial_guess = 5
t_150 = fsolve(equation_for_time, t_initial_guess)[0]

print(f"La tasa estimada de crecimiento k es: {k:.4f}")
print(f"La población estimada en 12 días es: {round(y12)} mariposas.")
print(f"El tiempo estimado para alcanzar 150 mariposas es: {t_150:.4f} días.")

# Graficar la poblacion
def plot_population():
    t = np.linspace(0, 20, 100)
    y = population(t, k, y0, N)
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, label='Población de mariposas')
    plt.xlabel('Días')
    plt.ylabel('Número de mariposas')
    plt.title('Modelo de crecimiento de la población de mariposas')
    plt.legend()
    plt.grid(True)
    plt.show()
