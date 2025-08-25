# PM Modulation Python Script Didáctico
import numpy as np
import matplotlib.pyplot as plt
from math import pi

plt.close('all')

# Parámetros
Fs = 500
t = np.arange(0, 1, 1/Fs)      # 1 segundo
Fc = 5                          # Portadora lenta para ver ciclos
Fm = 1                          # Frecuencia de mensaje
message = np.sin(2*pi*Fm*t)    # Señal de mensaje analógica

# Factor de modulación para ±180° en el pico del mensaje
kp = pi

# Señal PM
pm_signal = np.cos(2*pi*Fc*t + kp * message)

# Ploteo
plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.plot(t, message, 'b')
plt.title("Señal de Mensaje Analógica (m(t))")
plt.ylabel("Amplitud")
plt.grid(True)

plt.subplot(3,1,2)
carrier = np.cos(2*pi*Fc*t)
plt.plot(t, carrier, 'r')
plt.title("Portadora (c(t))")
plt.ylabel("Amplitud")
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t, pm_signal, 'g')
plt.title("Señal PM modulada - cambio de fase ±180° en los picos")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

plt.xlim(0, 1)  # Ajustar para que se vean claramente los picos
plt.tight_layout()
plt.show()
