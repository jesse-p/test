#!/usr/bin/env python

def func1(num):
	age = num
	def func2():
		age +=1
		return age
	return func2


p = func1(1)
print p()
