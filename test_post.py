import pandas as pd 
import requests
import json 

nom_var = "yf_agrc_bevs_and_spices_tonne_ha"


### Cargamos datos de la consulta rest para ver que no hay información
r = requests.get(f"http://0.0.0.0:8080/ssp/get_all/{nom_var}")
j = r.json()

print(j)

## Poblamos la tabla
df = pd.read_csv(f"https://raw.githubusercontent.com/milocortes/sisepuede_data/main/AFOLU/{nom_var}/input_to_sisepuede/historical/{nom_var}.csv")

post_names = ["iso_code3", "nation", "year", "value"]
df.columns = post_names
n_registros = df.shape[0]

for i in range(n_registros):
    print(f"{i}/{n_registros}")    
    r = requests.post(f'http://0.0.0.0:8080/ssp/new/{nom_var}', json= json.loads(df.iloc[i,:].to_json()) )
    print(r.status_code)

### Cargamos datos de la consulta rest
r = requests.get(f"http://0.0.0.0:8080/ssp/get_all/{nom_var}")
j = r.json()

df_consulta = pd.DataFrame.from_dict(j)

### Cargamos datos de la consulta rest por pais
pais = "MEX"
r = requests.get(f"http://0.0.0.0:8080/ssp/get_country/{nom_var}/{pais}")
j = r.json()

df_consulta = pd.DataFrame.from_dict(j)

### Probaremos la función de actualización
### Cambiaremos los datos de México
df_consulta.query("iso_code3=='MEX'")

for anio in range(2011, 2020):

    requests.put(f"http://0.0.0.0:8080/ssp/edit/{nom_var}/MEX/{anio}", 
                json= {'iso_code3': 'MEX', 
                       'nation': 'Mexico', 
                       'year': anio, 
                       'value': 1111}
                )

### Volvemos a cargar los datos para ver las actualizaciones

r = requests.get(f"http://0.0.0.0:8080/ssp/get_country/{nom_var}/{pais}")
j = r.json()

df_consulta = pd.DataFrame.from_dict(j)
df_consulta