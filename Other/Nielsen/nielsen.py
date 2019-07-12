import numpy as np
import pandas as pd

data=pd.read_csv('milk_promo_sales.csv')
# unq=np.unique(data['store_id']) #ID всех магазинов
allDuration=np.array([1])
allCount=0
sum=0
tempSum=0
data=data.sort_values(by=['store_id','period_id'])
# print(data)
prev_id=0
prev_per=0
count=1
duration=1
def func(row):
    global  allDuration, allCount, sum, tempSum, prev_id, prev_per, count, duration
    if row['period_id']-prev_per>1 and row['store_id']==prev_id:
        prev_per=row['period_id']
        count += 1
        allCount=count
        allDuration =np.append(allDuration,1)
        duration = 1
        if tempSum==0:
            sum=row['sales_volume']
        tempSum=0
    elif row['store_id']!=prev_id:
        prev_id = row['store_id']
        prev_per = row['period_id']
        allDuration =np.array([1])
        sum=row['sales_volume']
        # sum=0
        tempSum = 0
        allCount=count
        count = 1
        duration = 1
    elif row['period_id']-prev_per==1 and row['store_id']==prev_id:
        prev_per = row['period_id']
        duration+=1
        allDuration[count-1]=duration
        tempSum += row['sales_volume']
        sum+=tempSum
        allCount=count
    return np.array2string(allDuration)+'_'+str(allCount)+'_'+str(round(sum,2))

data['allDuration']=data.apply(lambda row: func(row), axis=1)

def splt1(row):
    return row.split('_')[0].replace('[','').replace(']','')+' '
def splt2(row):
    return int(row.split('_')[1])
def splt3(row):
    return float(row.split('_')[2])

data['allCount']=data['allDuration'].apply(lambda row: splt2(row))
data['sum']=data['allDuration'].apply(lambda row: splt3(row))
data['allDuration']=data['allDuration'].apply(lambda row: splt1(row))

data=data.drop_duplicates(subset='store_id',keep='last')

print(np.sum(data['allCount'])) #1. Общее количество промопериодов (во всех магазинах)
print(np.median(np.fromstring(np.sum(data['allDuration']),dtype=int,sep=' '))) #2. Медиана продолжительности промопериода (количество недель)
print(data['sum']) #3. Объем  продаж по каждому промопериоду
print(np.median(data['allCount'])) #4. Медиана количества промопериодов на один магазин

# data.to_csv('ansCSV.csv',index=False)
# data.to_excel('ansEx.xls',index=False)

# 1. 141158
# 2. 3
# 3. Ответ в ansCSV.csv в колонке 'sum'
# 4. 6




