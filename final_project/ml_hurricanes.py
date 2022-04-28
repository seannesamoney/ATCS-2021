'''
Program: Hurricanes
Author: Sean Nesamoney
Course: AT Computer Science
Date (last modified): April 25, 2022
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''Visualize Data'''
data = pd.read_csv("data/hurricanes2020.csv")
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

'''Create Multiple Linear Regression Model'''
#Organize data into correct format
x = data[["lat_1", "long_1"]].values
y = data["mx_sustained_winds"].values

#Separate data into train/test set
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2)

#Create model on training data
model = LinearRegression().fit(x_train, y_train)

#Print out model information
print("Model Information")
print("Latitude Coef", model.coef_[0])
print("Longitude Coef", model.coef_[1])
print("Intercept:", model.intercept_)
print()

'''Compare to test data'''
#Get the predicted y values for the x_test value
predictions = model.predict(x_test)

#Compare actual and predicted values
print("Testing Linear Model with Test Data:")
for index in range(len(x_test)):
    #Actual y value
    actual = y_test[index]

    #Predicted y value
    y_predict = predictions[index]

    #Test x values
    x_precipitation = x_test[index][0]
    x_winter = x_test[index][1]
    print("Latitude:", x_precipitation)
    print("Longitude:", x_winter)
    print("Predicted Max Wind:", y_predict)
    print("Actual Max Wind:", actual)
