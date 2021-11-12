import pandas as pd

def get_genders():
    males = 0
    females = 0
    age_range = {
        '<1920':0,
        '1920-1930':0,
        '1930-1940':0,
        '1940-1950':0,
        '1950-1960':0,
        '1960-1970':0,
        '1970-1980':0,
        '1980-1990':0
        }
    ymin=9999
    ymax=0
    df = pd.read_csv('client_processed.csv')
    for i,row in df.iterrows():
        if row['gender'] == 'F':
            females+=1
        else:
            males+=1

        year = int(row['birthdate'][0:4])

        if year <= 1920:
            age_range['<1920'] = age_range['<1920']+1
        elif year <= 1930:
            age_range['1920-1930'] = age_range['1920-1930']+1
        elif year <= 1940:
            age_range['1930-1940'] = age_range['1930-1940']+1
        elif year <= 1950:
            age_range['1940-1950'] = age_range['1940-1950']+1
        elif year <= 1960:
            age_range['1950-1960'] = age_range['1950-1960']+1
        elif year <= 1970:
            age_range['1960-1970'] = age_range['1960-1970']+1
        elif year <= 1980:
            age_range['1970-1980'] = age_range['1970-1980']+1
        elif year <= 1990:
            age_range['1980-1990'] = age_range['1980-1990']+1


        if year < ymin:
            ymin = year
        elif year > ymax:
            ymax = year

    
    print('Age range',age_range)
    print('Males',males)
    print('Females',females)
    print('Max',ymax)
    print('Min',ymin)

get_genders()

