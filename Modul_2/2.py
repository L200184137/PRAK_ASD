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
