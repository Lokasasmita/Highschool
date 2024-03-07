import numpy

x1_values = []

add_x1 = input("Enter the first list of independent values:")
split_x1 = add_x1.split(' ')
x1_values.extend(split_x1)
x1_values = [int(g) for g in x1_values]

avg_x1 = sum(x1_values)/len(x1_values)

x2_values = []

add_x2 = input("Enter the second list of independent values:")
split_x2 = add_x2.split(' ')
x2_values.extend(split_x2)
x2_values = [int(g) for g in x2_values]

avg_x2 = sum(x2_values)/len(x2_values)

x1m = []
for i in range(len(x1_values)):
    x1m_add = (x1_values[i]-avg_x1)**2
    x1m.append(x1m_add)
var_x1m = (numpy.sum(x1m))/(len(x1_values))

x2m = []
for i in range(len(x2_values)):
    x2m_add = (x2_values[i]-avg_x2)**2
    x2m.append(x2m_add)
var_x2m = (numpy.sum(x2m))/(len(x2_values))

t_test = (max(avg_x1, avg_x2) - min(avg_x1, avg_x2))/((var_x1m/len(x1_values)) + (var_x2m/len(x2_values)))**0.5
print(t_test)