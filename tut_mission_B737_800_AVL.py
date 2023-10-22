#Steps to simulate the aircraft’s performance over a mission
#Locate the folder where you have the tutorial repository. 
#If using the command line, cd to this directory.
#Open the tut_mission_B737_AVL.py script in your favorite editor or IDE.
aerodynamics = SUAVE.Analyses.Aerodynamics.AVL() 
#Excluding the functions tut_mission_B737_AVL.py script, all of the subroutine 
#python scripts described below are located in the SUAVE/Methods/Aerodynamics/AVL repository.
aerodynamics.settings.number_spanwise_vortices  = 5

#Defining Flight Conditions
#This is done in the translate_data.py script which translates flight conditions parameters defined in the mission_setup() to an AVL data structure to be used in run cases. This script also stores AVL results into SUAVE’s results data structures.

#Writing Run Cases
#Uses information in the AVL run case data structure created in translate_data.py 
#to write an AVL format run case to be used by the AVL executable. This is done in write_run_cases.py script.
#Reading Results
#Opens saved AVL result files and stores data in a data structure used to create aerodynamic and stability surrogate models. 
#This is done in read_results.py script.
Downloading AVL
#The tutorial assumes that AVL is available on your machine and can be called using 
#just “avl” in the command line. 

