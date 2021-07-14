#!/usr/bin/python3
n = int(input())
res = []
for i in range(n):
    m = input().split()
    if m[0] == 'append':
        res.append(int(m[1]))
    elif m[0] == 'insert':
        res.insert(int(m[1]),int(m[2]))
    elif m[0] == 'remove':
        res.remove(int(m[1]))
    elif m[0] == 'sort':
        res.sort()
    elif m[0] == 'pop':
        res.pop()
    elif m[0] == 'print':
        print(res)
    else:
        res.reverse()
