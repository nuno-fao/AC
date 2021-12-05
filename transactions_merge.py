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

#credit_count=df_trans.groupby('account_id')['type'].apply(lambda x: (x=='credit').sum()).reset_index(name='credit count')
#withdrawal_count=df_trans.groupby('account_id')['type'].apply(lambda x: (x=='withdrawal').sum()).reset_index(name='withdrawl count')

# operation on dataset with CREDIT

credit_df=df_trans.loc[df_trans['type']=='credit']
credit_count=credit_df.groupby('account_id')['type'].count().reset_index(name='credit count')
credit_balancemean=credit_df.groupby('account_id')['balance'].mean().round().reset_index(name='credit balance mean')
credit_balancemin=credit_df.groupby('account_id')['balance'].min().round().reset_index(name='credit balance min')
credit_balancemax=credit_df.groupby('account_id')['balance'].max().round().reset_index(name='credit balance max')

credit_amountmean = credit_df.groupby('account_id')['amount'].mean().round().reset_index(name='credit amount mean')
credit_amountmin = credit_df.groupby('account_id')['amount'].min().round().reset_index(name='credit amount min')
credit_amountmax= credit_df.groupby('account_id')['amount'].max().round().reset_index(name='credit amount max')
credit_amount_std=credit_df.groupby('account_id')['amount'].std().round().reset_index(name='credit amount std')


# operation on dataset with WITHDRAWAL

withdrawal_df=df_trans.loc[df_trans['type']=='withdrawal']
withdrawal_count=withdrawal_df.groupby('account_id')['type'].count().reset_index(name='withdrawal count')
withdrawal_balancemean=withdrawal_df.groupby('account_id')['balance'].mean().round().reset_index(name='withdrawal balance mean')
withdrawal_balancemin=withdrawal_df.groupby('account_id')['balance'].min().round().reset_index(name='withdrawal balance min')
withdrawal_balancemax=withdrawal_df.groupby('account_id')['balance'].max().round().reset_index(name='withdrawal balance max')

withdrawal_amountmean = withdrawal_df.groupby('account_id')['amount'].mean().round().reset_index(name='withdrawal amount mean')
withdrawal_amountmin = withdrawal_df.groupby('account_id')['amount'].min().round().reset_index(name='withdrawal amount min')
withdrawal_amountmax= withdrawal_df.groupby('account_id')['amount'].max().round().reset_index(name='withdrawal amount max')
withdrawal_amount_std=withdrawal_df.groupby('account_id')['amount'].std().round().reset_index(name='withdrawal amount std')



# merge on CREDIT

merged=merged.merge(credit_count,on='account_id')
merged=merged.merge(credit_balancemean,on='account_id')
merged=merged.merge(credit_balancemin,on='account_id')
merged=merged.merge(credit_balancemax,on='account_id')
merged = merged.merge(credit_amountmean,on='account_id')
merged = merged.merge(credit_amountmin,on='account_id')
merged=merged.merge(credit_amountmax,on='account_id')
merged=merged.merge(credit_amount_std,on='account_id')

# merge on WITHDRAWAL

merged=merged.merge(withdrawal_count,on='account_id')
merged=merged.merge(withdrawal_balancemean,on='account_id')
merged=merged.merge(withdrawal_balancemin,on='account_id')
merged=merged.merge(withdrawal_balancemax,on='account_id')
merged = merged.merge(withdrawal_amountmean,on='account_id')
merged = merged.merge(withdrawal_amountmin,on='account_id')
merged=merged.merge(withdrawal_amountmax,on='account_id')
merged=merged.merge(withdrawal_amount_std,on='account_id')

merged.to_csv("D:/FEUP/AC/AC/testdataset.csv",index=False)
