# mencari nilai penjumlahan dari nilai asli suatu bilangan

def penjumlah(n):
    if n <= 1:
        return n
    else:
        return n + penjumlah(n-1)

bil = int(input('input bilangan : '))

if bil < 0:
    print('Masukkan bilangan positif')
else:
    print('Penjumlah dari nilai asli', bil, 'adalah', penjumlah(bil))