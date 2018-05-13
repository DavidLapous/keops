import os.path
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)

#--------------------------------------------------------------#
#                     Standard imports                         #
#--------------------------------------------------------------#
import torch
from torch          import Tensor
from torch.autograd import grad
from pykeops.torch.kernels import Kernel, kernel_product

#--------------------------------------------------------------#
#                   Convenience functions                      #
#--------------------------------------------------------------#
def scal_to_var(x) :
    "Turns a float into a length-1 tensor, that can be used as a parameter."
    return torch.tensor([x], requires_grad=True, device=device)

def scalprod(x, y) :
    "Simple L2 scalar product."
    return torch.dot(x.view(-1), y.view(-1))

#--------------------------------------------------------------#
#                   Define our dataset                         #
#--------------------------------------------------------------#
npoints_x, npoints_y = 100, 700
dimpoints, dimsignal =   3,   1

# Choose the storage place for our data : CPU (host) or GPU (device) memory.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# N.B.: PyTorch's default dtype is float32
a = torch.randn(npoints_x,dimsignal, requires_grad=True, device=device)
x = torch.randn(npoints_x,dimpoints, requires_grad=True, device=device)
y = torch.randn(npoints_y,dimpoints, requires_grad=True, device=device)
b = torch.randn(npoints_y,dimsignal, requires_grad=True, device=device)


#--------------------------------------------------------------#
#                    A first Kernel                            #
#--------------------------------------------------------------#
# N.B.: "sum" is default, "lse" is for "log-sum-exp"
modes = ["sum", "lse"] if dimsignal==1 else ["sum"]

# Wrap the kernel's parameters into a JSON dict structure
sigma = scal_to_var(-1.5)
params = {
    "id"      : Kernel("gaussian(x,y)"),
    "gamma"   : 1./sigma**2,
    "mode"    : "sum",
}


# Test, using a pytorch or keops
for mode in modes : 
    params["mode"] = mode
    print("Mode :", mode, "========================================")
    for backend in ["pytorch", "auto"] :
        params["backend"] = backend
        print("Backend :", backend, "--------------------------")

        Kxy_b  = kernel_product( params, x,y,b )
        aKxy_b = scalprod(a, Kxy_b)
        print("Kernel dot product  : ", aKxy_b )

        # Computing a gradient is that easy - we can also use the "aKxy_b.backward()" syntax. 
        # Notice the "create_graph=True", which will allow us to compute
        # higher order derivatives.
        [grad_x, grad_y, grad_s]   = grad(aKxy_b, [x, y, sigma], create_graph=True)
        print("Gradient wrt. x     : ", grad_x[:2,:] )
        print("Gradient wrt. y     : ", grad_y[:2,:] )
        print("Gradient wrt. s     : ", grad_s       )

        grad_x_norm        = scalprod(grad_x, grad_x)
        [grad_xx, grad_xy] = grad(grad_x_norm, [x,y], create_graph=True)
        print("Arbitrary formula 1 : ", grad_xx[:2,:] )
        print("Arbitrary formula 2 : ", grad_xy[:2,:] )

        grad_s_norm        = scalprod(grad_s, grad_s)
        [grad_sx, grad_ss] = grad(grad_s_norm, [x,sigma], create_graph=True)
        print("Arbitrary formula 3 : ", grad_sx[:2,:] )
        print("Arbitrary formula 4 : ", grad_ss       )



#--------------------------------------------------------------#
#                   A second, custom Kernel                    #
#--------------------------------------------------------------#
kernel              = Kernel()
kernel.features     = "locations" # we could also use "locations+directions", etc.
# Symbolic formula, for the KeOps backend
kernel.formula_sum  = "( -G*SqDist(X,Y) )"
# Pytorch routine, for the "pure pytorch" backend
kernel.routine_sum  = lambda g=None, xmy2=None, **kwargs : \
                         -g*xmy2

# Wrap it (and its parameters) into a JSON dict structure
sigma = scal_to_var(0.5)
params = {
    "id"      : kernel,
    "gamma"   : 1./sigma**2,
    "backend" : "auto",
    "mode"    : "sum",
}


# Test, using a pytorch or keops
for mode in modes : 
    params["mode"] = mode
    print("Mode :", mode, "========================================")
    for backend in ["pytorch", "auto"] :
        params["backend"] = backend
        print("Backend :", backend, "--------------------------")

        Kxy_b  = kernel_product( params, x,y,b )
        aKxy_b = scalprod(a, Kxy_b)
        print("Kernel dot product  : ", aKxy_b )

        # Computing a gradient is that easy - we can also use the "aKxy_b.backward()" syntax. 
        # Notice the "create_graph=True", which will allow us to compute
        # higher order derivatives.
        [grad_x, grad_y, grad_s]   = grad(aKxy_b, [x, y, sigma], create_graph=True)
        print("Gradient wrt. x     : ", grad_x[:2,:] )
        print("Gradient wrt. y     : ", grad_y[:2,:] )
        print("Gradient wrt. s     : ", grad_s       )

        grad_x_norm        = scalprod(grad_x, grad_x)
        [grad_xx, grad_xy] = grad(grad_x_norm, [x,y], create_graph=True)
        print("Arbitrary formula 1 : ", grad_xx[:2,:] )
        print("Arbitrary formula 2 : ", grad_xy[:2,:] )

        grad_s_norm        = scalprod(grad_s, grad_s)
        [grad_sx, grad_ss] = grad(grad_s_norm, [x,sigma], create_graph=True)
        print("Arbitrary formula 3 : ", grad_sx[:2,:] )
        print("Arbitrary formula 4 : ", grad_ss       )
