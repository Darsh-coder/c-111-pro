import plotly.graph_objects as go
import csv 
import pandas as pd
import random
import statistics
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")

data = df["reading_time"].tolist()
mean = statistics.mean(data)
standard_deviation = statistics.stdev(data)

print ("mean of reading_time",mean)
print("standard_deviation of population",standard_deviation)

fig =ff.create_distplot([data],["reading_time"],show_hist = False)
#fig.show()

def randon_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex= random.randint(0,len(data)-1)
        value =data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return(mean)

meanlist=[]

for i in range(0,100):
    setofmeans=randon_set_of_mean(30)
    meanlist.append(setofmeans)

mean_sample = statistics.mean(meanlist)
standard_deviation_sample = statistics.stdev(meanlist)

print ("mean of reading_time",mean_sample)
print("standard_deviation of mean",standard_deviation_sample)

fig =ff.create_distplot([meanlist],["reading_time"],show_hist = False)


first_std_start,first_std_end = mean-standard_deviation_sample, mean+standard_deviation_sample
second_std_start,second_std_end = mean-(standard_deviation_sample*2), mean+(standard_deviation_sample*2)
third_std_start,third_std_end = mean-(standard_deviation_sample*3), mean+(standard_deviation_sample*3)

fig.add_trace(go.Scatter(x= [mean,mean],y=[0,0.17],mode="lines",name="MEAN"))

fig.add_trace(go.Scatter(x= [first_std_start,first_std_start],y=[0,0.17],mode="lines",name="first_std_start"))

fig.add_trace(go.Scatter(x= [first_std_end,first_std_end],y=[0,0.17],mode="lines",name="first_std_end"))

fig.add_trace(go.Scatter(x= [second_std_start,second_std_start],y=[0,0.17],mode="lines",name="second_std_start"))

fig.add_trace(go.Scatter(x= [second_std_end,second_std_end],y=[0,0.17],mode="lines",name="second_std_end"))

fig.add_trace(go.Scatter(x= [third_std_start,third_std_start],y=[0,0.17],mode="lines",name="third_std_start"))

fig.add_trace(go.Scatter(x= [third_std_end,third_std_end],y=[0,0.17],mode="lines",name="third_std_end"))

#mean of 1 set of student

samplemean = pd.read_csv("sample_2.csv")

data1 = samplemean["reading_time"].tolist()
mean1 = statistics.mean(data1)



fig.add_trace(go.Scatter(x= [mean1,mean1],y=[0,0.17],mode="lines",name="INTERVENTION 1"))




fig.show()

zscore1 = (mean_sample-mean1)/standard_deviation_sample 



print("zscore1 = ",zscore1)




