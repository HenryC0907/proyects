import os
import pandas as pd

# Carpeta donde se encuentran los archivos CSV de chunks
chunk_folder = os.path.expanduser('~/Escritorio/lab7/chunks')
output_directory = os.path.expanduser('~/Escritorio/lab7/resultado')

# Crea el directorio de salida si no existe
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Calcular la derivada discreta de Bx y By, y unir los chunks
derivative_threshold = 5
chunks_to_merge = []
current_chunk = []

# Enumera los archivos CSV en la carpeta
for i in range(100):  # Reemplaza 100 con el número de chunks que tengas
    chunk_path = os.path.join(chunk_folder, f'chunk_{i}.csv')
    chunk = pd.read_csv(chunk_path)
    
    # Calcula el promedio de Bx y By en el chunk actual
    chunk_mean_Bx = chunk['Bx'].mean()
    chunk_mean_By = chunk['By'].mean()
    
    if current_chunk:
        # Calcula la derivada discreta de Bx y By con respecto al chunk anterior
        previous_chunk = pd.read_csv(os.path.join(chunk_folder, f'chunk_{i - 1}.csv'))
        derivative_Bx = abs(chunk_mean_Bx - previous_chunk['Bx'].mean())
        derivative_By = abs(chunk_mean_By - previous_chunk['By'].mean())
        
        if derivative_Bx < derivative_threshold and derivative_By < derivative_threshold:
            current_chunk.append(i)
        else:
            chunks_to_merge.append(current_chunk)
            current_chunk = [i]
    else:
        current_chunk = [i]

# Combina los chunks
for chunk_indices in chunks_to_merge:
    merged_data = pd.concat([pd.read_csv(os.path.join(chunk_folder, f'chunk_{i}.csv')) for i in chunk_indices])
    merged_data.to_csv(os.path.join(output_directory, f'file{chunk_indices[0]}.csv'), index=False)

