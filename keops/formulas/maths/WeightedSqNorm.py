from keops.formulas.maths.SqNormDiag import SqNormDiag
from keops.formulas.maths.SqNormIso import SqNormIso
from keops.formulas.maths.SymSqNorm import SymSqNorm


# WeightedSqNorm(A,X) : redirects to SqNormIso, SqNormDiag or SymSqNorm
# depending on dimension of A.


def WeightedSqNorm(A, X):
    if A.dim == 1:
        return SqNormIso(A, X)
    elif A.dim == X.dim:
        return SqNormDiag(A, X)
    else:
        return SymSqNorm(A, X)
