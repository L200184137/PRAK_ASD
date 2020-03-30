class MhsTIF(object):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__(self):
        x = self.nama + ', umur' + str(self.umur) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku ' + str(self.uangSaku) \
            + 'tiap bulannya.'
        return x

    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilKota(self):
        return self.kotaTinggal
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF("Ika", 10, "Sukoharjo", 240000)
c1 = MhsTIF("Budi", 51, "Sragen", 230000)
c2 = MhsTIF("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTIF("Chandra", 18, "Surakarta", 235000)
c4 = MhsTIF("Eka", 4, "Boyolali", 240000)
c5 = MhsTIF("Fandi", 31, "Salatiga", 250000)
c6 = MhsTIF("Deni", 13, "Klaten", 245000)
c7 = MhsTIF("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTIF("Janto", 23, "Klaten", 245000)
c9 = MhsTIF("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTIF("Khalid", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def swap(A,p,q):
    tmp = A[p]
    a[p]=a[q]
    a[q]=tmp

def cariPosisiYangTerkecil(A,dariSini,sampaiSini):
    posisiYangTerkecil=dariSini
    for i in range(dariSini+1,sampaiSini):
        if A[i]<A[posisiYangTerkecil]:
            posisiYangTerkecil=i
    return posisiYangTerkecil

def cariTerkecil(A):
    baru = A[0].NIM

    for i in range(len(A)):

        if(A[i].NIM<baru):

            baru = A[i].NIM

    return baru

def urutkan(A):

    baru = {}

    for i in range(len(A)):

        baru[A[i].nama] = A[i].NIM

    listofTuples = sorted(baru.items(), key=lambda x: x[1])

    for elem in listofTuples :

        print(elem[0] , ":" , elem[1] )





urutkan(Daftar)
