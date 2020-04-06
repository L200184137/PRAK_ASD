class MhsTIF(object):
    def __init__ (self, nama, NIM, kota):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        
    def __str__ (self) :
        s = self.nama + " " + str(self.NIM) + " " + self.kotaTinggal
        return s

    def getNim(self) :
        return self.NIM
    



daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]


def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i=0 ; j=0 ; k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i].NIM < separuhKanan[j].NIM:
                A[k].NIM = separuhKiri[i].NIM
                i = i + 1
            else :
                A[k].NIM = separuhKanan[j].NIM
                j = j + 1
            k = k+1

        while i < len(separuhKiri):
            A[k].NIM = separuhKiri[i].NIM
            i = i + 1
            k = k + 1

        while j < len(separuhKanan):
            A[k].NIM = separuhKanan[j].NIM
            j = j + 1
            k = k + 1
            
        return A


def quicksort(A):
    quicksortbantu (A,0, len(A) -1)
    return A

def quicksortbantu(A, awal, akhir):
    if awal < akhir :
        titikbelah = partisi(A, awal, akhir)
        quicksortbantu(A, awal, titikbelah -1)
        quicksortbantu(A, titikbelah +1, akhir)

def partisi(A, awal, akhir):
    nilaipivot = A[awal].getNim()

    penandakiri = awal +1
    penandakanan = akhir

    selesai = False
    while not selesai :
        while penandakiri <= penandakanan and \
              A[penandakiri].getNim() <= nilaipivot :
            penandakiri +=1
        while A[penandakanan].getNim() >= nilaipivot and \
            penandakanan >= penandakiri :
            penandakanan -=1
        if penandakanan < penandakiri :
            selesai = True
        else :
            temp = A[penandakiri]
            A[penandakiri] = A[penandakanan]
            A[penandakanan] = temp

    temp = A[awal]
    A[awal] = A[penandakanan]
    A[penandakanan] = temp

    return penandakanan

      
mergeSort(daftar)
for i in daftar:
    print(i)
    
print(" ")

quicksort(daftar)
for i in daftar:
    print(i)
