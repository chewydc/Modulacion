# AM Modulation Python Script Didáctico
import numpy as np
import matplotlib.pyplot as plt
from math import pi

plt.close('all')

# Parámetros de simulación
Fs = 5000            # Frecuencia de muestreo
t = np.arange(0, 1, 1/Fs)   # Vector de tiempo

# Portadora
Fc = 50              # Frecuencia de portadora
Ac = 1               # Amplitud de portadora
carrier = Ac * np.cos(2 * pi * Fc * t)

# Señal de mensaje
Fm = 5               # Frecuencia de mensaje (mucho menor que Fc)
Am = 0.5             # Amplitud inicial de mensaje
message = Am * np.cos(2 * pi * Fm * t)

# ------------------------
# 1) Señales básicas
# ------------------------
plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.plot(t, message, 'b')
plt.title("Señal de Mensaje (m(t))")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t, carrier, 'r')
plt.title("Portadora (c(t))")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

plt.subplot(3,1,3)
modulated = carrier * (1 + message/Ac)
plt.plot(t, modulated, 'g')
plt.title("Señal AM modulada (Am=0.5)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

plt.tight_layout()
plt.show()

# ------------------------
# 2) Ejemplos de modulación
# ------------------------
plt.figure(figsize=(10,8))

# Caso 1: Modulación menor al 100% (m=0.5)
Am = 0.5
m = Am * np.cos(2*pi*Fm*t)
s = carrier * (1 + m/Ac)
plt.subplot(3,1,1)
plt.plot(t, s, 'g')
plt.title("AM Bien modulada (Am=0.5, m=0.5)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

# Caso 2: Modulación al 100% (m=1)
Am = 1
m = Am * np.cos(2*pi*Fm*t)
s = carrier * (1 + m/Ac)
plt.subplot(3,1,2)
plt.plot(t, s, 'b')
plt.title("AM al 100% (Am=1, m=1)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

# Caso 3: Overmodulation (m=1.5)
Am = 1.5
m = Am * np.cos(2*pi*Fm*t)
s = carrier * (1 + m/Ac)
plt.subplot(3,1,3)
plt.plot(t, s, 'r')
plt.title("Overmodulation (Am=1.5, m=1.5)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

plt.tight_layout()
plt.show()
