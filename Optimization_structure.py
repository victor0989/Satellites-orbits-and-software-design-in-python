#Standard Optimization File Structure
#These are the standard files that are used in the optimization process. 
#They are typically stored as Optimize.py, Vehicle.py, Analysis.py, Mission.py, Procedure.py, and Plot_Mission.py. 

#ater functions with the information needed to vary the parameters. Units.less indicates a unitless quantity. 
#SI units are the default in SUAVE’s internal calculations, 
#so Units.meter will not modify the internal value, while something like Units.foot will.
problem.inputs = np.array([
[ 'wing_area'     ,  125.  , (   120.   ,   180.   )  ,   100.  , Units.meter**2],
[ 'aspect_ratio'  ,  3.3   , (   2.0    ,   6.0    )  ,   10.   , Units.less],
])
#Constraints and the objective are similar. Both have scaling quantities and constraints also have bounds.
problem.constraints = np.array([
[ 'design_range_fuel_margin', '>', 0., 1E-1, Units.less]
])

problem.objective = np.array([
['fuel_burn_rate', 1., Units.kg/Units.s]
])
#Finally we have aliases. This provides the optimization process with the position of the various parameters in the data structure.
#Vehicle Setup
#This contains the vehicle information such as geometric data and configurations. 
#It is the same as the vehicle setup used for basic analysis purposes.
#Analysis Setup 
#This contains information on what analyses should be run for the vehicle. 
def set_fidelity_level(nexus):

if nexus.has_key('fidelity_level') == False:
	print 'Fidelity level not set, defaulting to 1'
	nexus.fidelity_level = 1

if nexus.fidelity_level == 2:
	aerodynamics = SUAVE.Analyses.Aerodynamics.Supersonic_OpenVSP_Wave_Drag()
	aerodynamics.settings.number_slices    = 20
	aerodynamics.settings.number_rotations = 10        
elif nexus.fidelity_level == 1:
	aerodynamics = SUAVE.Analyses.Aerodynamics.Supersonic_Zero()
else:
	raise ValueError('Selected fidelity level not supported')
aerodynamics.geometry = copy.deepcopy(nexus.vehicle_configurations.base)
nexus.analyses.base.append(aerodynamics)

nexus.missions = mission_as2.setup(nexus.analyses)
return nexus
