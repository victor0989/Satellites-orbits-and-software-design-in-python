#altitude, air speed, and distance are the necessary inputs. 
#If the user does not specify an altitude, it will be taken automatically from the last value in the previous segment.

self.altitude  = None
		self.air_speed = 10. * Units['km/hr']
		self.distance  = 10. * Units.km
		
#The other set of segment specific initial values are the values used for solving the segment 
#(typically this means satisfying a force balance at every evaluation point). 
#These can be changed by the user if needed, but the default values should perform fine for most cases.

self.state.unknowns.throttle   = ones_row(1) * 0.5
		self.state.unknowns.body_angle = ones_row(1) * 0.0
		self.state.residuals.forces    = ones_row(2) * 0.0

#Mission Setup
#Initializes default values for unknowns
#Initializes set of functions used to determine residuals
#Reads user input for segment parameters
#This still uses 2D force balance but changes the profile.
#For this case, altitude, air speed, and distance are the necessary inputs. 
self.altitude  = None
		self.air_speed = 10. * Units['km/hr']
		self.distance  = 10. * Units.km
		
##he values used for solving the segment (typically this means satisfying a force balance at every evaluation point). 
#These can be changed by the user if needed, but the default values should perform fine for most cases.

self.state.unknowns.throttle   = ones_row(1) * 0.5
		self.state.unknowns.body_angle = ones_row(1) * 0.0
		self.state.residuals.forces    = ones_row(2) * 0.0
		
#Multiple segments can be run sequentially by appending them in the desired order. 
#Process Summary
#Mission Setup

#Initializes default values for unknowns
#Initializes set of functions used to determine residuals
#Reads user input for segment parameters
#Adds the analysis group to be used (including the vehicle and items like atmosphere)
#Appends segments in order
#Evaluate

def initialize_conditions(segment,state):
		
		# unpack
		climb_rate = segment.climb_rate
		air_speed  = segment.air_speed   
		alt0       = segment.altitude_start 
		altf       = segment.altitude_end
		t_nondim   = state.numerics.dimensionless.control_points
		conditions = state.conditions  
		
		# check for initial altitude
		if alt0 is None:
			if not state.initials: raise AttributeError('initial altitude not set')
			alt0 = -1.0 * state.initials.conditions.frames.inertial.position_vector[-1,2]
		
		# discretize on altitude
		alt = t_nondim * (altf-alt0) + alt0
		
		# process velocity vector
		v_mag = air_speed
		v_z   = -climb_rate # z points down
		v_x   = np.sqrt( v_mag**2 - v_z**2 )
		
		# pack conditions    
		conditions.frames.inertial.velocity_vector[:,0] = v_x
		conditions.frames.inertial.velocity_vector[:,2] = v_z
		conditions.frames.inertial.position_vector[:,2] = -alt[:,0] # z points down
		conditions.freestream.altitude[:,0]             =  alt[:,0] # positive altitude in this context


#Adds the analysis group to be used (including the vehicle and items like atmosphere)
#Appends segments in order

#Evaluate variables
#Varies unknowns until residual convergence is reached using scipy’s fsolve
		
