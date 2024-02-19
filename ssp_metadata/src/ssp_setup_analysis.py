# Cargamos paquetes
import os
import sys
import pandas as pd 

# Definimos el directorio donde se encuentra sisepuede
FILE_PATH = os.getcwd()
sys.path.append(os.path.join(FILE_PATH, "sisepuede", "python"))

# Definimos la ruta del directorio de salida
OUTPUT_PATH = os.path.abspath(os.path.join(FILE_PATH, "..", "output"))

# Cargamos el paquete setup_analysis de sisepuede, el cual contiene metadatos del modelo
import setup_analysis as sa

# Obtenemos los sectores de sisepuede
sectores = sa.model_attributes.all_sectors

# Obtenemos los subsectores de AFOLU
sa.model_attributes.get_sector_subsectors('AFOLU')

# Obtenemos las variables del subsector Agriculture
sa.model_attributes.get_subsector_variables('Agriculture')

# Obtenemos la lista de variables de Crop Yield Factor
sa.model_attributes.build_varlist(None,'Crop Yield Factor')

# Exportamos la lista de variables anterior para generar una lista de tablas a crear con SQLModel
tablas_sqlmodel = pd.DataFrame([("AFOLU", "Agriculture", "Crop Yield Factor", i) for i in sa.model_attributes.build_varlist(None,'Crop Yield Factor')], 
                                columns = ["sector", "subsector", "var_subsector", "variable"])

tablas_sqlmodel.to_csv(os.path.join(OUTPUT_PATH, "tablas_sqlmodel.csv"), index = False)                                