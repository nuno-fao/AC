import pandas as pd

def process_clients():
    df_clients = pd.read_csv("original_files/client.csv",sep=';')

    birthdays = []
    gender = []
    for i, row in df_clients.iterrows():
        birthdate = str(row['birth_number'])
        month=int(birthdate[2:4])
        if(month>12):
            gender.append('2')
            month=month-50
        else:
            gender.append('1')

        date = 99 - int(birthdate[0:2])
        birthdays.append(date)

    df_clients = df_clients.drop('birth_number', axis=1)
    df_clients['age']=birthdays
    df_clients['gender']=gender

    df_clients.to_csv('processed_files/client_processed.csv', index=False)

def process_accounts():
    df_accounts = pd.read_csv("original_files/account.csv",sep=';')
    df_accounts = df_accounts.astype({'date':str})
    for i, row in df_accounts.iterrows():
        date = row['date']
        df_accounts.at[i,'date'] = 99 - int(date[0:2])
        frequency = row['frequency']

        if frequency == 'monthly issuance':
            df_accounts.at[i,'frequency'] = '1'
        elif frequency == 'weekly issuance':
            df_accounts.at[i,'frequency'] = '2'
        elif frequency == 'issuance after transaction':
            df_accounts.at[i,'frequency'] = '3'

    df_accounts.to_csv('processed_files/account_processed.csv', index=False)

def process_cards(original):
    df_cards = pd.read_csv("original_files/"+original+".csv",sep=';')
    df_cards = df_cards.astype({'issued':str})
    
    for i, row in df_cards.iterrows():
        date = row['issued']
        df_cards.at[i,'issued'] = date[0:2] + "-" + date[2:4] + "-" + date[4:]

        if row['type']=='classic':
            df_cards.at[i,'type'] = '1'
        elif row['type']=='gold':
            df_cards.at[i,'type'] = '2'
        elif row['type']=='junior':
            df_cards.at[i,'type'] = '3'

    df_cards = df_cards.astype({'type':int})
    df_cards.to_csv('processed_files/' + original + "_processed.csv" , index=False)

def process_disposition():
    df_disp = pd.read_csv("original_files/disp.csv",sep=';')
    df_disp.loc[df_disp['type'] == 'OWNER', 'type'] = 0
    df_disp.loc[df_disp['type'] == 'DISPONENT', 'type'] = 1
    df_disp.to_csv('processed_files/disp_processed.csv', index=False)

def process_district():
    df_district = pd.read_csv("original_files/district.csv",sep=';')
    df_district.to_csv('processed_files/district_processed.csv', index=False)

def process_transaction(original):
    df_trans = pd.read_csv("original_files/"+original+".csv",sep=';',low_memory=False)
    
    df_trans = df_trans.astype({'date':str})
    for i, row in df_trans.iterrows():
        date = row['date']
        df_trans.at[i,'date'] = date[0:2] + "-" + date[2:4] + "-" + date[4:]
        
        if row['operation'] == "credit in cash":
            df_trans.at[i,'operation'] = '1'
        elif row['operation'] == "collection from another bank":
            df_trans.at[i,'operation'] = '2'
        elif row['operation'] == "withdrawal in cash":
            df_trans.at[i,'operation'] = '3'
        elif row['operation'] == "remittance to another bank":
            df_trans.at[i,'operation'] = '4'
        elif row['operation'] == "credit card withdrawal":
            df_trans.at[i,'operation'] = '5'
        else:
            df_trans.at[i,'operation'] = '6'

        if row['type'] == "withdrawal in cash":
            df_trans.at[i,'type'] = 'withdrawal'

    df_trans = df_trans.drop(['k_symbol','bank','account'], axis=1)        
    df_trans.to_csv('processed_files/' + original + "_processed.csv" , index=False)

def process_loan(original):
    df_loans = pd.read_csv("original_files/"+original+".csv",sep=';')

    df_loans = df_loans.astype({'date':str})
    loan_years = []
    loan_months = []
    for i, row in df_loans.iterrows():
        date = row['date']
        loan_years.append( date[0:2])
        loan_months.append( date[2:4])
    df_loans['loan_year']=loan_years
    df_loans['loan_month']=loan_months

    df_loans.to_csv('processed_files/' + original + "_processed.csv" , index=False)


# process_clients()
# process_accounts()
process_cards("card_train")
process_cards("card_test")
# process_disposition()
# process_district()
# process_transaction("trans_train")
# process_transaction("trans_test")
# process_loan("loan_train")
# process_loan("loan_test")