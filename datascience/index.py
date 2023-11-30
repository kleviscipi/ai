import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

health_data = pd.read_csv("health.csv", header=0, sep=",")

health_data.dropna(axis=0,inplace=True)

print(health_data)

print(health_data.info())

health_data['Average_Pulse'] = health_data['Average_Pulse'].astype(float)
health_data['Max_Pulse'] = health_data['Max_Pulse'].astype(float)

print(health_data.info())

print(health_data.describe())

# health_data.plot(kind='line', x='Average_Pulse', y='Calorie_Burnage')
# plt.ylim(ymin=0)
# plt.xlim(xmin=0)
# plt.show()


# Find the slope and intercept of the line

x = health_data['Average_Pulse']
y = health_data['Calorie_Burnage']

slope_intercept = np.polyfit(x,y,1)

print(slope_intercept)

# Find the 10 % Max_Pulse

Max_Pulse = health_data['Max_Pulse']
percetile_10 = np.percentile(Max_Pulse,10)

print(percetile_10)