import numpy

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

avg_y = sum(y_values)/len(y_values)

if len(x_values) != len(y_values):
    print("Please make sure number of dependent and independent variables are equal")
    quit()

subtracted_x = []
for i in range (len(x_values)):
    xsubbed = x_values[i] - avg_x
    subtracted_x.append(xsubbed)

subtracted_y = []
for i in range (len(y_values)):
    ysubbed = y_values[i] - avg_y
    subtracted_y.append(ysubbed)

x_squared = []
for i in range (len(subtracted_x)):
    xsquare =subtracted_x[i]**2
    x_squared.append(xsquare)
x2val = numpy.sum(x_squared)

y_squared = []
for i in range (len(subtracted_y)):
    ysquare =subtracted_y[i]**2
    y_squared.append(ysquare)
y2val = numpy.sum(y_squared)

mutliplied = []
for i in range (len(x_values)):
    multiply = (subtracted_x[i])*(subtracted_y[i])
    mutliplied.append(multiply)
mulval = numpy.sum(mutliplied)

pearson = mulval/((x2val*y2val)**0.5)
print(pearson)

