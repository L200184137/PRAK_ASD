class Pesan(object):
    def __init__ (self, p):
        self.pesan = p

    def apakahTerkandung (self, cari):
        if cari in self.pesan :
            return True
        else :
            return False

    def cetakPesan(self):
        return self.pesan

    def hitungVokal(self):
        vokal = "aiueoAIUEO"
        hitung = 0
        for i in self.pesan:
            if i in vokal :
                hitung += 1
        return hitung

    def hitungKonsonan(self):
        vokal = "aiueoAIUEO"
        berapa = 0
        for i in self.pesan:
            if i not in vokal :
                berapa += 1
        return berapa
