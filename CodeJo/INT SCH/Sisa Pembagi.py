#Alexander Johan Pramudito/XI5/01

num1 = int(input("Masukkan jumlah bebek : "))
num2 = int(input("Masukkan jumlah teman : "))

def pembagian_sisa(x,y):
    bagi = int(x / y)
    sisa = x % y
    print("masing-masing", bagi)
    print("bersisa", sisa)

pembagian_sisa(num1,num2)

