import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Biking.csv")

df_mean = pd.DataFrame(columns=['TimestampInMS','phone_lat','phone_long'])
df_median = pd.DataFrame(columns=['TimestampInMS','phone_lat','phone_long'])

def calcStuff():
    lats = list(map(lambda row: row["phone_lat"], rowsInWindow))
    longs = list(map(lambda row: row["phone_long"], rowsInWindow))

    lat_mean = np.mean(lats)
    long_mean = np.mean(longs)
    
    lat_median = np.median(lats)
    long_median = np.median(longs)

    last = rowsInWindow[-1]

    df_mean.loc[len(df_mean.index)] = [last["TimestampInMS"], lat_mean, long_mean]
    df_median.loc[len(df_mean.index)] = [last["TimestampInMS"], lat_median, long_median]

    return

base = None
rowsInWindow = []

for index, row in df.iterrows():
    
    if base == None:
        base = row["TimestampInMS"]
    
    if row["TimestampInMS"] - base > 10000:
        calcStuff()
        base = row["TimestampInMS"]
        rowsInWindow = []
        
    rowsInWindow.append(row)

if rowsInWindow:
    calcStuff()

plt.plot(df["gt_lat"], df["gt_long"], 'k')
plt.plot(df["phone_lat"], df["phone_long"], 'r')
plt.plot(df_mean["phone_lat"], df_mean["phone_long"], 'b')
plt.plot(df_median["phone_lat"], df_median["phone_long"], 'g')
plt.show()
