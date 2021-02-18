def bil_prim(x,y):
    for bil in range(x,y):
        prima = True
        if bil > 1:
            for j in range (2,bil):
                if (bil%j==0):
                    break
            else:
                print(bil)

print("Bilangan prima antara 1 dan 100 : ")
bil_prim(1,100)