#Alexander Johan Pramudito/XI5/01

num = int(input("bilangan : "))

if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            print(num, 'bukan bilangan prima')
            print(i, "kali", num/i, "=", num)
            break
        else:
            print(num, "adalah bilangan prima")
else:
    print(num, "bukan bilangan prima")