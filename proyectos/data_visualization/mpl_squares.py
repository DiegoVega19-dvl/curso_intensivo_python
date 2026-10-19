import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.style.use('seaborn-v0_8')

fix, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# asignado titulo a graficos y etiquetas de los ejes

ax.set_title("Numeros al cuadrado", fontsize=24)
ax.set_xlabel("valor", fontsize=14)
ax.set_ylabel("valor del cuadrado", fontsize=14)

ax.tick_params(labelsize=14)

plt.show()