#!/usr/bin/python3
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    n = set(arr)
    n.remove(max(n))
    print(max(n))
