num1 = int(input("Masukkan bilangan pertama : "))
num2 = int(input("Masukkan bilangan kedua : "))

def fpb(x,y):
    if y == 0:
        return x
    else:
        return fpb(y,x%y)
    
def kpk(x,y):
    return x*y/fpb(num1,num2)

print (format(kpk(num1,num2), '.0f'))