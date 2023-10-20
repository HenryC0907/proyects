import matplotlib.pyplot as plt
import pandas as pd

# Lee los datos desde el archivo CSV
data = pd.read_csv('Terrestre5s.csv')

# Extrae las columnas de interés
time = data['time']
columns_to_plot = ['Bx', 'By', 'Bz', 'BT']

# Crea un gráfico para cada columna de B_{algo}
plt.figure(figsize=(10, 6))

for column in columns_to_plot:
    plt.plot(time, data[column], label=column)

# Configura el gráfico
plt.title('Datos de B_{algo} respecto al Tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Valor de B_{algo')
plt.legend()
plt.grid(True)

# Muestra el gráfico en pantalla
plt.show()
