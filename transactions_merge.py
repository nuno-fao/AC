import pandas as pd

df_trans = pd.read_csv("D:/FEUP/AC/AC/processed_files/trans_train_processed.csv",sep=',')

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


merged=df_trans[['account_id']]
merged=merged.drop_duplicates(subset=['account_id'])

credit_count=df_trans.groupby('account_id')['type'].apply(lambda x: (x=='credit').sum()).reset_index(name='credit count')
withdrawal_count=df_trans.groupby('account_id')['type'].apply(lambda x: (x=='withdrawal').sum()).reset_index(name='withdrawl count')
amount_std=df_trans.groupby('account_id')['amount'].std().reset_index(name='amount std')
#actions=df_trans['account_id',df_trans['type']=='withdrawl'].groupby['account_id'].count()
balancemean=df_trans[['account_id', 'balance']].groupby('account_id').mean()
balancemin=df_trans[['account_id', 'balance']].groupby('account_id').min()
balancemax=df_trans[['account_id', 'balance']].groupby('account_id').max()

meantrans = df_trans[['account_id', 'amount']].groupby('account_id').mean()
maxtrans = df_trans[['account_id', 'amount']].groupby('account_id').max()
mintrans= df_trans[['account_id', 'amount']].groupby('account_id').min()
merged=merged.merge(credit_count,on='account_id')
merged=merged.merge(withdrawal_count,on='account_id')
merged=merged.merge(balancemean,on='account_id')
merged=merged.merge(balancemin,on='account_id')
merged=merged.merge(balancemax,on='account_id')
merged = merged.merge(meantrans,on='account_id')
merged = merged.merge(maxtrans,on='account_id')
merged=merged.merge(mintrans,on='account_id')
merged=merged.merge(amount_std.round(),on='account_id')
merged = merged.rename(columns={'type':'number of actions','amount_x':'transaction mean','amount_y':'transaction max','amount' : 'transaction min', 'balance_x': 'balance mean','balance_y':'balance min','balance':'balance max'})

merged.to_csv("D:/FEUP/AC/AC/testdataset.csv",index=False)
