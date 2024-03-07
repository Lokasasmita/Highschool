import os

#Setting the parameters
a = 5
b = 6
c = 2
d = 8

voxel_array = [
    [a, b],
    [c, d]
]

#Step 1
density = a+b+c+d

detector = [
    [int((4*a + b+c+d)-density)/3, int((4*b +a+c+d)-density)/3],
    [int((4*c + a+b+d)-density)/3, int((4*d +a+b+c)-density)/3]
]

def print_detector():
    print("----------------")
    for i in  range(len(detector)):
        print("|{:^5}|{:^5}|".format(detector[i][0], detector[i][1]))
    print("----------------")

print_detector()