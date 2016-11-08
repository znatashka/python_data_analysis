# coding=utf-8
import matplotlib.pyplot as plt
import scipy as sp

from koelyo_scipy_common import x, y, error

inflection = 3.5 * 7 * 24  # вычислить положение точки в часах
xa = x[:inflection]  # данные до точки изгиба
ya = y[:inflection]

xb = x[inflection:]  # данные после неё
yb = y[inflection:]

fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))

fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)
print 'Error inflection=%f' % float(fa_error + fb_error)

fxa = sp.linspace(0, xa[-1], 1000)
plt.plot(fxa, fa(fxa), linewidth=3)

fxb = sp.linspace(500, xb[-1], 1000)
plt.plot(fxb, fb(fxb), '-.', linewidth=3)

plt.legend(["d=%i" % fa.order, "d=%i" % fb.order], loc="upper left")
plt.show()
