# coding=utf-8
import matplotlib.pyplot as plt
import numpy
import scipy as sp

from koelyo_scipy_common import x, y, error

print sp.version.full_version

# todo Изучаем SciPy
print sp.dot is numpy.dot

# todo Выбор подходящей модели и обучающего алгоритма
# вариант 1 - линейная функция
f1p, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
print 'Параметры модели: %s' % f1p
print residuals
f1 = sp.poly1d(f1p)
print error(f1, x, y)

fx = sp.linspace(0, x[-1], 1000)  # сгенерировать значения Х для трафика
plt.plot(fx, f1(fx), linewidth=3)
# plt.legend(["d1=%i" % f1.order], loc="upper left")
# plt.show()

# вариант 2 - полином степени 2
f2p = sp.polyfit(x, y, 2)
f2 = sp.poly1d(f2p)
print error(f2, x, y)

fx2 = sp.linspace(0, x[-1], 1000)
plt.plot(fx2, f2(fx2), linewidth=3)
# plt.legend(["d=%i" % f1.order, "d=%i" % f2.order], loc="upper left")
# plt.show()

# вариант 3 - полином степени 3
f3p = sp.polyfit(x, y, 3)
f3 = sp.poly1d(f3p)
print error(f3, x, y)

fx3 = sp.linspace(0, x[-1], 1000)
plt.plot(fx3, f3(fx3), linewidth=3)

# вариант 4 - полином степени 10
f10p = sp.polyfit(x, y, 10)
f10 = sp.poly1d(f10p)
print error(f10, x, y)

fx10 = sp.linspace(0, x[-1], 1000)
plt.plot(fx10, f10(fx10), linewidth=3)

# вариант 5 - полином степени 100
f100p = sp.polyfit(x, y, 100)
f100 = sp.poly1d(f100p)
print error(f100, x, y)

fx100 = sp.linspace(0, x[-1], 1000)
plt.plot(fx100, f100(fx100), linewidth=3)

plt.legend(["d=%i" % f1.order, "d=%i" % f2.order, 'd=%i' % f3.order, 'd=%i' % f10.order, 'd=%i' % f100.order],
           loc="upper left")
plt.show()
