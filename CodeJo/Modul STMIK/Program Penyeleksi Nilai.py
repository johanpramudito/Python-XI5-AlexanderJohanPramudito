num = int(input("Masukkan nilai : "))

if 0 <= num < 45:
    print("Kriteria E")
elif 45 <= num < 60:
    print("Kriteria D")
elif 60 <= num < 77:
    print("Kriteria C")
elif 77 <= num < 88:
    print("Kriteria B")
elif 88 <= num <= 100:
    print("Kriteria A")
else:
    print("Nilai minimal 0 dan maksimal 100")