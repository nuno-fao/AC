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

    ax.bar(labels, ages_good.values(), 0.35, yerr=0, label='successfull')
    ax.bar(labels, ages_bad.values(), 0.35, yerr=0, bottom=0,
        label='unsuccessfull')

    ax.set_ylabel('Clients')
    ax.set_title('Sucess/insucess by age')
    ax.legend()

    plt.show()
    
    success_rate = {
        '0-24' : ages_good['0-24']/(ages_good['0-24']+ages_bad['0-24'])*100,
        '24-35' : ages_good['24-35']/(ages_good['24-35']+ages_bad['24-35'])*100,
        '36-64' : ages_good['36-64']/(ages_good['36-64']+ages_bad['36-64'])*100,
        '64+' : ages_good['64+']/(ages_good['64+']+ages_bad['64+'])*100
    }
    print(success_rate,non_clients)

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

    success_rate = {
        'Prague' : region_good['Prague']/(region_good['Prague']+region_bad['Prague'])*100,
        'central Bohemia':region_good['central Bohemia']/(region_good['central Bohemia']+region_bad['central Bohemia'])*100,
        'south Bohemia':region_good['south Bohemia']/(region_good['south Bohemia']+region_bad['south Bohemia'])*100,
        'west Bohemia':region_good['west Bohemia']/(region_good['west Bohemia']+region_bad['west Bohemia'])*100,
        'north Bohemia':region_good['north Bohemia']/(region_good['north Bohemia']+region_bad['north Bohemia'])*100,
        'east Bohemia':region_good['east Bohemia']/(region_good['east Bohemia']+region_bad['east Bohemia'])*100,
        'south Moravia':region_good['south Moravia']/(region_good['south Moravia']+region_bad['south Moravia'])*100,
        'north Moravia':region_good['north Moravia']/(region_good['north Moravia']+region_bad['north Moravia'])*100
    }
    print(success_rate,non_clients)
    fig, ax = plt.subplots()
    labels= region_good.keys()

    ax.bar(labels, region_good.values(), 0.35, yerr=0, label='sucessfull')
    ax.bar(labels, region_bad.values(), 0.35, yerr=0, bottom=0,
        label='unsuccessfull')

    ax.set_ylabel('Clients')
    ax.set_title('Sucess/insucess by region')
    ax.legend()
    plt.xticks(rotation=45)

    plt.show()


def get_genders():
    males = 0
    females = 0
    ages = {
        '0-24' : 0,
        '24-35' : 0,
        '36-64' : 0,
        '64+' : 0
    }
    ymin=9999
    ymax=0
    df = pd.read_csv('processed_files/client_processed.csv')
    for i,row in df.iterrows():
        if row['gender'] == 'F':
            females+=1
        else:
            males+=1

        age = 99 - int(row['birthdate'][0:2])

        if age <=24:
            ages['0-24'] +=1
        elif age <=35:
            ages['24-35'] +=1
        elif age <=64:
            ages['36-64'] +=1
        else:
            ages['64+'] +=1

    
    print('Age range',ages)
    print('Males',males)
    print('Females',females)
    print('Max',ymax)
    print('Min',ymin)
    return


def region_stats():
    df_disp = pd.read_csv("original_files/district.csv",sep=';')

    regions = {
            'Prague':0,
            'central Bohemia':0,
            'south Bohemia':0,
            'west Bohemia':0,
            'north Bohemia':0,
            'east Bohemia':0,
            'south Moravia':0,
            'north Moravia':0
            }
    total=0
    for i,row in df_disp.iterrows():
        
        if str(row["region"])=="Prague":
            regions['Prague']+=1
            total+=1
        elif str(row["region"])=="central Bohemia":
            regions['central Bohemia']+=1
            total+=1
        elif str(row["region"])=="south Bohemia":
            regions['south Bohemia']+=1
            total+=1
        elif str(row["region"])=="west Bohemia":
            regions['west Bohemia']+=1
            total+=1
        elif str(row["region"])=="north Bohemia":
            regions['north Bohemia']+=1
            total+=1
        elif str(row["region"])=="east Bohemia":
            regions['east Bohemia']+=1
            total+=1
        elif str(row["region"])=="south Moravia":
            regions['south Moravia']+=1
            total+=1
        elif str(row["region"])=="north Moravia":
            regions['north Moravia']+=1
            total+=1

    percentage = {
            'Prague':round((regions['Prague']/total)*100,2),
            'central Bohemia':round((regions['central Bohemia']/total)*100,2),
            'south Bohemia':round((regions['south Bohemia']/total)*100,2),
            'west Bohemia':round((regions['west Bohemia']/total)*100,2),
            'north Bohemia':round((regions['north Bohemia']/total)*100,2),
            'east Bohemia':round((regions['east Bohemia']/total)*100,2),
            'south Moravia':round((regions['south Moravia']/total)*100,2),
            'north Moravia':round((regions['north Moravia']/total)*100,2)
            }

    keys=percentage.keys()
    values=percentage.values()
    plt.pie(values, labels = keys)
    plt.show() 

    #print(regions)
    #print(percentage)
    return

def disp_stats():
    df_disp = pd.read_csv("original_files/disp.csv",sep=';')

    owner=0
    disponent=0

    for i,row in df_disp.iterrows():
        
        if str(row["type"])=="OWNER":
            owner +=1
        else:
            disponent+=1

    total=owner+disponent

    result_owners = "Number of owners is "+ str(owner)+ " (" + str(round((owner/total)*100,2)) +"%)"
    disponent_owners = "Number of disponents is "+ str(disponent)+ " (" + str(round((disponent/total)*100,2))+"%)"
    print(result_owners)
    print(disponent_owners)
    return

def credit_stats():
    df_disp = pd.read_csv("original_files/card_train.csv",sep=';')

    type = {'Junior':0,
            'Classic':0,
            'Gold':0
            }

    for i,row in df_disp.iterrows():
        
        if str(row["type"])=="junior":
            type['Junior']+=1
            
        elif str(row["type"])=="classic":
            type['Classic']+=1
        
        elif str(row["type"])=="gold":
            type['Gold']+=1

    
    keys=type.keys()
    values=type.values()
    plt.bar(keys, values)
    plt.show()
    return

get_genders()
loans_ages()
loans_regions()
region_stats()
disp_stats()
credit_stats()

