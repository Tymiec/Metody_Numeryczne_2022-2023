import plotly.express as px
import pandas as pd

df = pd.read_csv(r'C:\Repo\NUM\Zestaw 1\btc.csv')
df2 = pd.read_csv(r'C:\Repo\NUM\Zestaw 1\eth.csv')

df["crypto"] = "BTC"
df2["crypto"] = "ETH"

crypto=pd.concat([df,df2], ignore_index=True)

fig = px.line(crypto, x="day",range_x=[57,129], y="value",color="crypto", title="Graph of Cryptocurrency values", template="plotly_dark",
    labels={
        "day" : "Days since 01.01.2021",
        "value" : "Price in USD"
    })

fig.show()


