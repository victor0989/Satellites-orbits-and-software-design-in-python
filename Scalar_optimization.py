#Key Functions
#PyOpt setup
#Scalar optimization

inp = problem.optimization_problem.inputs
obj = problem.optimization_problem.objective
con = problem.optimization_problem.constraints  

# Set inputs
nam = inp[:,0] # Names
ini = inp[:,1] # Initials
bnd = inp[:,2] # Bounds
scl = inp[:,3] # Scale
typ = inp[:,4] # Type
from SUAVE.Optimization import helper_functions as help_fun

bnd_constraints    = help_fun.scale_const_bnds(con)
scaled_constraints = help_fun.scale_const_values(con,bnd_constraints)
x                  = ini/scl
#What happens next is entirely dependent on what optimizer you want to use. 
#Some may require that constraint bounds happen at 0 or are either > or <. 
#However this setup is done, you will likely need to create a function that can accept the problem and inputs and give required 
#outputs such as the objective value and constraints. In the PyOpt case, this is done with a simple wrapper and an added function:
mywrap = lambda x:PyOpt_Problem(problem,x)
…

def PyOpt_Problem(problem,x):

	obj   = problem.objective(x)
	const = problem.all_constraints(x).tolist()
	fail  = np.array(np.isnan(obj.tolist()) or np.isnan(np.array(const).any())).astype(int)


	print 'Inputs'
	print x
	print 'Obj'
	print obj
	print 'Con'
	print const

	return obj,const,fail
