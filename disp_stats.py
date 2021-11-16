import pandas as pd

df_disp = pd.read_csv("original_files/disp.csv",sep=';')

owner=0
disponent=0

for i,row in df_disp.iterrows():
    
    if str(row["type"])=="OWNER":
        owner +=1
    else:
        disponent+=1

total=owner+disponent

result_owners = "Number of owners is "+ str(owner)+ " (" + str(round((owner/total)*100,2)) +"%)"
disponent_owners = "Number of disponents is "+ str(disponent)+ " (" + str(round((disponent/total)*100,2))+"%)"
print(result_owners)
print(disponent_owners)