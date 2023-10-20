import os
import pandas as pd
import matplotlib.pyplot as plt

# Carpeta donde se encuentran los archivos CSV resultantes
result_folder = os.path.expanduser('~/Escritorio/lab7/resultado')

# Enumera y traza gráficas para cada archivo CSV en la carpeta de resultados
for file_name in os.listdir(result_folder):
    if file_name.endswith('.csv'):
        file_path = os.path.join(result_folder, file_name)
        data = pd.read_csv(file_path)
        
        # Extrae las columnas de tiempo, Bx y By
        tiempo = data['time']
        Bx = data['Bx']
        By = data['By']
        
        # Crea una nueva figura para cada archivo
        plt.figure()
        
        # Trazar la gráfica [Tiempo, Bx]
        plt.subplot(2, 1, 1)
        plt.plot(tiempo, Bx)
        plt.title('Gráfica [Tiempo, Bx]')
        plt.xlabel('Tiempo')
        plt.ylabel('Bx')
        
        # Trazar la gráfica [Tiempo, By]
        plt.subplot(2, 1, 2)
        plt.plot(tiempo, By)
        plt.title('Gráfica [Tiempo, By]')
        plt.xlabel('Tiempo')
        plt.ylabel('By')
        
        # Ajusta el diseño de las gráficas
        plt.tight_layout()
        
        # Mostrar gráficas en pantalla
        plt.show()

