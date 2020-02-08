import time
 
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
        return (t2-t1)*1000.0
    return wrapper


# Karatsuba fast multiplication algorithm
# Copyright (c) 2011 Nayuki Minase
# 
# Requires Python version >= 2.7 because of long.bit_length().

# Requirement: _CUTOFF >= 64, or else there will be infinite recursion.
_CUTOFF = 1536;


def k_multiply(x, y):
    if x.bit_length() <= _CUTOFF or y.bit_length() <= _CUTOFF:  # Base case
        return x * y;
    else:
        n = max(x.bit_length(), y.bit_length())
        half = (n + 32) / 64 * 32
        mask = (1 << half) - 1
        xlow = x & mask
        ylow = y & mask
        xhigh = x >> half
        yhigh = y >> half
        
        a = k_multiply(xhigh, yhigh)
        b = k_multiply(xlow + xhigh, ylow + yhigh)
        c = k_multiply(xlow, ylow)
        d = b - a - c
        return (((a << half) + d) << half) + c

def multiply(x,y):
    if x.bit_length() <= _CUTOFF or y.bit_length() <= _CUTOFF:  # Base case
        return x * y;
    else:
        n = max(x.bit_length(), y.bit_length())
        half = (n + 32) / 64 * 32
        mask = (1 << half) - 1
        xlow = x & mask
        ylow = y & mask
        xhigh = x >> half
        yhigh = y >> half
        
        a = multiply(xhigh, yhigh)
        b = multiply(xlow, yhigh)
        c = multiply(xlow, ylow)
        d = multiply(ylow,xhigh) + c
        return (((a << half) + d) << half) + c

def py_multiply(x,y):
    return x*y


def demo_multiply():
    dude = print_timing_no_res(multiply)


    print "multiplying 3**10000 and 7**10000"
    first = dude(3**100000,7**100000)
    prev = first

    for i in [200000,400000,800000]:
        print "multiplying 3**%s and 7**%s" % (i,i)
        cur = dude(3**i,7**i)
        print "\ntime went up by factor of:", cur/prev
        print 
        prev = cur

def demo_py_multiply():
    dude = print_timing_no_res(py_multiply)

    print "multiplying 3**100000 and 7**100000"
    first = dude(3**100000,7**100000)
    prev = first

    for i in [200000,400000,800000,1600000]:
        print "multiplying 3**%s and 7**%s" % (i,i)
        cur = dude(3**i,7**i)
        print "\ntime went up by factor of:", cur/prev
        print 
        prev = cur


print "-----------\n Demo of elementary school multiply. \n ---------"
demo_multiply()

print "-----------\n Demo of python multiply.\n ----------"
demo_py_multiply()



