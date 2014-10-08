from sympy import *

k = S('k')

pfrac=18/((k+1)*(k+2)*(k+3))

print(
    "{}={}".format(
        pfrac,
        apart(pfrac)
    )
)

#R1, R2, R3 = S('R1 R2 R3'.split())
#
#print(
#    solve(
#        [  # FIXME seems to be wrong, must have missed the equation system
#            Eq(18, 6*R1+3*R2+2*R3), #constant
#            Eq( 0, 6*R1+4*R2+3*R3), #k
#            Eq( 0,   R1+  R2+  R3), #k^2
#        ]
#    )
#)
