def jumlahHurufVokal(x):
    vokal =['a','i','u','e','o', 'A','I','U','E','O']
    a = 0
    hitung = 0
    for i in x :
        if i in vokal :
            a +=len (i)
        else:
            a += 0
    hitung = len (x),a
    return hitung
