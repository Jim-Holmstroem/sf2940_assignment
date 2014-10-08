from __future__ import division, print_function

from sympy import S, apart, summation


k = S('k')
k_domain = (k, 1, 00)

f_Y = 18/((k+1)*(k+2)*(k+3))


print(
    " = ".join([
        f_Y,
        apart(f_Y)
    ])
)

EY = summation(
    f_Y,
    k_domain
)

print(
    "E[Y] = {}".format(
        EY
    )
)
