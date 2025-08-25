# ASK Modulation Python Script Mejorado
import numpy as np
import matplotlib.pyplot as plt
from Binarygen import binary
from math import pi

plt.close('all')

# ------------------------
# Parámetros de simulación
# ------------------------
Fs = 1000            # Frecuencia de muestreo
T = 1                # Duración total [s]
t = np.arange(0, T, 1/Fs)

# Configuración de portadora
Fc = 30              # Frecuencia de portadora [Hz]
Ac0 = 1              # Amplitud para bit=0
Ac1 = 2              # Amplitud para bit=1

# Señal binaria
Td = 0.1             # Duración de cada bit [s]
Nsamples = int(Td*Fs)               # Muestras por bit
Nbits = int(np.floor(len(t)/Nsamples))  # Número de bits
message = binary(Nbits, Nsamples)        # Señal binaria (0/1)

# ------------------------
# Generación de señal ASK
# ------------------------
# Asignamos amplitud según bit
amplitude = Ac0 + (Ac1 - Ac0) * message
ask_signal = amplitude * np.cos(2*pi*Fc*t)

# ------------------------
# Ploteo de resultados
# ------------------------
plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.plot(t, message, 'b')
plt.title("Señal Binaria (m(t))")
plt.ylabel("Nivel lógico")
plt.grid(True)
plt.ylim(-0.2, 1.2)

plt.subplot(2,1,2)
plt.plot(t, ask_signal, 'r')
plt.title("Señal ASK Modulada")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

plt.tight_layout()
plt.show()
