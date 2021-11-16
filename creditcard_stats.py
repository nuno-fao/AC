import pandas as pd
import matplotlib.pyplot as plt

df_disp = pd.read_csv("original_files/card_train.csv",sep=';')

type = {'Junior':0,
        'Classic':0,
        'Gold':0
        }

for i,row in df_disp.iterrows():
    
    if str(row["type"])=="junior":
        type['Junior']+=1
        
    elif str(row["type"])=="classic":
        type['Classic']+=1
       
    elif str(row["type"])=="gold":
        type['Gold']+=1

  
keys=type.keys()
values=type.values()
plt.bar(keys, values)
plt.show()
