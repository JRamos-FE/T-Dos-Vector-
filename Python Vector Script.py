import math

print('Enter your choice of unit: ')
print('(1)  r/theta = degrees')
print('(2)  x/y')

response = int(input())
n = int(input('Enter desired number of vectors: '))
x = []
y = []
for i in range(n):
    if response == 1:
        r = float(input('Input r value: '))
        theta = float(input('Input theta: '))
        x.append(r * math.cos((theta / 180) * math.pi))
        y.append(r * math.sin((theta / 180) * math.pi))
    else:
        X = float(input('Input X value: '))
        Y = float(input('Input Y value: '))
        x.append(X)
        y.append(Y)
       
result_x = 0
result_y = 0
for i, j in zip(x,y):
    result_x = result_x + i
    result_y = result_y + j
print('Enter unit of measurement for result:    ')

response_2 = int(input('(1) r/theta     or  (2) x/y'))
if response_2 == 1:
    result_theta = math.atan(result_y / result_x)
    result_r = ((result_x ** 2) + (result_y ** 2)) ** 0.5
    print('Result r = ' + str(result_r))
    print('Result theta = ' + str((result_theta / math.pi) * 180))
else:
    print('Result x = ' + str(result_x))
    print('Result y = ' + str(result_y))
