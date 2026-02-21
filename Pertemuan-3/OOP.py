class Negara:
    def __init__(self, nama, ibukota, benua):
        self.nama = nama
        self.ibukota = ibukota
        self.benua = benua

    def lokasi(self):
        print(f"{self.nama} berada di benua {self.benua}")

    def nama_ibukota(self):
        print(f"Ibukota negara {self.nama} adalah {self.ibukota}")

negara1 = Negara("indonesia", "Jakarta", "Asia")
negara2 = Negara("Malaysia", "Kuala Lumpur", "Asia")
negara3 = Negara("Jepang", "Tokyo", "Asia")

negara1.nama_ibukota()      #Output: Jakarta
negara1.lokasi()            #Output: Asia
negara2.nama_ibukota()      #Output: Kuala Lumpur
negara2.lokasi()            #Output: Asia
negara3.nama_ibukota()      #Output: Tokyo
negara3.lokasi()            #Output: Asia