from numpy import arange, int32

a=arange(1,20,1, dtype=int32)

print(a)

def range_gen(start, end, step):
    while start <= end:
        yield start
        start += step

for x in range_gen(a[0],a[len(a)-1],0.2):
    if x > 12 and x < 14:
        print(x)

