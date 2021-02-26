import matplotlib.pyplot as plt

def handan(num):
    if 1 >= num:
        return 0
    for i in range(2,num):
        if num % i == 0:
            return 0
    return 1

cun = 10000

y = []
for j in range(2,cun):
    if handan(j) == 1:
        y.append(j)
        print(str(j) + ':' 'True')
    else:
        print(str(j) + ':' + 'False')

file = open('sosu.txt','w')
file.writelines(str(y))
file.close()