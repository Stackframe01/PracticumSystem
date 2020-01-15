import numpy as np
import requests
from tqdm import tqdm_notebook
import pandas as pd
import re

'''
Список специализаций
spec = []
spec.append(requests.get("https://api.hh.ru/specializations").json())

Задача: выгруженный список отфильтровать от специальностей, не связанных со специализацией Программное и аппаратное обеспечение встраиваемых систем
'''

'''
Для специализации с Id=1.274
'''
vac = []
for i in tqdm_notebook(range(0, 98)):
    vac.append(requests.get("https://api.hh.ru/vacancies?specialization=1.274", params={'page': i, 'per_page':20}).json())
    
pac=[]
for i in range(0, 39):
    for j in range(0, 20):
        pac.append(vac[i]['items'][j]['alternate_url'])

lili = [re.sub(r'[^0-9]', '', e) for e in pac]
vak_url = 'https://api.hh.ru/vacancies/{}'
 
var = []
for i in lili:
    var.append(requests.get(vak_url.format(i)).json())

df = pd.DataFrame(var)

df['description'] = df['description'].apply(lambda x: (re.sub(r'<.*?>', '', str(x))))

file_name = 'description'
df.to_csv(file_name, columns =['description'])

