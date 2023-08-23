import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

#print(london_data.head())

print(len(london_data))

temp = london_data["TemperatureC"]

average_temp = np.mean(temp)
print(average_temp)

temperature_var = np.var(temp)
print(temperature_var)

temperature_standard_deviation = np.std(temp)
print(temperature_standard_deviation)

june = london_data.loc[london_data["month"] == 6 ]["TemperatureC"]
july  = london_data.loc[london_data["month"] == 7 ]["TemperatureC"]

june_mean = np.mean(june)
july_mean = np.mean(july)

print(june_mean)
print(july_mean)

june_std = np.std(june)
july_std = np.std(july)

print(june_std)
print(july_std)

for i in range(1,13):
  month_data = london_data.loc[london_data["month"] == i ]["TemperatureC"]
  print(" the average temperature for " + str(i) + " is " + str(np.mean(month_data)) + " with a Standar Deviation of " + str(np.std(month_data)) )


