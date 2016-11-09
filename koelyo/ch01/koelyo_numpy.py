# coding=utf-8
import timeit

import numpy as np

print np.version.full_version

# todo Изучаем NumPy
a = np.array([0, 1, 2, 3, 4, 5])
print a
print a.ndim
print a.shape

b = a.reshape((3, 2))
print b
print b.ndim
print b.shape

b[1][0] = 77
print b
print a

c = a.reshape((3, 2)).copy()
print c

c[0][0] = -99
print c
print a

d = np.array([1, 2, 3, 4, 5])
print d * 2
print d ** 2

# todo Индексирование
print a[np.array([2, 3, 4])]
print a > 4
print a[a > 4]

a[a > 4] = 4
print a
print a.clip(0, 4)

# todo Обработка отсутствующих значений
c = np.array([1, 2, np.NAN, 3, 4])
print c
print np.isnan(c)
print c[~np.isnan(c)]
print np.mean(c[~np.isnan(c)])

# todo Сравнение времени работы
normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))', number=10000)
naive_np_sec = timeit.timeit('sum(na*na)', setup='import numpy as np; na=np.arange(1000)', number=10000)
good_np_sec = timeit.timeit('na.dot(na)', setup='import numpy as np; na=np.arange(1000)', number=10000)
print 'Normal Python: %f sec' % normal_py_sec
print 'Naive NumPy: %f sec' % naive_np_sec
print 'Good NumPy: %f sec' % good_np_sec

print np.array([1, 2, 3]).dtype
print np.array(['1', 'stringy']).dtype
print np.array([1, 'stringy', {1, 2, 3}]).dtype
