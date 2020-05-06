import math

class Upah:
    def __init__(self,gaji):
        self.gaji=gaji

    def tampilan(self):
        print("Diketahui biaya upah tenaga pemborong permeter adalah", self.gaji)

    def rincian (self):
        print("uang tersebut diperoleh dari uang makan dan upah permeternya yaitu sebesar", self.gaji, "permeter")

    def jadi (self):
        print("Jadi semakin luas bangunan, maka semakin banyak biaya upah pemborong yang diperlukan")
        
class Biayabawah:
    def __init__(self,bawah):
        self.bawah=bawah

    def tampilan(self):
        print("Diketahui biaya material bagian bawah permeter adalah", self.bawah)

    def rincian (self):
        print("nominal tersebut sudah kami perhitungkan sebelumnya, dari harga bahan saat ini", self.bawah,  "permeter")

    def jadi (self):
        print("Jadi semakin luas bangunan, maka semakin banyak biaya material yang diperlukan")
        
class Biayaatap:
    def __init__(self,atap):
        self.atap=atap

    def tampilan(self):
        print("Diketahui biaya material bagian atap permeter adalah", self.atap)

    def rincian (self):
        print("nominal tersebut sudah kami perhitungkan sebelumnya, dari harga bahan saat ini", self.atap,  "permeter")

    def jadi (self):
        print("Jadi semakin luas bangunan, maka semakin banyak biaya material atap yang diperlukan")
        




