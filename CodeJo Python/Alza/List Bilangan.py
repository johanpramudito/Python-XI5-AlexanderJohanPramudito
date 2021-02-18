lst = []

n = int(input("Masukkan ada berapa angka yang akan dimasukkan ke dalam list : "))

for i in range(0,n):
    bil = int(input())

    lst.append(bil)

print("Nilai terbesar adalah", max(lst))
print("Nilai terkecil adalah", min(lst))
print("Rata-ratanya adalah", sum(lst)/n)