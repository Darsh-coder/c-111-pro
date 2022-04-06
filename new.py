import plotly.graph_objects as go
import csv 
import pandas as pd
import random
import statistics
import plotly.figure_factory as ff

df = pd.read_csv("gg.csv")

data = df["ggc"].tolist()
mean = statistics.mean(data)
standard_deviation = statistics.stdev(data)

print ("mean of population",mean)
print("standard_deviation of population",standard_deviation)

fig =ff.create_distplot([data],["ggc"],show_hist = False)
fig.show()