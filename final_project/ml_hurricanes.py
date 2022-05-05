'''
Program: Hurricane Predictor
Author: Sean Nesamoney
Course: AT Computer Science
Date (last modified): May 2, 2022
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.image as mpimg
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''Visualize Data'''
data = pd.read_csv("hurricanes2020.csv")
x_1 = data["lat_1"]
x_2 = data["long_1"]
y = data["mx_sustained_winds"]
y = pd.Series([int(char.split()[0]) for char in y])
#print(temp)
# for i in y:
#     print(i.split())

fig, graph = plt.subplots(2)
graph[0].scatter(x_1, y)
graph[0].set_xlabel("lat_1")
graph[0].set_ylabel("mx_sustained_winds")

graph[1].scatter(x_2,y)
graph[1].set_xlabel("long_1")
graph[1].set_ylabel("mx_sustained_winds")

print("Corr between Latitude and Max. Wind", x_1.corr(y))
print("Corr between Longitude and Max. Wind", x_2.corr(y))

plt.tight_layout()
#plt.show()
'''3d Graph'''
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# ax.set_xlabel("Latitude")
# ax.set_ylabel("Longitude")
# ax.set_zlabel("Wind Speed")
# ax.scatter(x_1[:, 0], x_2[:, 1], y[:, 2])
# plt.show()

'''Create Multiple Linear Regression Model'''
#Organize data into correct format
x = data[["lat_1", "long_1"]].values
y = y.values
# print(x)
# print(y)

#Separate data into train/test set
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2)
print(y_test)

#Create model on training data
model = LinearRegression().fit(x_train, y_train)

#Print out model information
print("Model Information")
print("Latitude Coef", model.coef_[0])
print("Longitude Coef", model.coef_[1])
print("Intercept:", model.intercept_)
print()

'''Compare to test data'''
# Get the predicted y values for the x_test value
# predictions = model.predict(x_test)

'''User input'''
lat = float(input("What is the latitude of your region (in degree coordinates)?\n"))
long = float(input("What is the longitude of your region (in degree coordinates)?\n"))

x_pred = [[lat, long]]

#Get prediction with user input
predictions = model.predict(x_pred)
#print(predictions[0])
y_pred = predictions[0]

#Compare actual and predicted values
print("Predicting Wind Speed:")



#Test x values
# x_precipitation = x_test[index][0]
# x_winter = x_test[index][1]
x_lat = lat
x_long = long
print("Latitude:", lat)
print("Longitude:", long)
print("Predicted Max Wind:", y_pred)

