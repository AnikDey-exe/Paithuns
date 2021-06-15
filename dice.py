import random
import math
import plotly.express as px
import csv
import plotly.figure_factory as ff
import pandas as pd

# rolls = []
# count = []

# for number in range(0,1000):
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)
#     print("Dice 1: ",dice1)
#     print("Dice 2: ",dice2)
#     print(" ")
#     rolls.append(dice1+dice2)
#     count.append(number)

# fig = ff.create_distplot([rolls],["Result"])
# fig.show()

# df = pd.read_csv('health.csv')

# fig = ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist=False)
# fig.show()

df = pd.read_csv('amazon.csv')

fig = ff.create_distplot([df["Avg Rating"].tolist()],["Average"],show_hist=False)
fig.show()

