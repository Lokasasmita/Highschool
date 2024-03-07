import numpy

n_values = []

add_n = input("Enter the values:")
split_n = add_n.split(' ')
n_values.extend(split_n)
n_values = [int(g) for g in n_values]

totalN = numpy.sum(n_values)

final = []
for i in range(len(n_values)):
    addf = (n_values[i]/totalN)**2
    final.append(addf)
print(final)
finalsum = numpy.sum(final)
print(finalsum)

print("Simpson's Index:" + str(1-finalsum))