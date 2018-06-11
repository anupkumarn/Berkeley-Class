import numpy as np 





class _file_operations():
    def write_my_file(my_arr):
        wfile=open(filpath,'w')
        a.tofile(wfile,':',format="%s")
        wfile.close()

    def read_my_file():
        rfile=open('filpath','r')
        sentences=rfile.readlines()
        print(sentences)
        rfile.close()

my_range=np.arange(5,45,7)

filpath='C:\\users\\anup\\Dev\\Data\array_file.txt'
print(filpath)



