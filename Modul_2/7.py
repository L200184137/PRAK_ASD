def Manusia (object):
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def ambilNama(self, nama):
        return self.nama

    def ambilUmur(self, umur):
        return self.umur

    def ambilAlamat(self, nama):
        return self.alamat

class Mahasiswa(object):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__ (self):
        s = self.nama + ", NIM " + str(self.NIM)\
            + ", tinggal di " + self.kotaTinggal\
            + ", uang saku " + str(self.uangSaku)\
            + " tiap bulannya"
        return s

    def ambilNama(self):
        return self.nama

    def ambilNIM(self):
        return self.NIM

    def ambilUangSaku(self):
        return self.uangSaku

    def makan(self, s):
        print("saya baru saja makan", s, "sambil belajar")
        self.keadaan = "kenyang"

    def ambilKotaTinggal(self):
        return self.kotaTinggal

    def perbaruiKotaTinggal(self, p):
        self.kotaTinggal = p

    def tambahUangSaku(self, k):
        self.uangSaku += k

class MhsTIF(Mahasiswa):
    def katakanPy(self):
        print("Python is cool")

a = MhsTIF("Hafshah", 4092, "Solo", 200000)
a.ambilNama() # from class Manusia
a.makan("roti") # from class Mahasiswa
a.ambilNIM() # from class Mahasiswa
a.ambilUangSaku() # from class Mahasiswa
a.katakanPy() # from class MhsTIF
