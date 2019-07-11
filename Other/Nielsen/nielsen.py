import numpy as np
import pandas as pd

data=pd.read_csv('milk_promo_sales.csv')
unq=np.unique(data['store_id']) #ID всех магазинов
allDuration=np.array(np.empty(0,dtype=int))
allCount=np.array(np.empty(0,dtype=int))
sum=np.array(np.empty(0,dtype=int))
for unique in unq: #Просмотр промопериодов по каждому магазину
    data = pd.read_csv('milk_promo_sales.csv')
    data=data.loc[data['store_id']==unique] # Оставляем данные только о текущем магазине
    data=data.sort_values(by=['period_id']) #Сортируем недели по порядку
    # print(data)
    count=1
    duration=1
    strt=0
    for i in range(len(data)-1):
        if data.iloc[i+1,1]-data.iloc[i,1]>1: # Если промопериод закончился
            count+=1
            allDuration=np.append(allDuration,duration) #Записываем длительность текущего промопериода
            duration=1
            sum=np.append(sum,np.sum(data.iloc[strt:i+1,2])) #Записываем объем продаж в течение данного промопериода
            strt = i + 1 # Запоминаем начало следующего промопериода
        else:
            duration+=1
    allDuration=np.append(allDuration,duration) #Записываем данные о последнем промопериоде для данного магазина
    sum=np.append(sum,np.sum(data.iloc[strt:len(data),2]))
    allCount=np.append(allCount,count)
    # print(allCount)
    # print(allDuration)
    # print(sum)

print(np.sum(allCount)) #1. Общее количество промопериодов (во всех магазинах)
print(np.median(allDuration)) #2. Медиана продолжительности промопериода (количество недель)
print(sum) #3. Объем  продаж по каждому промопериоду
print(np.median(allCount)) #4. Медиана количества промопериодов на один магазин


