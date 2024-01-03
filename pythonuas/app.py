# Fungsi untuk menghitung rata-rata nilai
def hitung_rata_rata(nilai_python, nilai_web, nilai_cpp):
    return (nilai_python + nilai_web + nilai_cpp) / 3

# Fungsi untuk menentukan apakah mahasiswa layak beasiswa
def layak_beasiswa(nilai_python, nilai_web, nilai_cpp):
    return nilai_python >= 50 and nilai_web >= 50 and nilai_cpp >= 50

# List untuk menyimpan data mahasiswa
daftar_mahasiswa = []

# Input data mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah_mahasiswa):
    nim = int(input("Masukkan NIM mahasiswa: "))
    nama = input("Masukkan nama mahasiswa: ")
    nilai_python = int(input("Masukkan nilai Pemrograman Python: "))
    nilai_web = int(input("Masukkan nilai Pemrograman Web: "))
    nilai_cpp = int(input("Masukkan nilai Pemrograman C++: "))

    # Menambahkan data mahasiswa ke list
    daftar_mahasiswa.append((nim, nama, nilai_python, nilai_web, nilai_cpp))

# Menyaring mahasiswa yang layak beasiswa
mahasiswa_layak = [(nim, nama, hitung_rata_rata(np, nw, nc)) for nim, nama, np, nw, nc in daftar_mahasiswa if layak_beasiswa(np, nw, nc)]

# Mengurutkan mahasiswa berdasarkan nilai rata-rata
mahasiswa_layak.sort(key=lambda x: x[2], reverse=True)

# Menampilkan peringkat 1 - 3 mahasiswa yang layak beasiswa
print("\nPeringkat 1 - 3 Mahasiswa yang Layak Beasiswa:")
for i, (nim, nama, rata_rata) in enumerate(mahasiswa_layak[:3]):
    print(f"{i + 1}. NIM: {nim}, Nama: {nama}, Rata-rata: {rata_rata}")
