# FSK Modulation Python Script Didáctico
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
Fc = 30              # Frecuencia base de portadora [Hz]

# Señal binaria
Td = 0.1             # Duración de cada bit [s]
Nsamples = int(Td*Fs)               # Muestras por bit
Nbits = int(np.floor(len(t)/Nsamples))  # Número de bits
message = binary(Nbits, Nsamples)        # Señal binaria (0/1)

# ------------------------
# Generación de señal FSK
# ------------------------
# Frecuencias FSK: bit=0 -> Fc, bit=1 -> Fc + Fc/2
f_fsk = Fc + (Fc/2) * message
fsk_signal = np.sin(2*pi*f_fsk*t)

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
plt.plot(t, fsk_signal, 'r')
plt.title("Señal FSK Modulada")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

plt.tight_layout()
plt.show()
