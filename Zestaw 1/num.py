import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Tymiec/NUM/master/Zestaw%201/btc.csv')

fig = px.line(df)
fig.show()