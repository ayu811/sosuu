import matplotlib.pyplot as plt

def handan(num):
    if 1 >= num:
        return 0
    for i in range(2,num):
        if num % i == 0:
            return 0
    return 1

cun = 1000
file = open("sosu.txt",'w')
all_n = 0
all_p = 0
per = 0
#y = []
for j in range(2,cun):
    if handan(j) == 1:
        all_n += 1
        all_p += 1
        per = all_p / all_n
        file.write(str(per) + '\n')
        
        print(str(j) + ':' 'True')
    else:
        all_n += 1
        file.write(str(per) + '\n')
        print(str(j) + ':' + 'False')
