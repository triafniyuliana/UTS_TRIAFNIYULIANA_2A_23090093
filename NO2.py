tahun = int(input("Masukkan Tahun: "))

if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
    print(tahun, "merupakan TAHUN KABISAT")
else:
    print(tahun, "bukan merupakan TAHUN KABISAT.")



