import plotly.express as px
import pandas as pd

df = pd.read_csv(r'C:\Repo\NUM\Zestaw 1\btc_nice.csv')
df = pd.read_csv(r'C:\Repo\NUM\Zestaw 1\btc_nice.csv')

fig = px.line(df, x="day", y="value", title="Graph of Cryptocurrency values", template="plotly_dark",
    labels={
        "day" : "Days since 01.01.2021",
        "value" : "Price in USD"
    })

fig.show()