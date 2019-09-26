# mendefinisikan kelas induk pertama
class SD(object):
    def __init__(self, a):
        self.a = a
    def cetakA(self):
        print("SD\t: ", self.a)

# mendefinisikan kelas induk kedua
class SMP(object):
    def __init__(self, b):
        self.b = b
    def cetakB(self):
        print("SMP\t: ", self.b)

# mendefinisikan kelas turunan
class SMK(SD, SMP):
    def __init__(self, a, b, c):
        # memanggil SD.__init__()
        SD.__init__(self, a)
        # memanggil SMP.__init__()
        SMP.__init__(self, b)
        self.c = c
    def cetakC(self):
        print("SMK\t: ", self.c)

def main():
    print("Tahun Lulus di : ")
    # membuat objek dari kelas Anak
    obj = SMK(2012, 2015, 2018)
    
    # memanggil metode kelas induk pertama dari obj
    obj.cetakA()

    # memanggil metode kelas induk kedua dari obj
    obj.cetakB()

    # memanggil metode kelas Anak
    obj.cetakC()

if __name__ == "__main__":
    main()
