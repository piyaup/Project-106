import plotly_express as px
import csv 

with open("./coffee.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Coffeeinml",y="hours")
    fig.show()