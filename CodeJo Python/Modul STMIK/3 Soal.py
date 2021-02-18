# Soal 1
def soal1():
    a = int(input("Masukkan bilangan pertama : "))
    b = int(input("Masukkan bilangan kedua : "))
    c = int(input("Masukkan bilangan ketiga : "))

    print((a+b+c)/3)

#Soal 2
def soal2():
    print("Program ini hanya mencakup fungsi f(x) = 2x^3 + 2x + 15/x)")
    d = int(input("Masukkan x : "))

    e = 2*(d**3)+2*d+15/d
    print(e)

#Soal 3
lst = []
def soal3():
    print("Tukar nilai bilangan A,B,C,D => B,D,A,C")
    print("Masukkan 4 angka yang akan dimasukkan!")
    for i in range (0,4):
        bil = int(input())
        lst.append(bil)
    print(lst)

    def pindah_tempat(list, pos1, pos2, pos3, pos4):
        list[pos1], list[pos2], list[pos3], list[pos4] = list[pos2], list[pos4], list[pos1], list[pos3]
        return list
    
    pos1, pos2, pos3, pos4 = 1, 2, 3, 4
    print(pindah_tempat(lst, pos1-1, pos2-1, pos3-1, pos4-1))

print("Pilih Soal : ")
print("1. Soal Rata-Rata 3 Bilangan")
print("2. f(x)")
print("3. Tukar nilai")

choice = input("Masukkan pilihan(1/2/3) : ")
if choice == '1':
    soal1()
elif choice == '2':
    soal2()
elif choice == '3':
    soal3()
else:
    print("Masukan salah")