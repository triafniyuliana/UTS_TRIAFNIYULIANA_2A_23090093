jumlah_barang = int(input("Masukkan jumlah barang: "))
total_harga = 0
for i in range(jumlah_barang):
        harga_barang = float(input("Masukkan harga barang ke-{}: ".format(i + 1)))
        total_harga += harga_barang

print("Total harga belanja:", total_harga)