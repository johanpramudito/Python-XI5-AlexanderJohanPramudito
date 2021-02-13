lst = []

n = int(input("Masukkan ada berapa angka yang akan dimasukkan : "))

for i in range (0,n):
    bil = int(input())

    lst.append(bil)

print("Rata-rata jumlah bilangan tersebut adalah", sum(lst)/n)