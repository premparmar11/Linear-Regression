# import libraries
from builtins import len, range

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read data
data = pd.read_csv("../Data/CelsiusToFahrenheit.csv")

# data.shape gives total rows and columm of data in form of (rows, columm)
print(data.shape)

# To show top 5 rows
print(data.head())

x = data["Celsius"]
y = data["Fahrenheit"]

# avg value of dependent and independent variables
mean_x = np.mean(x)
mean_y = np.mean(y)

# total nunmber of values
n = len(x)

numer = 0
denom = 0
for i in range(n):
    numer += (x[i] - mean_x) * (y[i] - mean_y)
    denom += (x[i] - mean_x) ** 2

b1 = numer/denom
b0 = mean_y - (b1 * mean_x)

print (b1 , b0)

# plotting values and regression line

max_x = np.max(x)
min_x = np.min(x)

# calculating line values x and y
x = np.linspace(min_x, max_x)
y = b0 + b1 * x

# plotting line
plt.plot(x, y, color="#58b970", label="Regression Line")
# plotting scatter points
plt.scatter(x, y, c="#ef5423", label="Scatter Plot")

plt.xlabel("Celsius")
plt.ylabel("Fahreheit")
plt.legend()
plt.show()