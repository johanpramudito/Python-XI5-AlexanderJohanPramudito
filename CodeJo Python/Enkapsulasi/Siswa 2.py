class Siswa:

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    #decorator
    @property
    def nis(self):
        pass

    #getter
    @nis.getter
    def nis(self):
        return self.__nis

    #setter
    @nis.setter
    def nis(self, newnis):
        self.__nis = newnis
    
johan = Siswa(16354, "Johan Pramudito", "XI MIPA 5")

print(johan.nis)
johan.nis = 12345
print(johan.nis)