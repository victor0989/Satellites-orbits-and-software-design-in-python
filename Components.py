#Network scripts are the link between these components. 
#The network script allows you to reconfigure the connection between components to create your dream propulsion system.
#These must be logically created as components have set inputs and outputs.s

# step 1
solar_flux.solar_radiation(conditions)
# link
solar_panel.inputs.flux = solar_flux.outputs.flux
# step 2
solar_panel.power()
# link
solar_logic.inputs.powerin = solar_panel.outputs.power

# suave imports
import SUAVE

from SUAVE.Components.Energy.Energy_Component import Energy_Component

# ----------------------------------------------------------------------
#  Solar_Panel Class
# ----------------------------------------------------------------------
class Solar_Panel(Energy_Component):

def __defaults__(self):
	self.area       = 0.0
	self.efficiency = 0.0

def power(self):
	
	# Unpack
	flux       = self.inputs.flux
	efficiency = self.efficiency
	area       = self.area
	
	p = flux*area*efficiency
	
	# Store to outputs
	self.outputs.power = p

	return p
