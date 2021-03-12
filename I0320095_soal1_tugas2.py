
#menghitung luas persegi panjang
panjang = float(input("masukkan nilai panjang"))
lebar = float(input("masukkan nilai lebar"))
luas_persegipanjang = panjang * lebar
print("panjang = ", panjang)
print("lebar = ", lebar)
print("luas persegi panjang = ", luas_persegipanjang)

#menghitung luas lingkaran
r = float(input("Masukan nilai jari-jari"))
luas_lingkaran = 3,14*(r ** 2)
print("r= ", r)
print("luas lingkaran = ", luas_lingkaran)

#menghitung luas kubus
s = float(input("Masukan nilai panjang sisi"))
luas_permukaan_kubus = 6 * (s ** 2)
print("s = ", s)
print("luas permukaan kubus = ", luas_permukaan_kubus)

#menghitung koversi suhu celcius ke farenheit
C = float(input("Masukkan suhu celcius"))
F = ((9/5) * C) + 32
print("Hasil konversi", C, "celcius =", F, "farenheit")

#menghitung konversi suhu reamur ke kelvin
R = float(input("Masukkan suhu reamur"))
K = ((5/4) * R) + 273
print("Hasil konversi", R, "reamur =", K, "kelvin")
