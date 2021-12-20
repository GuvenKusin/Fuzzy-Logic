#Setting tips with fuzzy logic
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Inputs and Outputs are Defined..!
quality=ctrl.Antecedent(np.arange(0,11,1), "Quality")
# Give quality grade in the range of 0-10

service=ctrl.Antecedent(np.arange(0,11,1), "Service") #Do the same for the service
tip=ctrl.Consequent(np.arange(0,26,1), "Tip") #Sets the tip rate in the range of 0-25

#Determination of membership functions for input values ​​(automatically determined..!)
quality.automf(3) #We get 3 as we have 3 output values
service.automf(3)

#Determination of membership functions for output values ​​(determined manually..!)
tip["Greedy"] = fuzz.trimf(tip.universe, [0,0,13])
tip["General"] = fuzz.trimf(tip.universe,[0,13,25])
tip["Generous"] =fuzz.trimf(tip.universe,[13,25,25])

#Determining Fuzzy Logic Rules..!
rule1=ctrl.Rule(quality["good"] | service["good"], tip["Generous"])
rule2=ctrl.Rule(service["average"], tip["General"])
rule3=ctrl.Rule(service["poor"] | quality["poor"], tip["Greedy"])

#Determining the Tip..!
tipControl=ctrl.ControlSystem([rule1, rule2, rule3])
tipset=ctrl.ControlSystemSimulation(tipControl)

#Calculating the Tip..!
tipset.input["Quality"] = 5.8