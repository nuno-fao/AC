import pandas as pd

df_clients = pd.read_csv("original_files/client.csv",sep=';')

birthdays = []
gender = []
print(df_clients)
for i, row in df_clients.iterrows():
    birthdate = str(row['birth_number'])
    month=int(birthdate[2:4])
    if(month>12):
        gender.append('F')
        month=month-50
    else:
        gender.append('M')

    date = "19" + birthdate[0:2] + "-"+ str(month)+"-" + birthdate[4:6]
    birthdays.append(date)

df_clients = df_clients.drop('birth_number', axis=1)
df_clients['birthdate']=birthdays
df_clients['gender']=gender

df_clients.to_csv('client_processed.csv', index=False)

    