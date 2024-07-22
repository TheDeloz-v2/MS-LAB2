import matplotlib.pyplot as plt

def eulersEpidemic(S0, I0, R0, t, dt, gamma, beta):
    steps = int(t / dt)

    # Inicializacion de los vectores
    S = [0] * (steps + 1)
    I = [0] * (steps + 1)
    R = [0] * (steps + 1)
    T = [0] * (steps + 1)

    # Condiciones iniciales
    N = S0 + I0 + R0
    S[0] = S0
    I[0] = I0
    R[0] = R0

    # Metodo de Euler
    for step in range(steps):
        T[step + 1] = T[step] + dt
        
        dS = -beta * S[step] * I[step]/N * dt
        dI = (beta * S[step] * I[step]/N - gamma * I[step]) * dt
        dR = gamma * I[step] * dt
        
        S[step + 1] = S[step] + dS
        I[step + 1] = I[step] + dI
        R[step + 1] = R[step] + dR
        
        S[step + 1] = max(S[step + 1], 0)
        I[step + 1] = max(I[step + 1], 0)
        R[step + 1] = max(R[step + 1], 0)
        
    print(f"S(t={t}) = {S[-1]}")
    print(f"I(t={t}) = {I[-1]}")
    print(f"R(t={t}) = {R[-1]}")
    
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