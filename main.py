import pandas as pd

# Carregar o arquivo CSV
# df = pd.read_csv('dados/centros_voluntarios_rs.csv', delimiter=',')
df = pd.read_excel('dados/centros_voluntarios_rs.xlsx')

# Transformar o DataFrame em JSON
json_result = df.to_json(orient='records')

# Salvar o JSON em um arquivo
with open('dados/centros_voluntarios_rs.json', 'w') as file:
    file.write(json_result)