import fife

persegi_panjang_pertama = fife.mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)
"""
Pertama, kita perlu mengimpor file berisi fungsi yang sebelumnya dibuat dengan cara mendefinisikan "import hello". Ingat bahwa hello adalah nama file kita sebelumnya. Baris kedua dan seterusnya adalah cara yang sama dengan yang telah kita pelajari. Namun, perbedaannya adalah kita memanggil fungsi memakai cara "hello.mencari_luas_persegi_panjang(5,10)" dengan hello adalah nama modul atau file yang telah kita impor.

Sekarang, jalankan file main.py pada terminal Anda. Gunakan kode di bawah ini dan pastikan terminal yang Anda buka sedang berada pada direktori yang sama dengan file yang telah dibuat.
"""
print(fife.nama)
"""
Terlihat pada kode di atas bahwa untuk menampilkan variabel kita tidak menggunakan kurung tutup "()" seperti pada saat pemanggilan fungsi. Namun, kita tetap menggunakan "hello" sebagai modul yang telah kita impor sebelumnya.

Untuk catatan, Anda juga bisa mengimpor variabel atau fungsi secara spesifik dari suatu modul. Dalam contoh di atas, artinya Anda bisa langsung mengimpor fungsi “mencari_luas_persegi_panjang” dan variabel “nama” dari modul hello.
"""
from fife import mencari_luas_persegi_panjang,nama

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

print(nama)
"""
Kode setelah “from” adalah nama modul yang ingin diimpor, sedangkan kode setelah “import” adalah nama fungsi dan variabel yang ingin kita impor.

Sebenarnya, impor tidak hanya terbatas pada fungsi dan variabel, Anda juga bisa mengimpor kelas, method, dan sebagainya.

Terakhir, berikut adalah tampilan ketika kita menjalankan file dengan cara yang disebutkan di atas.
"""