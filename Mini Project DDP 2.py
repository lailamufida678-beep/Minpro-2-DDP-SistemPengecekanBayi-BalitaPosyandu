from datetime import datetime
from prettytable import PrettyTable
import pwinput
import os
os.system("cls" if os.name == "nt" else "clear")

akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "user123", "role": "user"},
}

data_anak = {
    1: {"nama": "Budi", "umur": 10, "kondisi": "Sehat", "tanggal": "01/01/24"},
    2: {"nama": "Siti", "umur": 15, "kondisi": "Sakit", "tanggal": "02/01/24"},
    3: {"nama": "Andi", "umur": 8, "kondisi": "Sehat", "tanggal": "03/01/24"},
}
data_hapus = []
data_ubah = []

def login():
    percobaan = 0
    while percobaan < 3:
        print("=== Login Posyandu ===")
        username = input("Masukkan username: ")
        password = pwinput.pwinput("Masukkan password: ")
        if username in akun and akun[username]["password"] == password:
            print(f"Login berhasil. Selamat datang, {username}!")
            return akun[username]["role"]
        else:
            percobaan += 1
            print("Username atau password salah.", "Sisa percobaan:", {3 - percobaan})
    print ("Login gagal 3 kali. Program berhenti.")
    return None
    
def input_data_anak():
    while True:
        nama = input("Masukkan nama anak: ")
        if nama == "":
            print("Nama tidak boleh kosong. Silakan masukkan nama anak.")
            continue
        umur = int(input("Masukkan umur (bulan): "))
        if umur < 0 or umur >59:
            print("Umur harus antara 0 hingga 59 bulan. Silakan masukkan umur yang valid.")
            continue
        kondisi = input("Masukkan kondisi (Sehat/Sakit): ")
        if kondisi not in ["Sehat", "Sakit"]:
            print("Kondisi harus 'Sehat' atau 'Sakit'. Silakan masukkan kondisi yang valid.")
            continue
        return nama, umur, kondisi
    
def tambah_data():
    nama, umur, kondisi = input_data_anak()
    tanggal = datetime.now().strftime("%d/%m/%y")

    if not data_anak:
        nomor = 1
    else:
        nomor = max(data_anak) + 1
    data_anak[nomor] = {"nama": nama, "umur": umur, "kondisi": kondisi, "tanggal": tanggal}
    print("Data berhasil ditambahkan.")

def lihat_data():
    print("=== Data Anak ===")
    if not data_anak:
        print("Belum ada data.")
        return
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Umur", "Kondisi", "Tanggal", "Kategori", "Tindakan"]
    for id_anak, anak in data_anak.items():
        kategori = "Bayi" if anak["umur"] <= 11 else "Balita"
        tindakan = "Diberikan vitamin dan PMT" if anak["kondisi"] == "Sehat" else "Diberikan surat rujukan ke Puskesmas"
        tabel.add_row([id_anak, anak["nama"], anak["umur"], anak["kondisi"], anak["tanggal"], kategori, tindakan])
    print(tabel)

def pilih_id(prompt):
    id_input = input(prompt)
    if not id_input.isdigit():
        print("ID harus berupa angka.")
        return None
    id_anak = int(id_input)
    if id_anak in data_anak:
        return id_anak
    print("ID tidak ditemukan.")
    return None

def ubah_data():
    if not data_anak: return print("Belum ada data.")
    lihat_data()
    id_anak = pilih_id("Masukkan id yang ingin diubah: ")
    if id_anak is None: return
    data_lama = data_anak[id_anak].copy()
    nama, umur, kondisi = input_data_anak()
    data_anak[id_anak] = {"nama": nama, "umur": umur, "kondisi": kondisi, "tanggal": data_lama["tanggal"]}
    data_ubah.append({"id": id_anak, "sebelum": data_lama, "sesudah": data_anak[id_anak]})
    print("Data berhasil diubah.")

def hapus_data():
        if not data_anak:
            print("Belum ada data.")
            return
        lihat_data()
        id_anak = pilih_id("Masukkan id yang ingin dihapus: ")
        if id_anak is None:
            return
        terhapus = data_anak.pop(id_anak)
        data_hapus.append(terhapus)
        print("Data yang dihapus:", terhapus)

def hasil_akhir():
    print("=== Hasil Akhir ===")
    print("Data yang tersisa:", data_anak)
    print("Data yang diubah:", data_ubah)
    print("Data yang dihapus:", data_hapus)
    print("Pendataan selesai.")

def menu_admin():
    while True:
        print("=== Menu Admin ===")
        print("1. Tambah Data Anak")
        print("2. Lihat Data Anak")
        print("3. Ubah Data Anak")
        print("4. Hapus Data Anak")
        print("5. Hasil Akhir")
        print("6. Logout")

        pilihan = input("Masukkan Pilihan: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            lihat_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            hasil_akhir()
        elif pilihan == "6":
            print("Logout berhasil.")
            break

def menu_user():
    while True:
        print("=== Menu User ===")
        print("1. Lihat Data Anak")
        print("2. Hasil Akhir")
        print("3. Logout")

        pilihan = input("Masukkan Pilihan: ")

        if pilihan == "1":
            lihat_data()
        elif pilihan == "2":
            hasil_akhir()
        elif pilihan == "3":
            print("Logout berhasil.")
            print("Terima kasih telah menggunakan program ini.")
            break

role = login()
if role == "admin":
    menu_admin()
elif role == "user":
    menu_user()


