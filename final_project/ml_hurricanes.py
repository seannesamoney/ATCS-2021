'''
Program: Hurricane Wind Speed Predictor
Author: Sean Nesamoney
Course: AT Computer Science
Date (last modified): May 10, 2022
'''
import csv
import pandas as pd
import matplotlib.pyplot as plt
import self as self
from sklearn.cluster import KMeans
import matplotlib.image as mpimg
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from mpl_toolkits.mplot3d import Axes3D

#Read in CSV files
data = pd.read_csv("hurricanes2020.csv")
states_data = pd.read_csv("us_states_data.csv")
#Assign variables to CSV columns
x_1 = data["lat_1"]
x_2 = data["long_1"]
y = data["mx_sustained_winds"]
y = pd.Series([int(char.split()[0]) for char in y])

#Gets U.S state from user input
def getState():
    state = input("Enter your state:\n")
    return state

user_state = getState()

#Finds corresponding latitude from given state
def getLat(data, state):
    #Credits: https://www.protechtraining.com/blog/post/python-for-beginners-reading-manipulating-csv-files-737
    f = open("us_states_data.csv")
    csv_f = csv.reader(f)

    lat_in = data.loc[data["state"] == state]['latitude']
    return lat_in

lat = getLat(states_data, user_state)

#Finds corresponding longitude from given state
def getLong(data, state):
    # CREDITS: https://www.protechtraining.com/blog/post/python-for-beginners-reading-manipulating-csv-files-737
    f = open("us_states_data.csv")
    csv_f = csv.reader(f)

    long_in = data.loc[data["state"] == state]['longitude']
    return long_in

long = getLong(states_data, user_state)

'''MACHINE LEARNING'''
#Uses multilinear regression model to predict maximum wind speed
def predict(data, y, lat_in, long_in):
    #Create Multiple Linear Regression Model
    x = data[["lat_1", "long_1"]].values
    y = y.values

    #Separate data into train/test set
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2)


    #Create model on training data
    model = LinearRegression().fit(x_train, y_train)

    #Print out model information
    print("Model Information:")
    print("Latitude Coef", model.coef_[0])
    print("Longitude Coef", model.coef_[1])
    print("Intercept:", model.intercept_)
    print()

    '''Compare to test data'''

    x_pred = [[lat_in.values[0], long_in.values[0]]]

    #Get prediction with user input
    predictions = model.predict(x_pred)
    y_pred = predictions[0]

    #Compare actual and predicted values
    print("Predicting Wind Speed:")

    x_lat = lat_in
    x_long = long_in
    print("Latitude:", lat_in.values[0])
    print("Longitude:", long_in.values[0])
    print("Predicted Max Wind:", y_pred)
    return y_pred

prediction = predict(data, y, lat, long)

'''DATA SCIENCE'''
'''Adds predicted maximum wind for a given state to a CSV'''
def addData(state, wind_speed):
    #Credits: https://www.delftstack.com/howto/python/python-append-to-csv/
    data = [state, wind_speed]
    # Open the file in the write mode
    with open('states_and_winds.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the data
        writer.writerow(data)

        f.close()

addData(user_state, prediction)

def plot():
    winds = pd.read_csv("states_and_winds.csv")
    state = winds["state"]
    wind_speed = winds["max_wind_speed"]
    #Plotting the bar graph
    plt.bar(state, wind_speed, color='g')
    plt.title("States and Predicted Wind Speeds")
    plt.xlabel("U.S State")
    plt.ylabel("Maximum Wind Speed")

    # Show the plot
    plt.show()

plot()