import numpy

cond1_values = []

add_cond1 = input("Enter the list of observed values in the first condition:")
split_cond1 = add_cond1.split(' ')
cond1_values.extend(split_cond1)
cond1_values = [int(g) for g in cond1_values]

totalO1 = numpy.sum(cond1_values)

cond2_values = []

add_cond2 = input("Enter the list of observed values in the second condition:")
split_cond2 = add_cond2.split(' ')
cond2_values.extend(split_cond2)
cond2_values = [int(g) for g in cond2_values]

totalO2 = numpy.sum(cond2_values)

sumO = []
for i in range(len(cond1_values)):
    addsumO = cond1_values[i] + cond2_values[i]
    sumO.append(addsumO)
totalO = numpy.sum(sumO)

E1_values = []
for i in range(len(cond1_values)):
    addE1 = (cond1_values[i] + cond2_values[i])*totalO1/totalO
    E1_values.append(addE1)

E2_values = []
for i in range(len(cond2_values)):
    addE2 = (cond1_values[i] + cond2_values[i])*totalO2/totalO
    E2_values.append(addE2)

print(E1_values)
print(E2_values)

OminusE1 = []
for i in range(len(E1_values)):
    addOminusE1 = ((cond1_values[i]-E1_values[i])**2)/E1_values[i]
    OminusE1.append(addOminusE1)

OminusE2 = []
for i in range(len(E2_values)):
    addOminusE2 = ((cond2_values[i]-E2_values[i])**2)/E2_values[i]
    OminusE2.append(addOminusE2)

total1 = numpy.sum(OminusE1)
total2 = numpy.sum(OminusE2)
print(total1 + total2)