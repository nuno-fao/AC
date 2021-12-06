import pandas as pd

df_trans = pd.read_csv("D:/FEUP/AC/AC/processed_files/trans_train_processed.csv",sep=',')


merged=df_trans[['account_id']]
merged=merged.drop_duplicates(subset=['account_id'])


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



# operation on dataset with OPERATION == 1
operationA_df=df_trans.loc[df_trans['operation']==1]
operationA_amountmean = operationA_df.groupby('account_id')['amount'].mean().round().reset_index(name='OPERATION A amount mean')
operationA_count = operationA_df.groupby('account_id')['account_id'].count().reset_index(name='OPERATION A count')

# operation on dataset with OPERATOR == 2
operationB_df=df_trans.loc[df_trans['operation']==2]
operationB_amountmean = operationB_df.groupby('account_id')['amount'].mean().round().reset_index(name='OPERATION B amount mean')
operationB_count = operationB_df.groupby('account_id')['account_id'].count().reset_index(name='OPERATION B count')

# operation on dataset with OPERATOR == 3
operationC_df=df_trans.loc[df_trans['operation']==3]
operationC_amountmean = operationC_df.groupby('account_id')['amount'].mean().round().reset_index(name='OPERATION C amount mean')
operationC_count = operationC_df.groupby('account_id')['account_id'].count().reset_index(name='OPERATION C count')

# operation on dataset with OPERATOR == 4
operationD_df=df_trans.loc[df_trans['operation']==4]
operationD_amountmean = operationD_df.groupby('account_id')['amount'].mean().round().reset_index(name='OPERATION D amount mean')
operationD_count = operationD_df.groupby('account_id')['account_id'].count().reset_index(name='OPERATION D count')

# operation on dataset with OPERATOR == 5
operationE_df=df_trans.loc[df_trans['operation']==5]
operationE_amountmean = operationE_df.groupby('account_id')['amount'].mean().round().reset_index(name='OPERATION E amount mean')
operationE_count = operationE_df.groupby('account_id')['account_id'].count().reset_index(name='OPERATION E count')

# operation on dataset with OPERATOR == 6
operationF_df=df_trans.loc[df_trans['operation']==6]
operationF_amountmean = operationF_df.groupby('account_id')['amount'].mean().round().reset_index(name='OPERATION F amount mean')
operationF_count = operationF_df.groupby('account_id')['account_id'].count().reset_index(name='OPERATION F count')

# merge on CREDIT

merged=merged.merge(credit_count,how='left',on='account_id')
merged=merged.merge(credit_balancemean,how='left',on='account_id')
merged=merged.merge(credit_balancemin,how='left',on='account_id')
merged=merged.merge(credit_balancemax,how='left',on='account_id')
merged = merged.merge(credit_amountmean,how='left',on='account_id')
merged = merged.merge(credit_amountmin,how='left',on='account_id')
merged=merged.merge(credit_amountmax,how='left',on='account_id')
merged=merged.merge(credit_amount_std,how='left',on='account_id')

# merge on WITHDRAWAL

merged=merged.merge(withdrawal_count,how='left',on='account_id')
merged=merged.merge(withdrawal_balancemean,how='left',on='account_id')
merged=merged.merge(withdrawal_balancemin,how='left',on='account_id')
merged=merged.merge(withdrawal_balancemax,how='left',on='account_id')
merged = merged.merge(withdrawal_amountmean,how='left',on='account_id')
merged = merged.merge(withdrawal_amountmin,how='left',on='account_id')
merged=merged.merge(withdrawal_amountmax,how='left',on='account_id')
merged=merged.merge(withdrawal_amount_std,how='left',on='account_id')

# merge on OPERATION TYPE

merged=merged.merge(operationA_amountmean,how='left',on='account_id')
merged=merged.merge(operationA_count,how='left',on='account_id')

merged=merged.merge(operationB_amountmean,how='left',on='account_id')
merged=merged.merge(operationB_count,how='left',on='account_id')

merged=merged.merge(operationC_amountmean,how='left',on='account_id')
merged=merged.merge(operationC_count,how='left',on='account_id')

merged=merged.merge(operationD_amountmean,how='left',on='account_id')
merged=merged.merge(operationD_count,how='left',on='account_id')

merged=merged.merge(operationE_amountmean,how='left',on='account_id')
merged=merged.merge(operationE_count,how='left',on='account_id')

merged=merged.merge(operationF_amountmean,how='left',on='account_id')
merged=merged.merge(operationF_count,how='left',on='account_id')


merged=merged.fillna(0)


merged.to_csv("D:/FEUP/AC/AC/testdataset.csv",index=False)
