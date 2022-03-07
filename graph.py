import pandas as pd
import plotly.graph_objects as pg
import csv

graph_data = pd.read_csv("data.csv")
df = graph_data.loc[graph_data['student_id']=="TRL_987"]
level = df.groupby("level")["attempt"].mean()

pic = pg.Figure(pg.Bar(x = level, y = ["Level1", "Level2", "Level3", "Level4"], orientation = "h"))
pic.show()

print(df)