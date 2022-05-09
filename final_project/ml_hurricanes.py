'''
Program: Hurricane Predictor
Author: Sean Nesamoney
Course: AT Computer Science
Date (last modified): May 2, 2022
'''
import csv

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.image as mpimg
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


'''Visualize Data'''
data = pd.read_csv("hurricanes2020.csv")
states_data = pd.read_csv("us_states_data.csv")
x_1 = data["lat_1"]
x_2 = data["long_1"]
y = data["mx_sustained_winds"]
y = pd.Series([int(char.split()[0]) for char in y])
#print(temp)Border Security and Immigration Enforcement Improvements
# for i in y:
#     print(i.split())

#CREDITS: https://www.protechtraining.com/blog/post/python-for-beginners-reading-manipulating-csv-files-737
f = open("us_states_data.csv")
csv_f = csv.reader(f)

#MAKE THIS A FUNCTION - SEARCHING FOR ITEM
state = input("Enter your state:\n")
lat_in = states_data.loc[states_data["state"] == state]['latitude']
long_in = states_data.loc[states_data["state"] == state]['longitude']
# print(lat_in.values)
# print(lat_in.values[0])
# print(long_in.values)


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
#print(y_test)

#Create model on training data
model = LinearRegression().fit(x_train, y_train)

#Print out model information
print("Model Information:")
print("Latitude Coef", model.coef_[0])
print("Longitude Coef", model.coef_[1])
print("Intercept:", model.intercept_)
print()

'''Compare to test data'''
# Get the predicted y values for the x_test value
# predictions = model.predict(x_test)

# '''User input'''
# lat = float(input("What is the latitude of your region (in degree coordinates)?\n"))
# long = float(input("What is the longitude of your region (in degree coordinates)?\n"))
# x_pred = [[lat, long]]

x_pred = [[lat_in.values[0], long_in.values[0]]]

#Get prediction with user input
predictions = model.predict(x_pred)
#print(predictions[0])
y_pred = predictions[0]

#Compare actual and predicted values
print("Predicting Wind Speed:")



#Test x values
# x_precipitation = x_test[index][0]
# x_winter = x_test[index][1]
x_lat = lat_in
x_long = long_in
print("Latitude:", lat_in.values[0])
print("Longitude:", long_in.values[0])
print("Predicted Max Wind:", y_pred)

