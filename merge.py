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

merged = merged.rename(columns={'district_id_x' : 'client_district', 'district_id_y':'account_district'})

merged = merged.merge(df_district, left_on='client_district',right_on='code ')

merged.to_csv("final_dataset.csv",index=False)
print(merged)
