num1 = int(input("Masukkan angka : "))

def ganjil_genap(x):
    if x != 0:
        for i in range(0, x):
            if (x % 2) == 0:
                print("Anda memasukkan bilangan", x,',', x, "adalah bilangan genap")
            else:
                print("Anda memasukkan bilangan", x,',', x, "adalah bilangan ganjil")
            break
    else:
        print("Anda memasukkan bilangan", x,',', x, "adalah bilangan genap")

ganjil_genap(num1)