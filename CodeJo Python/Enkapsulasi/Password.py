class PasswordManager:
    def __init__(self, username, password):
        self.__username = username
        self.__password = [password]

    def getuser(self):
        return self.__username

    def getpass(self):
        return self.__password

    def setpass(self, newpass):
        if newpass in self.__password:
            print("Masukkan password lain")
        else:
            self.__password = newpass
            print("Perubahan Password berhasil dilakukan")

    def yespass(self, passwo):
        if passwo in self.__password:
            return "Benar"
        else:
            return "Salah"

Facebook = PasswordManager("johancemiwiw", "HAH4HaH4")
Instagram = PasswordManager("lahinisijohan", "C1eci3Cie")
Twitter = PasswordManager("jowwwww", "apahayo0")

print(Facebook.getuser())
print(Instagram.getpass())
print(Twitter.setpass("apahay00"))
print(Instagram.yespass("C1eci3Cie"))