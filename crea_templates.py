import pandas as pd 
from jinja2 import Environment, FileSystemLoader

# Definimos la configuración de jinja
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

# Cargamos el template
template_output_tables = env.get_template('models_tablas_ssp.template')
template_mapping_objects = env.get_template('routes_tablas_ssp.template')

# Cargamos dataframe de tablas
tablas = pd.read_csv("ssp_metadata/output/tablas_sqlmodel.csv")
tablas = tablas.iloc[:2,]

# Enviamos la lista de tablas al template
output_tables = template_output_tables.render(tablas = tablas.variable.to_list())
output_mapping = template_mapping_objects.render(tablas = tablas.variable.to_list())

with open("models/tablas_ssp.py", "w") as text_file:
    text_file.write(output_tables)

with open("routes/tablas_ssp.py", "w") as text_file:
    text_file.write(output_mapping)

