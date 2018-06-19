# Anup Kumar (anup.kn@gmail.com) Midterm
import pylab as plb 

# Create and array with 12 elements having consecutive odd numbers 
A = plb.arange(5,30,2)
print("The origial array is: ", A)

def calc_sma(arr, window = 2):
    ones = plb.ones(window)/window
    mov_avg = plb.convolve(arr, ones, 'valid')
    print("Current window with = ", window)
    print("The SMA result is: ", mov_avg)
    return mov_avg

def calc_cma(arr):
    cum_sum_arr = plb.cumsum(arr)
    cum_avg_list = []
    for i, x in enumerate(cum_sum_arr, 1):
        if i > 1 :
            cum_avg_list.append( x/i )
    cum_avg_arr = plb.asarray(cum_avg_list)
    print("The CMA of this SMA is: ", cum_avg_arr)
#    return cum_avg_arr

# Calculate SMA of array with default window
B = calc_sma(A)
calc_cma(B)

# Calculate SMA of array with window = 4
C = calc_sma(A, 4)
calc_cma(C)

# Sin of array B
B_sin = plb.sin(B)

# Sin of array B
C_sin = plb.sin(C)

# Plot the sin of arrays B and C
plb.figure(figsize=(6,3), dpi=100)
plb.plot(B,B_sin, color="red", linewidth=1.2, linestyle="-", label="B sin")
plb.plot(C, C_sin, color="blue", linewidth=1.2, linestyle="-.", label="C sin")
plb.legend(loc="upper right")
plb.grid()
plb.pause(10)
