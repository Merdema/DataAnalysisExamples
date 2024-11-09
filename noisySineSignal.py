import numpy as np
import matplotlib.pyplot as plt


num_points = 1000
x = np.linspace(0, 10, num_points)
signal = np.sin(x)
noise = np.random.normal(0, 0.5, num_points)
noisy_signal = signal + noise


window_size = 50
filtered_signal = np.convolve(noisy_signal, np.ones(window_size)/window_size, mode='same')


noise_energy_before = np.sum((noisy_signal - signal)**2)
noise_energy_after = np.sum((filtered_signal - signal)**2)
noise_reduction_ratio = 100 * (1 - noise_energy_after / noise_energy_before)


plt.figure(figsize=(10, 6))
plt.plot(x, signal, label="Orijinal Sinyal", color='blue')
plt.plot(x, noisy_signal, label="Gürültülü Sinyal", color='orange', alpha=0.6)
plt.plot(x, filtered_signal, label="Filtrelenmiş Sinyal", color='green', linestyle='dashed')
plt.legend()
plt.xlabel("Zaman")
plt.ylabel("Genlik")
plt.title("Orijinal, Gürültülü ve Filtrelenmiş Sinyal")
plt.show()

noise_reduction_ratio

