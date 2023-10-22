#Space-manipulation
#!/usr/bin/python3

from qutip import *
#This will load all of the user available functions. Often, we also need to import the NumPy and Matplotlib libraries with:
import numpy as np
import matplotlib.pyplot as plt

# Space manipulation with tensors and matrix in quantum mechanics
>>> C = qeye([4])
>>> E = qeye)[6])
>>> to_super(tensor(C, E)).dims #DIMENSIONS
>>> tensor(to_super(C), to_super(B)).dims

#The qutip.tensor.super_tensor function performs the needed rearrangement, providing the most direct analog to qutip 
tensor on the underlying Hilbert space. In particular.
#for any two type="oper" Qobjs A and B, to_super(tensor(A, B)) == super_tensor(to_super(A), to_super(B))
>>> super_tensor(to_super(C), to_super(E).dims
>>> composite(C, E).dims
>>> composite(to_super(C), to_super(E)).dims
#general tensor manipulations that are useful for converting between superoperator representations [WBC11]. In particular, the tensor_contract function allows for contracting one or more pairs of indices. 
As detailed in the channel contraction tutorial.

#Generic tensor manipulations sample
>>> tensor_contract(composite(to_super(A), to_super(B)), (1, 3), (4, 6)).dims
[[[2], [2]], [[3], [3]]]

#Further analysis datasets
https://qutip.readthedocs.io/en/latest/guide/guide-saving.html#storing-and-loading-datasets
