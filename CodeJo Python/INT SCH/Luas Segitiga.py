#Alexander Johan Pramudito/XI5/01

num1 = int(input("Masukkan panjang alas : "))
num2 = int(input("Masukkan tinggi : "))

def luas_segitiga(x,y):
    luas = float(x * y / 2)
    print("Luas Segitiga :", format(luas, '.2f'))

luas_segitiga(num1,num2)

