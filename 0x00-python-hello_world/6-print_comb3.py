#!/usr/bin/python3
for i in range(8):
    for j in range(10):
        if i < j:
            print('{}{}'.format(i, j), sep='', end=', ')
print('89')
