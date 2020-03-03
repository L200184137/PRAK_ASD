
#masih ada yang error

import random
def tebak():
    max = 7
    start = 1

    x = random.randrange(1,100,1)
    while (start <= max):
        s = 'Masukkan tebakan ke- ' + str(start) + ':> '
        i = int(input(s))
        if(i == x):
            print ('Ya, anda benar')
        elif(i > x):
            print ('Itu terlalu besar. Coba lagi')
        elif(i < x):
            print ('Itu terlalu kecil. Coba lagi')
        start +=1
