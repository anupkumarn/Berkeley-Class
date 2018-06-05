#yield allows you to return a variable without losing the local variable values. In the example below yield is called within a function 
#where it returns the value to the calling function without losing track of the function variables.
#yield is a generator which preserves function local values.

def new_range(start,end,step):
    while start <= end:
        yield start
        start += step

for x in new_range(2,5,0.2):
    print (x)