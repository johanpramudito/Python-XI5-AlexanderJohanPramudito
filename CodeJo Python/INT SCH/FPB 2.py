#Alexander Johan Pramudito/XI5/01

def hitung_FPB(x,y):
    
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % 1 == 0) and (y % 1 == 0)):
            fpb = i
    return fpb

num1 = 106
num2 = 24

print("FPB dari ", num1, "dan", num2, "=", hitung_FPB(num1,num2))