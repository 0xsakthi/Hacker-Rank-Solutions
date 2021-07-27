#!/usr/bin/python3
def split_and_join(line):
    # write your code here
    spliting = line.split()
    joining = "-".join(spliting)
    return joining    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
