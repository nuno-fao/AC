import pandas as pd

df_client = pd.read_csv("processed_files/client_processed.csv",sep=',')
df_card = pd.read_csv("processed_files/card_train_processed.csv",sep=',')
df_account = pd.read_csv("processed_files/account_processed.csv",sep=',')
df_disp = pd.read_csv("processed_files/disp_processed.csv",sep=',')
df_district = pd.read_csv("processed_files/district_processed.csv",sep=',')
df_loan = pd.read_csv("processed_files/loan_train_processed.csv",sep=',')
df_trans = pd.read_csv("processed_files/trans_train_processed.csv",sep=',')

# def add_value(col,id,value):

#     return

# def merge_accounts():
#     global df_client
#     global df_account
#     global df_disp

#     df_client["account_id"]=""
#     df_client["account_district"]=""
#     df_client["disp_type"]=""
#     df_client["account_frequency"]=""
#     df_client["account_creation"]=""

#     for i,row in df_disp.iterrows():
#         print(df_account.loc[df_account['account_id'] == row['account_id']].items())
#         return

# merge_accounts()


merged = df_client.merge(df_disp, on='client_id')

merged = merged.merge(df_account, on='account_id')

merged = merged.merge(df_card,on='disp_id',how="left")

merged = merged.rename(columns={'type_x':'disp_type','type_y':'card_type','district_id_x' : 'client_district', 'district_id_y':'account_district','date':'account_date'})

merged = merged.merge(df_loan, on='account_id')

merged = merged.rename(columns={'date': 'loan_date'})

#limpar disponents

merged.drop(merged[merged['disp_type'] == 1].index, inplace = True) #POR ALGUM MOTIVO ISTO CORTA 1 VALOR!!!!

merged = merged.merge(df_district, left_on='client_district',right_on='code ')

merged = merged.rename(columns={
    'code ' : 'client_district_code',
    'name ':'client_district_name',
    "region": "client_district_region",
    "no. of inhabitants": "client_district_habitants",
    "no. of municipalities with inhabitants < 499 ": "client_district_mun_under_499",
    "no. of municipalities with inhabitants 500-1999": "client_district_mun_under_1999",
    "no. of municipalities with inhabitants 2000-9999 ": "client_district_mun_under_9999",
    "no. of municipalities with inhabitants >10000 ": "client_district_mun_higher_10000",
    "no. of cities ": "client_district_cities",
    "ratio of urban inhabitants ": "client_district_inhab_ration",
    "average salary ": "client_district_average_salary",
    "unemploymant rate '95 ": "client_district_95_unemp",
    "unemploymant rate '96 ": "client_district_96_unemp",
    "no. of enterpreneurs per 1000 inhabitants ": "client_district_entrepren",
    "no. of commited crimes '95 ": "client_district_95_crimes",
    "no. of commited crimes '96 ": "client_district_96_crimes",
    })

merged = merged.merge(df_district, left_on='account_district',right_on='code ')

merged = merged.rename(columns={
    'code ' : 'account_district_code',
    'name ':'account_district_name',
    "region": "account_district_region",
    "no. of inhabitants": "account_district_habitants",
    "no. of municipalities with inhabitants < 499 ": "account_district_mun_under_499",
    "no. of municipalities with inhabitants 500-1999": "account_district_mun_under_1999",
    "no. of municipalities with inhabitants 2000-9999 ": "account_district_mun_under_9999",
    "no. of municipalities with inhabitants >10000 ": "account_district_mun_higher_10000",
    "no. of cities ": "account_district_cities",
    "ratio of urban inhabitants ": "account_district_inhab_ration",
    "average salary ": "account_district_average_salary",
    "unemploymant rate '95 ": "account_district_95_unemp",
    "unemploymant rate '96 ": "account_district_96_unemp",
    "no. of enterpreneurs per 1000 inhabitants ": "account_district_entrepren",
    "no. of commited crimes '95 ": "account_district_95_crimes",
    "no. of commited crimes '96 ": "account_district_96_crimes",
    })



merged = merged.drop(['client_district','disp_id','disp_type','account_district','loan_id','client_district_code','account_district_code'],axis=1)

merged.to_csv("final_dataset.csv",index=False)
