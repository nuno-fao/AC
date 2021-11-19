import pandas as pd

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

get_genders()

