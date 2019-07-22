import numpy as np
import pandas as pd

data=pd.read_csv('milk_promo_sales.csv')
data=data.sort_values(by=['store_id','period_id'])
data['diff']=data.groupby('store_id')['period_id'].diff()
# data['cumcount']=data[data['diff']==1].groupby('store_id').cumcount()
data['promo']=(data['store_id']!=data['store_id'].shift()) | (data['period_id']!=data['period_id'].shift()+1)
data['cumsum']=data.groupby('store_id')['promo'].cumsum()
data['sum']=data.groupby(['store_id','cumsum'])['sales_volume'].cumsum()
data['sumDiff']=data.groupby(['store_id','cumsum'])['diff'].cumcount()+1

print(dict(data['promo'].value_counts()).get(True)) #1. Общее количество промопериодов (во всех магазинах)
print(np.median(data[data['promo'].shift(-1)==True]['sumDiff'])) #2. Медиана продолжительности промопериода (количество недель)
print(data[data['promo'].shift(-1)==True]['sum']) #3. Объем  продаж по каждому промопериоду
print(np.median(data[data['promo'].shift(-1)==True].drop_duplicates(subset='store_id',keep='last')
      ['cumsum'])) #4. Медиана количества промопериодов на один магазин

# data.to_csv('ansCSV1.csv',index=False)
# data.to_excel('ansEx1.xlsx',index=False)

# 1. 140992
# 2. 3
# 3. Ответ в ansCSV1.csv в колонке 'sum'
# 4. 6