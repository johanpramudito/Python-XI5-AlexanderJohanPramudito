import datetime

Tanggal = datetime.datetime.now()

Nama = input("Masukkan nama : ")
Usia = int(input("Masukkan usia saat ini : "))

def usia_50(x,y):
    a = int(50) - y
    b = Tanggal.year + a
    print("Nama anda", x, ",", "anda berusia", y, "tahun. Pada tahun", b, "anda akan berusia", 50, "tahun.")

usia_50(Nama,Usia)