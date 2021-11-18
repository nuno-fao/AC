import pandas as pd
import matplotlib.pyplot as plt
import time
import csv
  
df=pd.read_csv('D:\FEUP\AC\AC\processed_files\district_processed.csv')
  


# region_counts=df['region'].value_counts()
# region_cnt=region_counts.plot.bar()
# region_cnt.set_title("Region count")

# year_rating_dist = df[['region', 'average salary']].groupby('region').mean()
# yr_plot = year_rating_dist.plot.bar()
# yr_plot.set_title('Average salary per region')

# unemployment95 = df[['region', 'unemploymant rate 95']].groupby('region').mean()
# yr_plot = unemployment95.plot.bar()
# yr_plot.set_title('Unemployment \'95 by region')

# unemployment96 = df[['region', 'unemploymant rate 96']].groupby('region').mean()
# yr_plot = unemployment96.plot.bar()
# yr_plot.set_title('Unemployment \'96 by region')

unemployment96 = df[['region', 'no. of commited crimes \'95']].groupby('region').sum()
yr_plot = unemployment96.plot.bar()
yr_plot.set_title('Number of crimes commited \'95 by region')

unemployment96 = df[['region', 'no. of commited crimes \'96 ']].groupby('region').sum()
yr_plot = unemployment96.plot.bar()
yr_plot.set_title('Number of crimes commited \'96 by region')

plt.show()