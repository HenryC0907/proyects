import pandas as pd
import os

# Lee los datos desde el archivo CSV
data = pd.read_csv('Terrestre5s.csv')

# Define la longitud deseada de cada chunk (n filas)
chunk_size = 100

# Directorio donde deseas guardar los chunks
output_directory = os.path.expanduser('~/Escritorio/lab7/chunks')

# Crea el directorio si no existe
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Divide los datos en chunks de tamaño fijo y guárdalos en archivos CSV separados
for i, chunk_start in enumerate(range(0, len(data), chunk_size)):
    chunk_end = chunk_start + chunk_size
    chunk = data.iloc[chunk_start:chunk_end]
    # Especifica la ruta completa para guardar en la carpeta deseada
    chunk.to_csv(os.path.join(output_directory, f'chunk_{i}.csv'), index=False)

