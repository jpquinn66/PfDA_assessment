import pandas as pd
import numpy as np
import seaborn as sns
import csv
import matplotlib.pyplot as plt




bkdata  = pd.read_csv('day.csv')
totalusers= bkdata['casual'].sum()+bkdata['registered'].sum()
print (totalusers)

aver = bkdata.cnt.mean()
std= bkdata.cnt.std()
print(aver, std)

ctr = 0
for weathersit in bkdata:
    if weathersit[1] == '3':
        ctr += 1
print(ctr)

dy= bkdata.groupby('weekday').sum()
avdy= bkdata.groupby('weekday').mean()
print('Totals and average by day')
print(dy['cnt'],avdy['cnt'])

wea= bkdata.groupby('weathersit').sum()
avg= bkdata.groupby('weathersit').mean()                                          
print('Totals and average by weathertype')
print(wea['cnt'], avg['cnt'])





df = pd.DataFrame(bkdata)
df['dteday'] =  pd.to_datetime(df['dteday'])
df['day'] = df['dteday'].dt.day_name()
df[['day', 'cnt']].groupby('day').sum().plot(kind='bar', legend=None, title='Usage by Day')
##df[['weathersit', 'cnt']].groupby('weathersit').sum().plot(kind='scatter',x='weathersit', y='cnt', legend=None, title='Usage by Day')
##df.plot(kind='scatter',x=totalusers, y='weathersit',legend=None)



##X = list(df.iloc[:, 6])
##Y = list(df.iloc[:, 14])
  
# Plot the data using bar() method
##plt.bar(X, Y, color='b')
##plt.title("Total users by Weekday")
##plt.xlabel("Day")
##plt.ylabel("Number of Users")
  
# Show the plot
plt.show()

sns.scatterplot(x='cnt',y='weathersit',data=bkdata,hue='cnt')




plt.show()


fig, ax = plt.subplots(2, 2)
ax[0, 0].scatter(x = df['cnt'], y = df['weathersit'])
ax[0, 0].set_xlabel("Total users")
ax[0, 0].set_ylabel("weather status")

ax[0, 1].scatter(x = df['cnt'], y = df['windspeed'])
ax[0, 1].set_xlabel("Total users")
ax[0, 1].set_ylabel("Windspeed")

ax[1, 0].scatter(x = df['cnt'], y = df['hum'])
ax[1, 0].set_xlabel("Total users")
ax[1, 0].set_ylabel("Humidity")

ax[1, 1].scatter(x = df['cnt'], y = df['temp'])
ax[1, 1].set_xlabel("Total users")
ax[1, 1].set_ylabel("Temperature")

plt.show()

sns.scatterplot(x='cnt',y='windspeed',data=bkdata,hue='cnt')

plt.show()

sns.displot(bkdata, x='weathersit')
plt.show()

three = bkdata['weathersit'].value_counts()[3]
print(three)

