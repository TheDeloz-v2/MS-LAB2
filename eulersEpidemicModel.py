import matplotlib.pyplot as plt
import numpy as np

def eulersEpidemic(S0, I0, R0, t, dt, gamma, beta):
    steps = int(t / dt)

    # Inicializacion de los vectores
    S = np.zeros(steps)
    I = np.zeros(steps)
    R = np.zeros(steps)
    T = np.zeros(steps)

    # Condiciones iniciales
    N = S0 + I0 + R0
    S[0] = S0
    I[0] = I0
    R[0] = R0

    # Metodo de Euler
    for step in range(1, steps):
        T[step] = step * dt
        
        dS = -beta * S[step - 1] * I[step - 1] / N * dt
        dI = (beta * S[step - 1] * I[step - 1] / N - gamma * I[step - 1]) * dt
        dR = gamma * I[step - 1] * dt
        
        S[step] = S[step - 1] + dS
        I[step] = I[step - 1] + dI
        R[step] = R[step - 1] + dR
        
        S[step] = max(S[step], 0)
        I[step] = max(I[step], 0)
        R[step] = max(R[step], 0)
        
    print(f"Población:\tN = {N}")
    print(f"Susceptibless:\tS(t={t}) = {round(S[-1])}")
    print(f"Infectados:\tI(t={t}) = {round(I[-1])}")
    print(f"Recuperados:\tR(t={t}) = {round(R[-1])}")
    
    return T, S, I, R

def plot(T, S, I, R):
    plt.figure(figsize=(10, 6))
    plt.plot(T, S, label='Susceptibles (S)')
    plt.plot(T, I, label='Infectados (I)')
    plt.plot(T, R, label='Recuperados (R)')
    plt.xlabel('Días')
    plt.ylabel('Número de individuos')
    plt.title('Modelo SIR usando el método de Euler')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def main():
    
    beta = 0.3
    gamma = 0.1
    
    # Susceptibles, infectados y recuperados iniciales
    S0 = 990
    I0 = 10
    R0 = 0
    
    # Paso del tiempo y tiempo final
    dt = 0.1
    t = 50
    
    T, S, I, R = eulersEpidemic(S0, I0, R0, t, dt, gamma, beta)
    plot(T, S, I, R)
    
if __name__ == "__main__":
    main()