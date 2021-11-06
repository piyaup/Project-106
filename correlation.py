import plotly.express as px 
import csv
import numpy as np 

def plotfigure(data_path):
    with open (data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x = "Coffeeinml", y = "hours")
        fig.show()

def getDataSource(data_path):
    Coffeeinml = []
    DaysPresent= []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            Coffeeinml.append(float(row["Coffeeinml"]))
            DaysPresent.append(float(row["hours"]))
    return {"x":Coffeeinml, "y":DaysPresent}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between Coffe vs Sleep in hours :- \n--->",correlation[0,1])

def setup():
    data_path = "C:/Users/piyap/Downloads/python/coffee.csv"
    datasource = getDataSource(data_path)
    findcorrelation(datasource)
    plotfigure(data_path)
setup()