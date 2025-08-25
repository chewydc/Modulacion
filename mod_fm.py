# FM Modulation Python Script Didáctico
import numpy as np
import matplotlib.pyplot as plt
from math import pi

plt.close('all')

# ------------------------
# Parámetros de simulación
# ------------------------
Fs = 5000            # Frecuencia de muestreo
t = np.arange(0, 1, 1/Fs)   # Vector de tiempo

# Portadora
Fc = 50              # Frecuencia de portadora
Ac = 1               # Amplitud de portadora
carrier = Ac * np.cos(2 * pi * Fc * t)

# Señal de mensaje
Fm = 5               # Frecuencia de mensaje (mucho menor que Fc)
Am = 1               # Amplitud de mensaje
message = Am * np.cos(2 * pi * Fm * t)

# Índice de modulación para FM
b = 5  # cuanto mayor, más se nota la variación de frecuencia

# ------------------------
# 1) Señales básicas
# ------------------------
plt.figure(figsize=(10,8))

# Mensaje
plt.subplot(3,1,1)
plt.plot(t, message, 'b')
plt.title("Señal de Mensaje (m(t))")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

# Portadora
plt.subplot(3,1,2)
plt.plot(t, carrier, 'r')
plt.title("Portadora (c(t))")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

# Señal FM
fm_signal = np.cos(2 * pi * Fc * t + b * message)  # FM: frecuencia instantánea = Fc + b*m(t)
plt.subplot(3,1,3)
plt.plot(t, fm_signal, 'g')
plt.title(f"Señal FM modulada (índice b={b})")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

plt.tight_layout()
plt.show()

# FM Modulation Didactic Example - Effect of Modulation Index
import numpy as np
import matplotlib.pyplot as plt
from math import pi

plt.close('all')

# ------------------------
# Parámetros de simulación
# ------------------------
Fs = 5000               # Frecuencia de muestreo
t = np.arange(0, 0.5, 1/Fs)   # Tiempo suficiente para varios ciclos
Fc = 50                 # Frecuencia de portadora
Fm = 5                  # Frecuencia de mensaje
message = np.cos(2*pi*Fm*t)  # Señal de mensaje simple

# Índices de modulación a comparar
mod_indices = [1, 5, 25, 50]  # desde baja a sobre-modulación
colors = ['g', 'b', 'orange', 'r']
titles = [
    'FM - baja modulación (β=1)',
    'FM - modulación ligera (β=5)',
    'FM - modulación adecuada (β=25)',
    'FM - sobre-modulación (β=50)'
]

# ------------------------
# Ploteo comparativo
# ------------------------
plt.figure(figsize=(12,10))

for i, beta in enumerate(mod_indices):
    fm_signal = np.cos(2*pi*Fc*t + beta * message)
    plt.subplot(4,1,i+1)
    plt.plot(t, fm_signal, colors[i])
    plt.title(titles[i])
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)

plt.tight_layout()
plt.show()
