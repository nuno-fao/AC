import pandas as pd
import numpy as np

df_client = pd.read_csv("processed_files/client_processed.csv",sep=',')
df_card = pd.read_csv("processed_files/card_train_processed.csv",sep=',')
df_card_test = pd.read_csv("processed_files/card_test_processed.csv",sep=',')
df_account = pd.read_csv("processed_files/account_processed.csv",sep=',')
df_disp = pd.read_csv("processed_files/disp_processed.csv",sep=',')
df_district = pd.read_csv("processed_files/district_processed.csv",sep=',')
df_loan = pd.read_csv("processed_files/loan_train_processed.csv",sep=',')
df_loan_test = pd.read_csv("processed_files/loan_test_processed.csv",sep=',')
df_trans = pd.read_csv("processed_files/trans_train_processed.csv",sep=',')
df_trans_test = pd.read_csv("processed_files/trans_test_processed.csv",sep=',')

def transaction_stats(df_trans,df_loan):
    
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


    # operation on DATE 

    DATE_df=df_loan.merge(df_trans,how='left',on='account_id')
    
    DATEaux=DATE_df.loc[DATE_df['date']<DATE_df['loan_date']]
    #balanceBEFOREloan=DATEaux.groupby('account_id')['date'].max()
    DATEaux.sort_values(['account_id', 'date']).drop_duplicates('date', keep='last')
    balanceBEFOREloan=DATEaux[['account_id','balance','date']]
    DATEaux['ratio']=np.where(DATEaux['loan_amount']<1,DATEaux['loan_amount'],DATEaux['balance']/DATEaux['loan_amount'])

    finalDATE=DATEaux.drop_duplicates('account_id',keep='last')
    finalDATE2=finalDATE[['account_id','ratio']]

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

    merged=merged.merge(finalDATE2,how='left',on='account_id')

    merged=merged.fillna(0)
    return merged

def merge_datasets(clients,cards,accounts,disps,districts,loans,trans,final_name):
    merged = clients.merge(disps, on='client_id')

    merged = merged.merge(accounts, on='account_id')

    merged = merged.merge(cards,on='disp_id',how="left")

    merged['type_y'].fillna(value='0',inplace=True)

    merged = merged.astype({'type_y':int})

    merged = merged.rename(columns={'type_x':'disp_type','type_y':'card_type','district_id_x' : 'client_district', 'district_id_y':'account_district','date':'account_age'})

    merged = merged.merge(loans, on='account_id')

    merged = merged.rename(columns={'date': 'loan_date'})

    #limpar disponents

    merged.drop(merged[merged['disp_type'] == 1].index, inplace = True)

    merged = merged.merge(districts, left_on='client_district',right_on='code ')

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

    merged = merged.merge(districts, left_on='account_district',right_on='code ')

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

    merged = merged.drop(['client_district','disp_id','disp_type','account_district','client_district_code','account_district_code','card_id','issued'],axis=1)

    merged = merged.merge(transaction_stats(trans,loans),on='account_id',how='left')

    
    merged = merged.sort_values(by=['client_id'])
    
    merged = merged.fillna("none")

    merged = merged.drop(['account_id','client_id','client_district_name','client_district_region','account_district_name','account_district_region'],axis=1)

    merged.to_csv(final_name,index=False)

merge_datasets(df_client,df_card,df_account,df_disp,df_district,df_loan,df_trans,"final_dataset.csv")
merge_datasets(df_client,df_card_test,df_account,df_disp,df_district,df_loan_test,df_trans_test,"final_dataset_test.csv")
