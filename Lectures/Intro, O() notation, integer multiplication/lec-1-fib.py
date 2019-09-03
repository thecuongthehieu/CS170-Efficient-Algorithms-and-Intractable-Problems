# This code has a bug in it! Try to find it :) 

import time

def fib(n): 
  if n <= 1:  
     return n 
  else: 
     return fib(n-1) + fib(n-2)


def fibi(n):
  if n <= 1: 
     return n
  else:
    prev = 1
    prevprev = 1
    for i in xrange(2,n+1):  
       cur = prev+ prevprev
       prevprev = prev
       prev = cur
    return cur


def print_timing(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

def print_timing_no_res(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
        return "Done"
    return wrapper


tfib = print_timing(fib)

tfibi = print_timing(fibi)

tfibi_clean = print_timing_no_res(fibi)

print "Timing recursive fib:\n"


for i in [1,1,20,21,22,30]:
  print "timing recursive fib (%i)" % i 
  tfib(i)


print "\n Inductive...\n"

for i in [64000,128000,256000]:
  print "timing inductive fib(%i)" % i
  tfibi_clean(i)
