#Author: Sean Nesamoney
#Last Edited: 5 December 2021
##################################################################################################################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")
print(df)
df1 = pd.read_csv("emotion_index.csv")

########################################################################################################################
#LIVE REACTION HISTOGRAMS
# # #Histogram Song 1
# # axis = sns.histplot(data = df, x = "song1", color = "indigo")
# # axis.set_title("Song 1 Responses")
# # axis.set_xlabel("Emotions")
# # plt.show()
#
# # #Histogram Song 2
# # axis = sns.histplot(data = df, x = "song2", color = "orange")
# # axis.set_title("Song 2 Responses")
# # axis.set_xlabel("Emotions")
# # plt.show()
#
# # Histogram Song 3
# axis = sns.histplot(data = df, x = "song3", color = "indigo")
# axis.set_title("Song 3 Responses")
# axis.set_xlabel("Emotions")
# plt.show()
# #
# # # #Histogram Song 4
# axis = sns.histplot(data = df, x = "song4", color = "orange")
# axis.set_title("Song 4 Responses")
# axis.set_xlabel("Emotions")
# plt.show()
# #
# # #Histogram Song 5
# axis = sns.histplot(data = df, x = "song5", color = "indigo")
# axis.set_title("Song 5 Responses")
# axis.set_xlabel("Emotions")
# plt.show()

########################################################################################################################
#HISTORGRAM MUSIC_HOURS
# axis = sns.histplot(data = df, x = "music_hours", color = "orange")
# axis.set_title("How Many Hours Do Menlo CS Students Listen to Music per Day?")
# axis.set_xlabel("Hours")
# plt.show()

########################################################################################################################
#EMOTION INDEX SCATTER PLOT
index = df1.plot.scatter("tempo", "emotion_index", color = "indigo")
index.set_title("Varying Tempos and Corresponding Emotion Index")
index.set_xlabel("Tempo")
index.set_ylabel("Emotion Index")
plt.show()