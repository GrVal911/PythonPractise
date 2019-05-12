import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('for_analyst.csv')

# print(len(set(data['id'])))
# print(len(data))

data=data.drop_duplicates(subset='id', keep='last')

# regage=data.sort_values(by=['regage'])['regage']
# visits=data.sort_values(by=['regage'])['visits']

# corr=data['regage']/data['visits']
# print(sorted(corr))
# print(np.mean(sorted(corr)))
# print(np.median(sorted(corr)))
# n=np.arange(0,len(corr),1)
# fig, ax = plt.subplots()
# ax.plot(n, regage,'r')
# ax.plot(n, visits,'g')
# ax.plot(n, sorted(corr),'b')
# ax.grid()
# plt.show()

# lvl=sorted(set(data['level']))
# print(len(lvl))
# print(data.groupby('level')['regage'].transform(np.median),data['level'])
# data['med']=data.groupby('level')['regage'].transform(np.median)
# lvl=data.drop_duplicates(subset='level', keep='last')
# lvl=lvl.sort_values(by=['level'])
# print(lvl)

# fig, ax = plt.subplots()
# index = np.arange(len(lvl))
# rects1 = ax.bar(index, lvl['med'])
# ax.set_xticklabels(lvl['level'])
# fig.tight_layout()
# plt.show()

count=data.groupby(['geo_country', 'site']).size().reset_index(name='counts')
# print(count)
count=count.sort_values(by=['site'])
six,nine=count.groupby(['site'])['site'].count()
print(six,nine)

# print(count.loc[:])
s6=count.iloc[:six,:]['counts']
s6c=count.iloc[:six,:]['geo_country']
s9=count.iloc[six:,:]['counts']
s9c=count.iloc[six:,:]['geo_country']
# print(len(s9))
# print(set(data['site']))
# count=data.drop_duplicates(subset='geo_country',keep='first')
# count=count.dropna(subset=['count'])
# print(data)

fig, ax = plt.subplots()
groupgap=1
index1 = np.arange(len(s6))
index2 = np.arange(len(s9))+groupgap+len(s6)
bar_width = 1
rects1 = ax.bar(index1, s6, bar_width,color='r',  edgecolor= "black",label="site 6")
rects2 = ax.bar(index2, s9, bar_width,color='b',  edgecolor= "black",label="site 9")
# ax.set_xticklabels(s6c)
fig.tight_layout()
plt.show()

# print(data.groupby(['sex'])['id'].count())
# print(np.median(data['age']))