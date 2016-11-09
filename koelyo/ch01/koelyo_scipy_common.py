# coding=utf-8
import matplotlib.pyplot as plt
import scipy as sp


def error(f, x1, y1):
    return sp.sum((f(x1) - y1) ** 2)


# todo Чтение данных
data = sp.genfromtxt('ch01/data/web_traffic.tsv', delimiter='\t')
print data[:10]
print data.shape

# todo Предварительная обработка и очистка данных
x = data[:, 0]
y = data[:, 1]

print sp.sum(sp.isnan(y))

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

# представляем точки (x, y) кружочками диаметра 10
plt.scatter(x, y, s=5)
plt.title('Web traffic over the last month')
plt.xlabel('Time')
plt.ylabel('Hits/hour')
plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
# рисуем полупрозрачную сетку пунктирными линиями
plt.grid(True, linestyle='-', color='0.75')

# plt.show()
