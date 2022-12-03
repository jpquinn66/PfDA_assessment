import pandas as pd
import numpy as np
import seaborn as sns
import csv
import matplotlib.pyplot as plt

bkdata  = pd.read_csv('day.csv')
totalusers= bkdata['casual'].sum()+bkdata['registered'].sum()
print (totalusers)

df = pd.DataFrame(bkdata)
df['dteday'] =  pd.to_datetime(df['dteday'])
df['day'] = df['dteday'].dt.day_name()
df[['day', 'cnt']].groupby('day').sum().plot(kind='bar', legend=None)

##X = list(df.iloc[:, 6])
##Y = list(df.iloc[:, 14])
  
# Plot the data using bar() method
##plt.bar(X, Y, color='b')
##plt.title("Total users by Weekday")
##plt.xlabel("Day")
##plt.ylabel("Number of Users")
  
# Show the plot
plt.show()


