from lib import bagianbawah
from lib import atap
from lib import harga 
from lib import awalan


loopmaster=True
while loopmaster:
    print ("PT. Kontraktor Rumah Idaman")
    print ("Menghitung Prediksi Biaya Untuk Membangun Sebuah Bangunan")
    print(" ")
    print(" ")
    if __name__ == "__main__":
    
      a = awalan.Upah(1000000)
      b = awalan.Biayabawah(3000000)
      c = awalan.Biayaatap(500000)
  
      a.tampilan()
      a.rincian()
      a.jadi()
      print(" ")
      b.tampilan()
      b.rincian()
      b.jadi()
      print(" ")
      c.tampilan()
      c.rincian()
      c.jadi()
      print(" ")
      print ("")
      print ("")
    print ("M E N U")
    print ("")
    print ("Pilih Bentuk Atap Rumah Anda")
    print ("")
    print ("1. Prisma Segitiga 2. Kerucut 3. Setengah Bola")
    print ("")
    pilihan = int (input ("Masukkan pilihan: "))
    print ("")
    
    if pilihan == 1 :
      print ("Menghitung Prediksi Biaya Rumah dengan Atap Prisma Segitiga")
      x = int(input("Masukkan jumlah lantai bangunan: "))
      p = int(input("Masukkan panjang bangunan: "))
      l = int(input("Masukkan lebar bangunan: "))
      t = int(input("Masukkan tinggi bangunan: "))
      print ("")
      print ("")
      print ("Luas Bangunan = {}". format(bagianbawah.luastanah().add(p, l)))
      print ("Luas Permukaan Atap = {}". format(atap.prismasegitiga().add(p, l, t)))
      print ("")
      print ("Rincian Harga")
      print ("")
      
      print ("Upah Tenaga Borongan = {}". format(harga.upahpemborong().add(x, p, l)))
      print ("Biaya Material Bawah = {}". format(harga.materialbawah().add(x, p, l)))
      print ("Biaya Material Atas = {}". format(harga.materialatapprisma().add(p, l, t)))
      print ("Biaya Total = {}". format(harga.totalprisma().add(x, p, l, t)))

    elif pilihan == 2 :
      print ("Menghitung Prediksi Biaya Rumah dengan Atap Kerucut")
      x = int(input("Masukkan jumlah lantai bangunan: "))
      p = int(input("Masukkan panjang bangunan: "))
      l = int(input("Masukkan lebar bangunan: "))
      t = int(input("Masukkan tinggi bangunan: "))
      r = int(input("Masukkan jari-jari kerucut: "))
      s = int(input("Masukkan garis pelukis kerucut: "))
      print ("")
      print ("")
      print ("Luas Bangunan = {}". format(bagianbawah.luastanah().add(p, l)))
      print ("Luas Permukaan Atap = {}". format(atap.kerucut().add(r, s)))
      print ("")
      print ("Rincian Harga")
      print ("")
      
      print ("Upah Tenaga Borongan = {}". format(harga.upahpemborong().add(x, p, l)))
      print ("Biaya Material Bawah = {}". format(harga.materialbawah().add(x, p, l)))
      print ("Biaya Material Atas = {}". format(harga.materialatapkerucut().add(r, s)))
      print ("Biaya Total = {}". format(harga.totalkerucut().add(x, p, l, r, s)))


    elif pilihan == 3 :
      print ("Menghitung Prediksi Biaya Rumah dengan Atap Setengah Bola")
      x = int(input("Masukkan jumlah lantai bangunan: "))
      p = int(input("Masukkan panjang bangunan: "))
      l = int(input("Masukkan lebar bangunan: "))
      t = int(input("Masukkan tinggi bangunan: "))
      r = int(input("Masukkan jari-jari kerucut: "))
      print ("")
      print ("")
      print ("Luas Bangunan = {}". format(bagianbawah.luastanah().add(p, l)))
      print ("Luas Permukaan Atap = {}". format(atap.setengahbola().add(r)))
      print ("")
      print ("Rincian Harga")
      print ("")
      
      print ("Upah Tenaga Borongan = {}". format(harga.upahpemborong().add(x, p, l)))
      print ("Biaya Material Bawah = {}". format(harga.materialbawah().add(x, p, l)))
      print ("Biaya Material Atas = {}". format(harga.materialatapsetengahbola().add(r)))
      print ("Biaya Total = {}". format(harga.totalsetengahbola().add(x, p, l, r)))
    
    print ("")
    lagi = input ("Mau kembali ke menu ? (y/n) : ")
    print ("")
    if lagi == 'n' :
        loopmaster = False