# coding=utf-8
import matplotlib.pyplot as plt
import pandas as pd

from pandas import np

years = range(1880, 2016)
pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'data/names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc='sum')
total_births.plot(title='Total births by sex and year')
plt.show()


def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group


names = names.groupby(['year', 'sex']).apply(add_prop)
print np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)


def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]


grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc='sum')
subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title='Number of births per year')
plt.show()

table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc='sum')
table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
plt.show()


def get_quantile_count(group, q=0.5):
    group = group.sort_values(by='prop', ascending=False)
    return group.prop.cumsum().searchsorted(q)[0] + 1


diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')

print diversity.head()
diversity.plot(title='Number of popular names in top 50%')
plt.show()

# TODO Makkinni_U__-_Python_i_analiz_dannykh_-_2015 стр 52
