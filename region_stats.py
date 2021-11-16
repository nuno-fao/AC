import pandas as pd
import matplotlib.pyplot as plt

df_disp = pd.read_csv("original_files/district.csv",sep=';')

regions = {
        'Prague':0,
        'central Bohemia':0,
        'south Bohemia':0,
        'west Bohemia':0,
        'north Bohemia':0,
        'east Bohemia':0,
        'south Moravia':0,
        'north Moravia':0
        }
total=0
for i,row in df_disp.iterrows():
    
    if str(row["region"])=="Prague":
        regions['Prague']+=1
        total+=1
    elif str(row["region"])=="central Bohemia":
        regions['central Bohemia']+=1
        total+=1
    elif str(row["region"])=="south Bohemia":
        regions['south Bohemia']+=1
        total+=1
    elif str(row["region"])=="west Bohemia":
        regions['west Bohemia']+=1
        total+=1
    elif str(row["region"])=="north Bohemia":
        regions['north Bohemia']+=1
        total+=1
    elif str(row["region"])=="east Bohemia":
        regions['east Bohemia']+=1
        total+=1
    elif str(row["region"])=="south Moravia":
        regions['south Moravia']+=1
        total+=1
    elif str(row["region"])=="north Moravia":
        regions['north Moravia']+=1
        total+=1

percentage = {
        'Prague':round((regions['Prague']/total)*100,2),
        'central Bohemia':round((regions['central Bohemia']/total)*100,2),
        'south Bohemia':round((regions['south Bohemia']/total)*100,2),
        'west Bohemia':round((regions['west Bohemia']/total)*100,2),
        'north Bohemia':round((regions['north Bohemia']/total)*100,2),
        'east Bohemia':round((regions['east Bohemia']/total)*100,2),
        'south Moravia':round((regions['south Moravia']/total)*100,2),
        'north Moravia':round((regions['north Moravia']/total)*100,2)
        }

keys=percentage.keys()
values=percentage.values()
plt.pie(values, labels = keys)
plt.show() 

#print(regions)
#print(percentage)