# import csv
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 10a czy podsumowanie uwzględnia wiersz tytułowy?
boston = pd.read_csv('boston.csv', header=0)
print(boston.describe())
print(boston)

# 10b
pd.plotting.scatter_matrix(boston.loc[:, 'crim':])
plt.show()

# 10c
# boston.boxplot(['zn', 'medv'], 'crim')
boston.boxplot('crim', 'zn') # dla 0 - TAK
boston.boxplot('crim', 'indus') # dla wysokich - TAK
boston.boxplot('crim', 'chas') # nie?
boston.boxplot('crim', 'nox') # najpierw nic, a potem skok
boston.boxplot('crim', 'rm') # nie widać?
boston.boxplot('crim', 'age') # im starszy ludzie, tym bardziej, potem znowu mniej
boston.boxplot('crim', 'dis') # spadające liniowe
boston.boxplot('crim', 'rad') # dla 24 tak
boston.boxplot('crim', 'tax') # dla wysokich wartości tak
boston.boxplot('crim', 'ptratio') # dla jednego ptratio tak
boston.boxplot('crim', 'black') # nie?
boston.boxplot('crim', 'lstat') # nie?
boston.boxplot('crim', 'medv') # opadająca krzywa
plt.show()

# 10d
boston.hist(column=['crim', 'tax', 'ptratio'], bins=30)
plt.show()
print(len(boston.loc[boston['crim']>20]))
print(len(boston.loc[boston['tax']>666])) # wtf?
print(len(boston.loc[boston['ptratio']>20]))

# 10e
print(len(boston.loc[boston['chas']==1]))

# 10f
print(boston['ptratio'].median())

# 10g
print(boston.loc[boston['medv']==boston['medv'].min()])

# 10h  w jaki sposób porównać jak wypada subset w stosunku do całego set?
print(len(boston.loc[boston['rm']>7]))
print(len(boston.loc[boston['rm']>8]))

print(boston.loc[boston['rm']>8].describe())