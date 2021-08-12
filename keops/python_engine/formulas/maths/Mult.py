from keops.python_engine.formulas.Operation import Broadcast
from keops.python_engine.formulas.VectorizedScalarOp import VectorizedScalarOp
from keops.python_engine.formulas.maths.Scalprod import Scalprod
from keops.python_engine.formulas.variables.Zero import Zero
from keops.python_engine.utils.math_functions import keops_mul


##########################
######    Mult       #####
##########################


class Mult_Impl(VectorizedScalarOp):
    """the binary multiply operation"""

    string_id = "Mult"
    print_spec = "*", "mid", 3

    ScalarOpFun = keops_mul

    #  \diff_V (A*B) = (\diff_V A) * B + A * (\diff_V B)
    def DiffT(self, v, gradin):
        fa, fb = self.children
        if fa.dim == 1 and fb.dim > 1:
            return fa.DiffT(v, Scalprod(gradin, fb)) + fb.DiffT(v, fa * gradin)
        elif fb.dim == 1 and fa.dim > 1:
            return fa.DiffT(v, fb * gradin) + fb.DiffT(v, Scalprod(gradin, fa))
        else:
            return fa.DiffT(v, fb * gradin) + fb.DiffT(v, fa * gradin)
            
    
    # parameters for testing the operation (optional)
    nargs = 2                   # number of arguments
    torch_op = "torch.mul"      # equivalent PyTorch operation


# N.B. The following separate function should theoretically be implemented
# as a __new__ method of the previous class, but this can generate infinite recursion problems
def Mult(arg0, arg1):
    if isinstance(arg0, Zero):
        return Broadcast(arg0, arg1.dim)
    elif isinstance(arg1, Zero):
        return Broadcast(arg1, arg0.dim)
    elif isinstance(arg1, int):
        from keops.python_engine.formulas.variables.IntCst import IntCst

        return Mult(IntCst(arg1), arg0)
    else:
        return Mult_Impl(arg0, arg1)
