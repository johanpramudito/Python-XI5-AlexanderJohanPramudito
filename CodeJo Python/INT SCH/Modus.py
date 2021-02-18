#Alexander Johan Pramudito/XI5/01

num1 = int(input("Masukkan jumlah angka yang ingin dimasukkan : "))
num2 = input("List angka yang akan dimasukkan\n(Pisahkan angka dengan spasi, bukan tanda koma) : ")
list_angka = num2.split()
def Modus(list_angka):
    count = 0
    terbanyak = list_angka[0]

    for i in list_angka:
        flag = list_angka.count(i)
        if flag >= count:
            count = flag
            terbanyak = i
    return(terbanyak)

print("Modus terbanyak dari list angka tersebut :", Modus(list_angka))

