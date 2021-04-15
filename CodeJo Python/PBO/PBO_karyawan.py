import datetime

class Karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, tempat_lahir, tanggal_lahir, alamat, pendidikan_akhir, mulai_bekerja, status_karyawan, gaji):
        self.nama = nama
        self.tempat_lahir = tempat_lahir
        self.tanggal_lahir = tanggal_lahir
        self.alamat = alamat
        self.pendidikan_akhir = pendidikan_akhir
        self.mulai_bekerja = mulai_bekerja
        self.status_karyawan = status_karyawan
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total Karyawan:", Karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Tempat Lahir :", self.tempat_lahir)
        print("Tanggal Lahir :", self.tanggal_lahir)
        print("Umur :", "{:.0f}".format((((datetime.date.today())-self.tanggal_lahir).days)/365), "Tahun")
        print("Alamat :", self.alamat)
        print("Pendidikan Akhir :", self.pendidikan_akhir)
        print("Mulai Bekerja :", self.mulai_bekerja)
        print("Lama Bekerja :", "{:.0f}".format((((datetime.date.today())-self.mulai_bekerja).days)/365), "Tahun")
        print("Status Karyawan :", self.status_karyawan)
        print("Gaji :", self.gaji)

# Membuat objek pertama dari kelas Karyawan
karyawan1 = Karyawan("Budi", "Yogyakarta", datetime.date(1980,11,1), "Bener IX RT14/RW05, Tegalrejo, Yogyakarta", "SMA", datetime.date(2002,2,2), "Karyawan Tetap", 10000000)
# Membuat objek kedua dari kelas Karyawan
karyawan2 = Karyawan("Andi", "Jakarta", datetime.date(1991,10,7), "Gamping Tengah RT04/RW01, Gamping, Sleman", "S1", datetime.date(2007,8,4), "Karyawan Tetap", 20000000)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
print("Total karyawan :", Karyawan.jumlah_karyawan)