def hitung_bmi(berat_badan, tinggi_badan):
    bmi = berat_badan / (tinggi_badan ** 2)
    return bmi

def rekomendasi_bmi(bmi):
    if bmi < 18.5:
        return "berat badan kurang"
    elif 18.5 <= bmi < 24.9:
        return "berat badan normal"
    elif 25 <= bmi < 29.9:
        return "kelebihan berat badan"
    else:
        return "obesitas"

berat_badan = float(input("Masukkan berat badan (kg): ").replace(',', '.'))
tinggi_badan = float(input("Masukkan tinggi badan (m): "))
bmi_hasil = hitung_bmi(berat_badan, tinggi_badan)
kategori_bmi = rekomendasi_bmi(bmi_hasil)
print("Berat badan   : {} kg".format(berat_badan))
print("Tinggi badan  : {} m".format(tinggi_badan))
print("Nilai BMI Anda: {:.2f}".format(bmi_hasil))
print("Kategori BMI  :", kategori_bmi)