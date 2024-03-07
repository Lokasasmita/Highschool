import numpy

O_values = []

add_O = input("Enter the observed values:")
split_O = add_O.split(' ')
O_values.extend(split_O)
O_values = [int(g) for g in O_values]

totalO = numpy.sum(O_values)

E_ratio = []

add_E = input("Enter the expected ratio:")
split_E = add_E.split(' ')
E_ratio.extend(split_E)
E_ratio = [int(g) for g in E_ratio]

totalE = numpy.sum(E_ratio)

if len(O_values) != len(E_ratio):
    print("Please make sure number of dependent and independent variables are equal")
    quit()

E_values = []
for i in range(len(O_values)):
    addE = totalO*(E_ratio[i]/totalE)
    E_values.append(addE)

subtracted = []
for i in range (len(E_values)):
    subbed = O_values[i] - E_values[i]
    subtracted.append(subbed)

oesquared = []
for i in range (len(subtracted)):
    oesq = (subtracted[i]**2)/E_values[i]
    oesquared.append(oesq)
final = numpy.sum(oesquared)

print(final)
