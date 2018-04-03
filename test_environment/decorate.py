#!/usr/bin/env python
from  functools import wraps
def func1(func):
	print "you were into func 1"
	@wraps(func)
	def wrapper():
		func()
		print 'fun1 do some thing'
	return wrapper

def func2(func):
	print "I'm func2. you were into func2"
	def wrapper():
		func()
		print "func2 do some things"
	return wrapper
@func1
def demo():
	print "I'm demo"

demo()
print demo.__name__
