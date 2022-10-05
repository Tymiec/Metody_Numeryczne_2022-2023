import plotly.express as px
import pandas as pd

df = pd.read_csv('https://kacpertopol.github.io/start/pl/010_Nauczanie/008_Metody_Numeryczne/010_Zestawy_zada%C5%84/001_Zestaw_1/btc.data')

fig = px.line(df)
fig.show()