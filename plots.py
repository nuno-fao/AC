import pandas as pd
import matplotlib.pyplot as plt
import time
import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pandas.core.reshape.merge import merge
import plotly.express as px
import statsmodels.api as sm
pd.options.plotting.backend="plotly"
  
df_trans = pd.read_csv("D:/FEUP/AC/AC/processed_files/trans_train_processed.csv",sep=',')
df_loan=pd.read_csv("D:/FEUP/AC/AC/processed_files/loan_train_processed.csv")
df_client = pd.read_csv("D:/FEUP/AC/AC/processed_files/client_processed.csv",sep=',')
df_card = pd.read_csv("D:/FEUP/AC/AC/processed_files/card_train_processed.csv",sep=',')
df_card_test = pd.read_csv("D:/FEUP/AC/AC/processed_files/card_test_processed.csv",sep=',')
df_account = pd.read_csv("D:/FEUP/AC/AC/processed_files/account_processed.csv",sep=',')
df_disp = pd.read_csv("D:/FEUP/AC/AC/processed_files/disp_processed.csv",sep=',')
df_district = pd.read_csv("D:/FEUP/AC/AC/processed_files/district_processed.csv",sep=',')
df_loan = pd.read_csv("D:/FEUP/AC/AC/processed_files/loan_train_processed.csv",sep=',')
df_loan_test = pd.read_csv("D:/FEUP/AC/AC/processed_files/loan_test_processed.csv",sep=',')
df_trans = pd.read_csv("D:/FEUP/AC/AC/processed_files/trans_train_processed.csv",sep=',')
df_trans_test = pd.read_csv("D:/FEUP/AC/AC/processed_files/trans_test_processed.csv",sep=',')
df_final = pd.read_csv("D:/FEUP/AC/AC/final_dataset.csv",sep=',')


gender = []
for i, row in df_client.iterrows():
    if(row['gender']==1):
        gender.append('Male')
    else:
        gender.append('Female')

df_client['gender']=gender

df_loan["status"]=df_loan["status"].astype(str)

    ##
df_disp.drop(df_disp[df_disp['type'] == 1].index, inplace = True)
merged = df_client.merge(df_disp, on='client_id')

merged = merged.merge(df_loan, on='account_id')
#fig1=px.scatter(df_loan,x="amount",y="payments",size="duration",color="status",color_discrete_sequence=px.colors.qualitative.G10)
fig1=px.scatter_matrix(df_loan,dimensions=["amount","payments","duration"],color="status",color_discrete_sequence=px.colors.qualitative.G10)
fig2=px.scatter(df_district,x="no. of inhabitants",y="name ",size="average salary ",color="region")
male=merged.loc[merged['gender']=='Male']
female=merged.loc[merged['gender']=='Female']
fig3=px.histogram(merged,x="age",color="status",barmode='group')
fig4=px.histogram(merged,x="gender",color="status",barmode='group')


df_trans.drop_duplicates('account_id',keep='last')
df_trans=df_trans.merge(df_loan,how='right',on='account_id')
withdrawal_balancemin=df_trans.groupby('account_id')['balance'].min().round().reset_index(name='balance min')
fig1.show()
fig2.show()
fig3.show()
fig4.show()
