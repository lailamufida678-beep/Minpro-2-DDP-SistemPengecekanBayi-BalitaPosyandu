# Minpro-2-DDP-SistemPengecekanBayi-BalitaPosyandu

Nama: Laila Mufida
NIM: 2609116046
Kelas: B 2026

Berikut merupakan Code program dengan judul "Sistem Pengecekan Bayi/Balita Posyandu"
<img width="959" height="539" alt="Screenshot 2026-10-06 164423" src="https://github.com/user-attachments/assets/0d5a1c10-d9b8-41c5-be37-9f88a8d0002e" />
<img width="959" height="536" alt="Screenshot 2026-10-06 164438" src="https://github.com/user-attachments/assets/4ea8d30d-c24f-4b6b-b491-4d2ff8af0ba6" />
<img width="959" height="539" alt="Screenshot 2026-10-06 164456" src="https://github.com/user-attachments/assets/858b1648-e51d-4d67-a0c3-d92ab0b7f4c5" />
<img width="959" height="539" alt="Screenshot 2026-10-06 164611" src="https://github.com/user-attachments/assets/1a96cd9d-4ca4-4ffa-ac25-ac3c0e71d357" />
<img width="959" height="538" alt="Screenshot 2026-10-06 164621" src="https://github.com/user-attachments/assets/052389dc-6f42-4598-bd3f-bec8d90fc6d7" />
<img width="959" height="539" alt="Screenshot 2026-10-06 164643" src="https://github.com/user-attachments/assets/2bf87af3-0fa2-416f-b95d-bad20232135a" />


Deskripsi dan penjelasan singkat program:
Program ini adalah aplikasi manajemen kesehatan anak di posyandu menggunakan python. Program ini dirancang dengan sistem multi-role (admin dan user) serta dilengkapi fitur CRUD lengkap untuk mengelola informasi data anak.
1. Dictionary (akun, data_anak): Digunakan sebagai penyimpan data terstruktur (database sementara).
2. Library PrettyTable: Berfungsi untuk menampilkan data anak dalam bentuk tabel yang rapi, dan mudah dibaca.
3. Library pwinput: Digunakan untuk menyembunyikan karakter password saat mengetik (***) demi keamanan data pengguna.
4. Login System: Membatasi akses program maksimal hingga 3 kali percobaan menggunakan perulangan while.
5. Role Admin: Memiliki hak akses CRUD penuh, yaitu menambah, melihat, mengubah, menghapus, dan melihat riwayat perubahan data.
6. Role user: Hanya memiliki hak akses terbatas, yaitu melihat tabel data anak dan melihat hasil akhir.
7. Tambah & Ubah data: menyimpan data baru dengan tanggal otomatis via datetime
8. Lihat (lihat_data): Menampilkan data rapi berbentuk tabel lewat PrettyTable, serta otomatis menentukan kategori bayi/balida dan tindakan medis
9. Ubah & Hapus (ubah_data, hapus_data): Memperbarui atau menghapus data berdasarkan ID anak yang dipilih
10. Log hasil akhir: Menampilkan rangkuman data tersisa serta riwayat data yang pernah diubah dan dihapus.


Berikut merupakan output yang dihasilkan dari program tersebut:
<img width="959" height="539" alt="Screenshot 2026-10-06 170311" src="https://github.com/user-attachments/assets/02442736-4949-4ea6-9c49-fa5e63e5e456" />
<img width="959" height="525" alt="Screenshot 2026-10-06 170328" src="https://github.com/user-attachments/assets/f7528bf0-7eca-4b93-ba7c-8a402861267e" />
<img width="959" height="529" alt="Screenshot 2026-10-06 170340" src="https://github.com/user-attachments/assets/d2a3b4bc-c649-4438-8bad-265be4a8913f" />
<img width="959" height="539" alt="Screenshot 2026-10-06 170413" src="https://github.com/user-attachments/assets/00418e08-9270-4973-b7f7-c549ae1484ce" />
<img width="956" height="527" alt="Screenshot 2026-10-06 170427" src="https://github.com/user-attachments/assets/87eddd10-0719-45bd-b092-dc45bf38aef4" />


Berikut Merupakan Flowchart yang saya buat untuk melengkapi ketentuan tugas yang diberikan:
<img width="4228" height="4840" alt="image" src="https://github.com/user-attachments/assets/27083c2e-223a-4d5c-9e28-1451d1346e38" />
Penjelasan alur program:
1. Program dimulai (Start), lalu pengguna memasukkan username dan password
2. Program mengecek apakah login benar. Kalau salah, program akan mengecek apakah sudah salah 3 kali.Kalau belum, pengguna diminta mengisi lagi, kalau salah 3 kali program akan berakhir/berhenti.
3. Kalau login benar, program akan mengecek role. Admin dan user sama sama masuk ke menu (1-5). Diamond biru (ubah dan hapus) hanya untuk admin.
4. Program mengecek pilihan menu dari pilihan 1-5.
5. 1. Tambah data: Pengguna mengisi nama, umur, dan kondisi, lalu program mengecek apakah inputnya valid. Kalau tidak valid, pengguna mengisi ulang. Kalau valid, data disimpan ke data_anak, lalu kembali ke menu.
   2. Lihat data: Program mengambil data_anak, lalu mengecek umur. umur 11 bulan atau kurang masuk kategori bayi, di atas itu balita. selanjutnya, program akan mengecek kondisi, setelah itu tabel anak ditampilkan, lalu kembali ke menu.
   3. Ubah data (admin): Program menampilkan tabel anak, pengguna memasukkan ID, lalu program mengecek ID itu ada atau tidak. Lalu pengguna mengisi data baru, data lama disimpan ke data_ubah, dan program kembali ke menu.
   4. Hapus data (admin): Program menampilkan tabel anak, pengguna memasukkan ID, dan program mengecek ID-nya. Data yang dihapus disimpan ke data_hapus, lalu program kembali ke menu.
   5. Selesai. Program menampilkan hasil akhir.










