import matplotlib.pyplot as plt

# Leitura dos dados de escalabilidade forte
with open('strong_scaling.txt') as f:
    strong_scaling = [line.split() for line in f if "Solver runtime" in line]
threads = [1, 2, 4, 6, 8, 10, 12]
strong_times = [float(item[3]) for item in strong_scaling]

# Leitura dos dados de escalabilidade fraca
with open('weak_scaling.txt') as f:
    weak_scaling = [line.split() for line in f if "Solver runtime" in line]
scales = [1, 2, 4, 6, 8, 10, 12]
weak_times = [float(item[3]) for item in weak_scaling]

# Plot escalabilidade forte
plt.figure()
plt.plot(threads, strong_times, marker='o')
plt.xlabel('Número de Threads')
plt.ylabel('Tempo de Execução (s)')
plt.title('Escalabilidade Forte')
plt.grid(True)
plt.savefig('strong_scaling.png')

# Plot escalabilidade fraca
plt.figure()
plt.plot(scales, weak_times, marker='o')
plt.xlabel('Número de Threads')
plt.ylabel('Tempo de Execução (s)')
plt.title('Escalabilidade Fraca')
plt.grid(True)
plt.savefig('weak_scaling.png')

plt.show()
