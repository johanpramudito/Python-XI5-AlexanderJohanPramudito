num1 = int(input("Masukkan angka : "))

faktor = []

def pembagi_habis(x):
    for i in range(1,x):
        if (x % i) == 0:
            faktor.append(i)
    return faktor
    
print("Bilangan",num1, "dapat dibagi habis oleh bilangan: ", pembagi_habis(num1))