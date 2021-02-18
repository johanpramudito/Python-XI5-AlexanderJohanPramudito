def konversi(x):
    baris = len(str(x))
    angka1 = x//pow(10, baris-1)
    return (pow(2, baris-1) * angka1) + konversi(x % pow(10, baris-1))

binary = int(input("Masukkan angka biner : "))
desimal = konversi(binary)

print(desimal)