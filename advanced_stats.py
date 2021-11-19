import pandas as pd
import matplotlib.pyplot as plt

def loans_ages():
    ages_good = {
        '0-24' : 0,
        '24-35' : 0,
        '36-64' : 0,
        '64+' : 0
    }

    ages_bad = {
        '0-24' : 0,
        '24-35' : 0,
        '36-64' : 0,
        '64+' : 0
    }

    loans = pd.read_csv('processed_files/loan_train_processed.csv')
    clients = pd.read_csv('processed_files/client_processed.csv')
    non_clients = 0
    for i, row in loans.iterrows():
        try:
            age = clients.loc[clients['client_id'] == row['account_id']]['birthdate'].item()
            age = 99 - int(age.split('-')[0])
            if row['status'] == 1:     
                if age <=24:
                    ages_good['0-24'] +=1
                elif age <=35:
                    ages_good['24-35'] +=1
                elif age <=64:
                    ages_good['36-64'] +=1
                else:
                    ages_good['64+'] +=1

            elif row['status'] == -1:
                if age <=24:
                    ages_bad['0-24'] +=1
                elif age <=35:
                    ages_bad['24-35'] +=1
                elif age <=64:
                    ages_bad['36-64'] +=1
                else:
                    ages_bad['64+'] +=1
        except:
            non_clients+=1

    print(ages_good,ages_bad,non_clients)
    
    
    fig, ax = plt.subplots()
    labels= ages_good.keys()

    ax.bar(labels, ages_good.values(), 0.35, yerr=0, label='aproved')
    ax.bar(labels, ages_bad.values(), 0.35, yerr=0, bottom=0,
        label='not aproved')

    ax.set_ylabel('Clients')
    ax.set_title('Sucess/insucess by age')
    ax.legend()

    plt.show()
    

def loans_regions():
    region_good = {
        'Prague':0,
        'central Bohemia':0,
        'south Bohemia':0,
        'west Bohemia':0,
        'north Bohemia':0,
        'east Bohemia':0,
        'south Moravia':0,
        'north Moravia':0
    }

    region_bad = {
        'Prague':0,
        'central Bohemia':0,
        'south Bohemia':0,
        'west Bohemia':0,
        'north Bohemia':0,
        'east Bohemia':0,
        'south Moravia':0,
        'north Moravia':0
    }

    loans = pd.read_csv('processed_files/loan_train_processed.csv')
    clients = pd.read_csv('processed_files/client_processed.csv')
    non_clients = 0
    for i, row in loans.iterrows():
        try:
            region_id = clients.loc[clients['client_id'] == row['account_id']]['district_id'].item()
            
            if row['status'] == 1:     
                if region_id <=1:
                    region_good['Prague'] +=1
                elif region_id <=13:
                    region_good['central Bohemia'] +=1
                elif region_id <=21:
                    region_good['south Bohemia'] +=1
                elif region_id <=31:
                    region_good['west Bohemia'] +=1
                elif region_id <=41:
                    region_good['north Bohemia'] +=1
                elif region_id <=52:
                    region_good['east Bohemia'] +=1
                elif region_id <=66:
                    region_good['south Moravia'] +=1
                elif region_id <=77:
                    region_good['north Moravia'] +=1

            elif row['status'] == -1:
                if region_id <=1:
                    region_bad['Prague'] +=1
                elif region_id <=13:
                    region_bad['central Bohemia'] +=1
                elif region_id <=21:
                    region_bad['south Bohemia'] +=1
                elif region_id <=31:
                    region_bad['west Bohemia'] +=1
                elif region_id <=41:
                    region_bad['north Bohemia'] +=1
                elif region_id <=52:
                    region_bad['east Bohemia'] +=1
                elif region_id <=66:
                    region_bad['south Moravia'] +=1
                elif region_id <=77:
                    region_bad['north Moravia'] +=1
        except:
            non_clients+=1

    print(region_good,region_bad,non_clients)

loans_ages()
loans_regions()
