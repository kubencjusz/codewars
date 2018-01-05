# import csv
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 8a
college = pd.read_csv('College.csv', header=0)
print(college)
# # 8b
college = college.set_index('Uni')   # dobra praktyka to ustawić ją przy imporcie
# 8c i
print(college.describe())  # same as summary() in R
# 8c ii

import seaborn as sns
sns.pairplot(college.loc[:, :'Books'])

pd.plotting.scatter_matrix(college.loc[:, :'Books'])  # ??? jak pokazac kolumny, ktore maja wartosci NO/YES ?
plt.show()
# 8c iii
college.boxplot('Outstate', 'Private')
plt.show()
# 8c iv
college["Elite"] = "No"
college.loc[college['Top10perc']>50, 'Elite'] = "Yes"
college.boxplot('Outstate', 'Elite')
plt.show()
print(college["Elite"].value_counts())
# 8c v
college.hist(column=['Outstate', 'Books', 'Accept', 'PhD'], bins=7)
plt.show()
# 8c vi
print(college.loc[college['PhD']>100])

# 8a proby naokolo :P

'''
college = ""
with open('College.csv', newline='') as csvfile:   # college.csv is a file object so we're using newline=''
    college = csv.reader(csvfile, delimiter=',')
    college_list = []
    for row in college:
        college_list.append(row)
        # print(' '.join(row))

print(college_list)
Dictionary = {}
Dictionary = pd.DataFrame(Dictionary)
print(Dictionary)
'''