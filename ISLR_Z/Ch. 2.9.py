# import csv
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 9a
auto = pd.read_csv('Auto.csv', header=0,na_values='?')
print(auto)
auto.isnull().sum()
auto.dtypes
auto = auto.fillna(auto['horsepower'].mean())
# quantitative: mpg, cylinders, displacement, horsepower, weight, acceleration
# qualitative: origin, name

# 9b  czy da się to jakoś ładnie złączyć w jedno?
#print("Max is:", "\n", auto.loc[auto['mpg':'year']].max())
# print(auto.loc[:, :'year'].min()) or print(auto.iloc[:, :7].min())
print("Min is:", "\n", auto.loc[:, :'year'].min())
print("Max is:", "\n", auto.loc[:, :'year'].max())


# print(pd.merge(auto.max().to_frame(), auto.min().to_frame(), how="left"))

# 9c
print("Mean is:", "\n", auto.loc[:, :'year'].mean())
print("Standard Deviation is:", "\n", auto.loc[:, :'year'].std())

# 9d   Na pewno da się to zrobić ładniej...
print("Min is:", "\n", auto.drop(index=range(10, 86)).loc[:, :'year'].min())
print("Max is:", "\n", auto.drop(index=range(10, 86)).loc[:, :'year'].max())
print("Mean is:", "\n", auto.drop(index=range(10, 86)).loc[:, :'year'].mean())
print("Standard Deviation is:", "\n", auto.drop(index=range(10, 86)).loc[:, :'year'].std())

# 9e dlaczego nie pokazuje mi horsepower w scatter matrix?
pd.plotting.scatter_matrix(auto.loc[:, :'name'])
plt.violinplot(auto['weight'])
plt.hist(auto['weight'])
plt.show()
auto.boxplot('weight')
auto.boxplot('acceleration')
auto.boxplot('displacement')
auto.boxplot('mpg')
auto.boxplot('cylinders')
auto.boxplot('origin') # najwięcej 1?
auto.boxplot('year') # ciekawe - identyczna ilość samochodów w każdym roku?
auto.boxplot('displacement', 'acceleration') # szybki spadek, a później stabilizacja
auto.boxplot('displacement', 'cylinders') # wyraźna zależność liniowa
auto.boxplot('displacement', 'origin') # origin 2 i 3 są podobne, w 1 są jakieś dziwne rzeczy
auto.boxplot('weight', 'origin') # wyraźna zależność liniowa odwrotnie proporcjonalna
auto.boxplot('weight', 'cylinders') # wyraźna zależność liniowa


# auto.boxplot('year', 'origin') nieciekawe

# 9f
auto.boxplot('displacement', 'mpg') # hiperbola
auto.boxplot('weight', 'mpg') # hiperbola
auto.boxplot('mpg', 'year') # tak, ustawiłbym year w zbiory 3- letnie
auto.boxplot('mpg', 'cylinders') # może, ale nie liniowo
auto.boxplot('mpg', 'origin') # może, ale trochę za mało wartości
plt.show()

# auto.boxplot('mpg', 'acceleration') # nie

# moje strzały: year, weight, cylinders, displacement