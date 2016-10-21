# coding=utf-8
import json

import matplotlib.pyplot as plt
from pandas import DataFrame, Series, np

path = 'data/usagov_bitly_data2013-05-17-1368832207'
records = [json.loads(line) for line in open(path)]

frame = DataFrame(records)

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'

tz_counts = clean_tz.value_counts()

tz_counts[:10].plot(kind='barh', rot=0)
plt.show()  # Первые 10 часовых поясов из набора 1.usa.gov

results = Series([x.split()[0] for x in frame.a.dropna()])
cframe = frame[frame.a.notnull()]

operating_systems = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
by_tz_os = cframe.groupby(['tz', operating_systems])
agg_counts = by_tz_os.size().unstack().fillna(0)

# Нужен для сортировке в порядке возрастания
indexer = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(indexer)[-10:]

count_subset.plot(kind='barh', stacked=True)
plt.show()  # Первые 10 часовых поясов с выделением пользователей Windows и прочих

normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
plt.show()  # Процентная доля пользователей Windows и прочих в первых 10 часовых поясах
