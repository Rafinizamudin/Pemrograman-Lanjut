# Nama: Rafi Nizamudin
# NIM: 41823010088
# Matkul: Pemograman Lanjut

print("Selamat datang di Aplikasi perhitungan nilai Mahasiswa")
Tugas = float(input("Silahkan Masukan Nilai Tugas Anda: "))
UTS = float(input("Silahkan Masukan Nilai UTS Anda: "))
UAS = float(input("Silahkan Masukan Nilai UAS Anda: "))

a = Tugas * 0.25
b = UTS * 0.35
c = UAS * 0.4
NA = a + b + c

print("Nilai Akhir Anda: ", NA)

if NA > 85:
  print("Dalam Huruf: A")
elif NA > 80:
  print("Dalam Huruf: A-")
elif NA > 75:
  print("Dalam Huruf: B+")
elif NA > 70:
  print("Dalam Huruf: B")
elif NA > 65:
  print("Dalam Huruf: B-")
elif NA > 60:
  print("Dalam Huruf: C+")
elif NA > 55:
  print("Dalam Huruf: C")
elif NA > 50:
  print("Dalam Huruf: C-")
elif NA > 30:
  print("Dalam Huruf: D")
elif NA <= 30:
  print("Dalam Huruf: E")

