#!/usr/bin/python3

def leap(year):
	leap = False
	if year%400 == 0:
		leap = True
	elif year%4 == 0 and year%100 != 0:
		leap = True
	return leap
answer = leap(int(input()))
print(answer)