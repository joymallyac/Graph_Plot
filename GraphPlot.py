#@Author Jchakra
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Reading the .csv file
df = pd.read_csv('C:/Research_Emerson_Murphy_Hill/Python/Result.csv')

# Printing data
print(df)

# Grouping Female and Male data separately
female_merger = (df['percent_merged'].groupby(df['creator_gender']).head()[0],df['percent_merged'].groupby(df['creator_gender']).head()[2])
male_merger = (df['percent_merged'].groupby(df['creator_gender']).head()[1],df['percent_merged'].groupby(df['creator_gender']).head()[3])
 
# data to plot
n_groups = 2
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8
female_color = '#009E73'
male_color = '#E69F00'
 
rects1 = plt.bar(index, female_merger, bar_width,
                 alpha=opacity,
                 color=female_color,
                 label='Female')
 
rects2 = plt.bar(index + bar_width, male_merger, bar_width,
                 alpha=opacity,
                 color=male_color,
                 label='Male')
 
plt.xlabel('Merger or Closer')
plt.ylabel('Avg Merging Rate')
plt.title('Tug of War')
plt.xticks(index + bar_width, ('Female', 'Male'))
plt.legend()
 
plt.tight_layout()
plt.show()