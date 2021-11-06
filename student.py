import plotly_express as px
import csv 

with open("./student.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="DaysPresent",y="MarksInPercentage")
    fig.show()