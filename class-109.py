import csv
from os import name
import pandas as pd
import plotly.figure_factory as pff
import plotly.express as px
import statistics
import random
import plotly.graph_objects as pg

df = pd.read_csv("C:\\Users\\TRUSTANA MARKETING\\OneDrive\\Desktop\\Whitehat jr\\Python_Class\\StudentsPerformance.csv")
data = df["reading score"].to_list() 


stat_mean = statistics.mean(data)
print("This mean of height is: ",stat_mean)
stat_median = statistics.median(data)
print("This median of height is: ",stat_median)
stat_mode = statistics.mode(data)
print("This mode of height is: ",stat_mode)

std = statistics.stdev(data)

firstStdStart, firstStdEnd = stat_mean-std, stat_mean+std
secondStdStart, secondStdEnd = stat_mean-2*std, stat_mean+2*std
thirdStdStart, thirdStdEnd = stat_mean-3*std, stat_mean+3*std


    fig = pff.create_distplot([data], ["reading score"], show_hist=False)
    fig.add_trace(pg.Scatter(x=[stat_mean,stat_mean],y=[0,0.17],mode="lines", name="mean"))

    fig.add_trace(pg.Scatter(x=[firstStdStart, firstStdStart],y=[0,0.17],mode="lines", name="First std Deviation Start "))
    fig.add_trace(pg.Scatter(x=[firstStdEnd, firstStdEnd],y=[0,0.17],mode="lines", name="First std deviation end"))

    fig.add_trace(pg.Scatter(x=[secondStdStart, secondStdStart],y=[0,0.17],mode="lines", name="Second std Deviation Start "))
    fig.add_trace(pg.Scatter(x=[secondStdEnd, secondStdEnd],y=[0,0.17],mode="lines", name="Second std deviation end"))

    fig.add_trace(pg.Scatter(x=[thirdStdStart, thirdStdStart],y=[0,0.17],mode="lines", name="Third std Deviation Start "))
    fig.add_trace(pg.Scatter(x=[thirdStdEnd, thirdStdEnd],y=[0,0.17],mode="lines", name="Third std deviation end"))

    fig.show()

    data_of_data_within_1_std_deviation = [result for result in data if result > firstStdStart
    and result < firstStdEnd]
    print(len(data_of_data_within_1_std_deviation)*100/len(data))

    data_of_data_within_2_std_deviation = [result for result in data if result > secondStdStart
    and result < secondStdEnd]
    print(len(data_of_data_within_2_std_deviation)*100/len(data))

    data_of_data_within_3_std_deviation = [result for result in data if result > thirdStdStart
    and result < thirdStdEnd]
    print(len(data_of_data_within_3_std_deviation)*100/len(data))

    
