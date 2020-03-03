def katakan(bilangan):
    angka = ["", "satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan", "Sepuluh","Sebelas"]
    hasil = "  "
    n = int(bilangan)
    if n>=0 and n<=11:
        hasil = hasil + angka[n]
    elif n<20:
        hasil = katakan(n%10) + " Belas"
    elif n<100:
        hasil = katakan(n/10) + " Puluh" + katakan(n%10)
    elif n<200:
        hasil = " Seratus" + katakan(n-100)
    elif n<1000:
        hasil = katakan(n/100) + " Ratus" + katakan(n%100)
    elif n<2000:
        hasil = " Seribu" + katakan(n-1000)
    elif n<10000:
        hasil = katakan(n/1000) + " Ribu" + katakan(n%1000)
    elif n<20000:
        hasil = " Sepuluh Ribu" + katakan(n-10000)
    elif n<100000:
        hasil = katakan(n/10000) + " Puluh" + katakan(n%10000)
    elif n<20000:
        hasil = " Seratus" + katakan(n-100000)
    elif n<1000000:
        hasil = katakan(n/100000) + " Ratus" + katakan(n%100000)
    elif n<2000000:
        hasil = " Satu Juta" + katakan(n-1000000)
    elif n<10000000:
        hasil = katakan(n/1000000) + " Juta" + katakan(n%1000000)
    elif n<20000000:
        hasil = " Satu Milyar" + katakan(n-10000000)
    else:
        hasil = " Angka hanya sampai satu milyar"
    return hasil
