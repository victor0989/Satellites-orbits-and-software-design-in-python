#  Component 3 - Low Pressure Compressor

# instantiate 
compressor = SUAVE.Components.Energy.Converters.Compressor()    
compressor.tag = 'low_pressure_compressor'

# setup
compressor.polytropic_efficiency = 0.91
compressor.pressure_ratio        = 1.14    

# add to network
turbofan.append(compressor)
