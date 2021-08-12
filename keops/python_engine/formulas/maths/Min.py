from keops.python_engine.formulas.Operation import Operation
from keops.python_engine.formulas.maths.ArgMin import ArgMin
from keops.python_engine.formulas.maths.OneHot import OneHot
from keops.python_engine.utils.code_gen_utils import c_for_loop, c_if, value


############################
######    Min       #####
############################

class Min(Operation):
    string_id = "Min"

    def __init__(self, f):
        super().__init__(f)
        if f.dim < 1:
            raise ValueError("[KeOps] Min operation is only possible when dimension is non zero.")
        self.dim = 1

    def Op(self, out, table, arg):
        loop, k = c_for_loop(1, f.dim, 1, pragma_unroll=True)  # TODO : Fix this
        string = value(out).assign(arg[0])
        string += loop(c_if(arg[k] < value(out), value(out).assign(arg[k])))
        return string

    def DiffT(self, v, gradin):
        return f.DiffT(v, OneHot(ArgMin(f), f.dim) * gradin)




# TODO : transcript half2 implementation below

"""
#if USE_HALF && GPU_ON
  static DEVICE INLINE void Operation(half2 *out, half2 *outF) {
    *out = outF[0];
    #pragma unroll
    for (int k = 1; k < F::DIM; k++) {
      // we have to work element-wise...
      __half2 cond = __hgt2(*out,outF[k]);                 // cond = (out > outF[k]) (element-wise)
      __half2 negcond = __float2half2_rn(1.0f)-cond;       // negcond = 1-cond
      *out = cond * outF[k] + negcond * *out;              // out  = cond * outF[k] + (1-cond) * out
    }
  }
#endif

"""