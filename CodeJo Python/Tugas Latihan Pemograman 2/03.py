def compute_hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range (1, smaller + 1):
        if((x % 1 == 0) and (y % 1 == 0)):
            hcf = i
        return hcf

num1 = 54
num2 = 24

print("Nilai H.C.F adalah", compute_hcf(num1, num2))