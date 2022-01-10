import pandas as pd

df = pd.read_csv(r'C:\Users\Trabajo\Desktop\CursoDASH-PLOLTY\Datasets\2.3\Info_pais.csv',encoding = 'ISO-8859-1',delimiter=';')

print(df.head())