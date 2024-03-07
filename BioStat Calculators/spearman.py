import numpy
import scipy.stats as ss

x_values = []

add_x = input("Enter the independent values:")
split_x = add_x.split(' ')
x_values.extend(split_x)
x_values = [int(g) for g in x_values]

avg_x = sum(x_values)/len(x_values)

y_values = []

add_y = input("Enter the dependent values:")
split_y = add_y.split(' ')
y_values.extend(split_y)
y_values = [int(g) for g in y_values]

rx = ss.rankdata(x_values)
print(rx)
rankx = len(x_values) - ss.rankdata(x_values).astype(int) +1
print(rankx)

ry = ss.rankdata(y_values)
print(ry)
ranky = len(y_values) - ss.rankdata(y_values).astype(int) +1
print(ranky)

diff = []
for i in range(len(x_values)):
    add_diff = (rankx[i] - ranky[i])**2
    diff.append(add_diff)
print(diff)
print(sum(diff))

pearson = 1 - (6*(sum(diff)))/((len(x_values)**3 - len(x_values)))
print(pearson)
