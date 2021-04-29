class Siswa:
    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    #getter
    def getnis(self):
        return self.__nis

    #setter
    def setnis(self, newnis):
        self.__nis = newnis

johan = Siswa(17428, "Johan Pramudito", "XI MIPA 5")

print(johan.getnis())
johan.setnis(20000)
print(johan.getnis())