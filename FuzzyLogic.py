import numpy as np
import skfuzzy as fuzz

#ask user for input
user_input = input("Enter a value between 0 and 10: ")
input_value = float(user_input)

#input variables
x = np.arange(0, 11, 1) #input range from 0 to 10

#define fuzzy sets for the input variable
low = fuzz.trimf(x, [0, 0, 5]) #triangular fuzzy set for low values
medium = fuzz.trimf(x, [2, 5, 8]) #triangular fuzzy set for medium values
high = fuzz.trimf(x, [5, 10, 10]) #triangular fuzzy set for high values

#get membership values for input_value
low_degree = fuzz.interp_membership(x, low, input_value)
medium_degree = fuzz.interp_membership(x, medium, input_value)
high_degree = fuzz.interp_membership(x, high, input_value)

#define fuzzy rules
rule1 = np.fmax(low_degree, medium_degree) #Rule: If input is low or medium, then output is high
rule2 = np.fmin(medium_degree, high_degree) #Rule: If input is medium or high, then output is low

#Apply fuzzy rules to determine the fuzzy relation between input and output
relation = np.fmax(rule1, rule2)

#aggregate the fuzzy relation using the maximum operator 
aggregated = np.fmax(low, relation)
activated = np.fmin(aggregated, medium)

#Defuzzify the relation to obtain a crisp output
output = fuzz.defuzz(x, activated, 'centroid')

#Display the crisp output
print("Output: ", output)