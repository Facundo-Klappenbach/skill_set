# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars." )
  return estimated_cost

# Initial variables for Maria 
# Estimate Maria's insurance cost
maria_insurance_cost  = calculate_insurance_cost(28, 0, 26.2, 3, 0, "Maria")

# Initial variables for Omar
# Estimate Omar's insurance cost 
omar_insurance_cost  = calculate_insurance_cost(35, 1, 22.2, 0, 1, "Omar")

# Estimate Facundo's insurance cost
facundo_insurance_cost  = calculate_insurance_cost(27, 1, 30.2, 0, 0, "Facundo")

# Calculate differencebetween insurance cost
def difference_in_costs(insurance_cost_uer_1, insurance_cost_uer_2):
  difference_insurance_cost = insurance_cost_uer_1 - insurance_cost_uer_2
  print("The difference in insurance cost is " + str(difference_insurance_cost) + " dollars.")

difference_in_costs(omar_insurance_cost,facundo_insurance_cost)
