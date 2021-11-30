import pandas as pd

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

def transaction_stats(df_trans):
    merged=df_trans[['account_id']]
    merged=merged.drop_duplicates(subset=['account_id'])

    actions=df_trans[['account_id', 'type']].groupby('account_id').count()
    balancemean=df_trans[['account_id', 'balance']].groupby('account_id').mean().round(1)
    balancemin=df_trans[['account_id', 'balance']].groupby('account_id').min()
    balancemax=df_trans[['account_id', 'balance']].groupby('account_id').max()

    meantrans = df_trans[['account_id', 'amount']].groupby('account_id').mean().round(0)
    mintrans= df_trans[['account_id', 'amount']].groupby('account_id').min()
    maxtrans = df_trans[['account_id', 'amount']].groupby('account_id').max()
    merged=merged.merge(actions,on='account_id')
    merged=merged.merge(balancemean,on='account_id')
    merged=merged.merge(balancemin,on='account_id')
    merged=merged.merge(balancemax,on='account_id')
    merged = merged.merge(meantrans,on='account_id')
    merged = merged.merge(maxtrans,on='account_id')
    merged=merged.merge(mintrans,on='account_id')
    merged = merged.rename(columns={'type':'number of actions','amount_x':'transaction mean','amount_y':'transaction max','amount' : 'transaction min', 'balance_x': 'balance mean','balance_y':'balance min','balance':'balance max'})
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

    merged = merged.merge(transaction_stats(trans),on='account_id',how='left')

    
    merged = merged.sort_values(by=['client_id'])
    
    merged = merged.fillna("none")

    merged = merged.drop(['account_district_95_unemp', 'client_district_95_crimes','account_district_95_crimes','client_district_95_unemp','account_id','client_id','client_district_name','client_district_region','account_district_name','account_district_region'],axis=1)

    merged.to_csv(final_name,index=False)

merge_datasets(df_client,df_card,df_account,df_disp,df_district,df_loan,df_trans,"final_dataset.csv")
merge_datasets(df_client,df_card_test,df_account,df_disp,df_district,df_loan_test,df_trans_test,"final_dataset_test.csv")
