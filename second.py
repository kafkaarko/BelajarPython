#ekspresi
"""
penerapan ekspresi
"""

x = 10
y = 11

result = x + y
results = x - y

print(result)
print(results)

#dan ini adalah salah satu contohnya

angka = [2,3,4,5]
huruf = ['p','y','t','h','o','n']
gabung = angka + huruf
print(gabung)

"""
Pada kode di atas, Anda menggabungkan dua list dengan menggunakan operator penjumlahan (+). Namun, pada kode di bawah ini, Anda mereplikasi list dengan menggunakan operator perkalian (*).
"""
huruf = ['p','y','t','h','o','n']

klon = huruf * 2
print(klon)
 
#jenis jenis Ekspresi

"""
Jenis	Contoh
Biner

(x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), (x % y), (x == y), (x != y).

Uner

(x += 1), (x-=1), (not x).
"""

#penerapan biner dan uner

a = True
a = not a 
print(a)

b = 6
b -= 1
print(b)

c = 6 
c += 1
print(c)

d = 10
print(-d)

"""
Mari kita bedah satu persatu kode di atas.

Variabel a bernilai True, jika kita memberikan ekspresi "not a" yang artinya "not True", hasil yang didapat adalah False. 
Baik increment maupun decrement, keduanya adalah pola yang sama untuk menambahkan dan mengurangi suatu variabel dengan jumlah tetap.
a += 1 memiliki tujuan yang sama dengan struktur a = a + 1. Jika diasumsikan variabel a bernilai 1, seolah-olah kita melakukan operasi penjumlahan "1+1". Inilah alasan ia disebut dengan increment yang artinya kenaikan.
Decrement dapat dijelaskan sebagai a -=1, memiliki tujuan yang sama dengan struktur a = a - 1. Jika diasumsikan variabel a bernilai 1, seolah-olah kita melakukan operasi pengurangan "1-1".
Penjelasan lebih detail mengenai operator akan kita bahas pada materi selanjutnya. Saat ini mari kita lanjut membahas ekspresi menurut tipe data yang dihasilkan.
"""

"""
Ekspresi Menurut Tipe Data yang Dihasilkan

Jenis	Contoh
Ekspresi aritmetika: 

<numerik> <operator> <numerik> = <numerik>

2 + 2 = 4, 2 - 2 = 0

Ekspresi relasional: 

<numerik> <operator> <numerik> = <boolean>

3 < 10 = True, 1 > 10 = False

Ekspresi logika: 

<boolean> <operator> <boolean> = <boolean>

True or False = True
"""

#contoh

print (1 + 1)
print(4<10)
print(True or False)

"""
Pada kode di atas, kita melakukan operasi dengan melibatkan ekspresi aritmetika, ekspresi relasional, dan ekspresi logika. Pada ekspresi aritmetika, "2+2" menghasilkan nilai "4". Pada ekspresi relasional, "3<10" menghasilkan nilai True; tentu kita tahu bahwa tiga termasuk bilangan yang kurang dari sepuluh. Pada ekspresi logika "True or False" menghasilkan nilai True, ini merupakan gerbang logika pada dunia pemrograman. Anda akan mempelajari lebih detail pada materi operator logika.
"""

#jenis jenis operator

"""
Operator Aritmetika

Asumsikan x bernilai 11 dan y bernilai 5. 

Operator	Deskripsi	Contoh
Penjumlahan (+)

Menambahkan nilai dari kedua operan.

x + y = 16

Pengurangan (-)

Mengurangi nilai dari kedua operan.

x - y = 6

Perkalian (*)

Mengalikan nilai dari kedua operan.

x * y = 55

Pembagian Bulat (//)

Membagi nilai dari kedua operan. Jika operan adalah integer, hasil operasi adalah bilangan bulat.

x // y = 2

Pembagian Riil (/)

Membagi nilai dari kedua operan. Jika operan adalah float, hasil operasi adalah bilangan riil.

x / y = 2.2

Modulo (%)

Sisa hasil pembagian nilai dari dua operan.

x % y = 1

Pangkat (**)

Memangkatkan nilai dari dua operan.

x ** y = 161051
"""

x = 11
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x ** y)

"""
Pada kode di atas, Anda telah menerapkan seluruh operasi menggunakan operator aritmetika. Jika kita lihat lebih detail, seluruh output tersebut memiliki hasil yang sama dengan tabel sebelumnya.
"""

#operator Relasional

"""
 Asumsikan kedua variabel bertipe numerik atau float dengan x bernilai 5 dan y bernilai 10. 

 Operator	Deskripsi	Contoh
Sama dengan (==)

Menghasilkan True, jika kedua operan bernilai sama.

x == y, menghasilkan False. 

Tidak Sama dengan (!=)

Menghasilkan True, jika kedua operan tidak bernilai sama.

x != y, menghasilkan True.

Lebih Besar dari (>)

Menghasilkan True, jika operan kiri lebih besar dari operan kanan.

x > y, menghasilkan False.

Kurang dari (<)

Menghasilkan True, jika operan kanan lebih besar dari operan kiri.

x < y, menghasilkan True.

Lebih Besar dari Sama dengan (>=)

Menghasilkan True, jika operan kiri lebih besar atau sama dengan operan kanan.

x >= y, menghasilkan False.

Kurang dari Sama dengan (<=)

Menghasilkan True, jika operan kanan lebih besar atau sama dengan operan kiri.

x <= y, menghasilkan True.
"""

x = 11
y = 5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

"""
Pada kode di atas, Anda telah menerapkan seluruh operasi menggunakan operator relasional. Jika kita lihat lebih detail, seluruh output tersebut memiliki hasil yang sama dengan tabel sebelumnya. Sebagaimana telah dijelaskan sebelumnya, operator relasional dapat menggunakan operan bertipe integer, string, ataupun float. Kode di atas telah menggunakan operan bertipe integer, Anda juga bisa mengubahnya dengan operan bertipe float. 

Namun, berbeda halnya dengan operan bertipe string. Anda dapat melihat tabel di bawah untuk contoh penerapannya. Asumsikan x bernilai "Dicoding" dan y bernilai "Indonesia".
"""
x = "Indonesia"
y = 'Dicoding'

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

"""
Perhatikan kode di atas, string "Dicoding" dan "Indonesia" tidak sama sehingga sintaks operator sama dengan "==" menghasilkan nilai False, sedangkan operator tidak sama dengan "!=" menghasilkan nilai True. Operator sisanya akan membandingkan huruf D pada string "Dicoding" dan huruf I pada string "Indonesia". Anda bisa mencoba mengganti huruf pertama tersebut untuk memahami lebih detail.
"""

#Operator Logika

"""
asumsikan bahwa p bernilai True dan q bernilai False.

Operator	Deskripsi	Contoh
"AND" atau "&"

Logika yang hanya menghasilkan True jika kedua operan bernilai True.

p and q = False, p & q = False

"OR" atau "|"

Logika yang menghasilkan True jika salah satu dari kedua operan bernilai True.

p or q = True, p | q = True

NOT

Logika yang bertujuan untuk membalikkan nilai logika dari operannya.

not q = True
"""

#penerapan
#and,&
print(True and True)
print(True and False)
print(False and True)
print(False and False)

"""
Pada kode di atas, Anda menerapkan seluruh contoh yang ada pada tabel sebelumnya menjadi program Python. Dapat dilihat bahwa hanya jika kedua operan bernilai True yang menghasilkan nilai True.
"""

#or |

print(True or True)
print(True or False)
print(False or True)
print(False or False)

#Pada kode di atas, Anda menerapkan seluruh contoh yang ada pada tabel sebelumnya menjadi program Python. Dapat dilihat bahwa jika salah satu atau kedua operan bernilai True, hasil akhirnya bernilai True.

#not

print(not True)
print(not False)

"""
Pada kode di atas, Anda menerapkan seluruh contoh yang ada pada tabel sebelumnya menjadi program Python. Dapat dilihat bahwa jika operan bernilai True, hasilnya False dan sebaliknya.
"""

#Operator Assignment

"""
 Asumsikan x bernilai 11 dan y bernilai 5.

 Operator	Deskripsi	Contoh
+=

Menyederhanakan operasi x = x + y.

x += y, menghasilkan nilai 16.

-=

Menyederhanakan operasi x = x - y.

x -= y, menghasilkan nilai 6.

*=

Menyederhanakan operasi x = x * y.

x *= y, menghasilkan nilai 55.

/=

Menyederhanakan operasi x = x / y.

x /= y, menghasilkan nilai 2.2.

%= 

Menyederhanakan operasi x = x % y.

x %= y, menghasilkan nilai 1.


"""

# +=
x = 11
x += 5
print(x)

# -=
x = 11
x -= 5
print(x)

# /=
x = 11
x /= 5
print(x)

# %=
x = 11
x %= 5
print(x)

#Dalam kode di atas, Anda menerapkan seluruh contoh yang ada pada tabel sebelumnya menjadi program Python. Masih bingung? Mari lihat salah satu kode di atas dan bedah lebih dalam.

x = 11
x += 5
print(x)

x = 11
x = x + 5
print(x)

"""
Kode "x += 5" setara dengan "x = x + 5". Asumsikan x bernilai 11, hasil yang didapat dari kedua kode di atas adalah 16. Seolah-olah Anda melakukan operasi seperti berikut: "x = 11 + 5".   
"""


#Aksi Sekuensial

"""
Dalam bahasa pemrograman Python, program yang Anda buat akan dijalankan secara sekuensial. Apa maksudnya? Kode yang Anda bangun akan berjalan sesuai dengan urutan perintahnya. Aksi sekuensial sendiri memiliki makna sebagai sederetan instruksi yang akan dijalankan oleh komputer berdasarkan urutan penulisannya.
"""

#contoh

print("selamat datang di dalam program python!\n")
print("silahkan masukan data diri anda")
nama = input("masukan nama anda:")
tahun_lahir = input("masukan taun lahir anda:")
umur = 2024 - int(tahun_lahir)

print(f'selamat datang {nama} dalam program python ,per 2024 umur anda adalah {umur} tahun\n')
print("terima kasih telah menggunakan py")
"""
Untuk memaksimalkan contoh implementasi, silakan salin kode di atas dan jalankan menggunakan notebook atau IDE Anda. Mari bedah kode tersebut.

Komputer akan menjalankan kode pertama dengan menampilkan teks "Selamat datang dalam Program Python".
Setelah berhasil, kode kedua akan dijalankan dengan menampilkan teks "Silakan masukkan data diri Anda."
Lalu, kode ketiga akan dijalankan. Program akan meminta Anda memasukkan nama sembari memunculkan teks "Masukkan nama Anda: ". Input ini akan disimpan pada variabel bernama "nama".
Kemudian, kode keempat akan dijalankan. Program akan meminta Anda memasukkan tahun lahir sembari memunculkan teks "Masukkan tahun lahir Anda: ". Input ini akan disimpan pada variabel bernama tahun_lahir.
Setelah itu, variabel tahun_lahir akan dikalkulasikan untuk mengetahui umur Anda per tahun 2023. Hasil kalkulasi tersebut disimpan pada variabel umur.
Program akan memunculkan teks "Selamat datang {nama} dalam program Python, per 2023 umur Anda adalah {umur} tahun." Dengan {nama} dan {umur} merupakan nilai dari variabel dengan nama yang sama.
Program ditutup dengan memunculkan teks "Terima kasih telah menggunakan program Python!".
Keseluruhan kode tersebut menggambarkan bahwa program akan dijalankan berdasarkan urutan perintahnya. Perlu diperhatikan bahwa terdapat program yang akan berubah hasilnya jika urutan baris instruksinya diubah. Ada juga program yang hasilnya TIDAK akan berubah jika urutan baris instruksinya diubah.

Mari kita pahami satu per satu. Simak kode di bawah ini untuk melihat contoh jika urutan baris diubah, TIDAK mengubah hasil eksekusi.
"""

#Python Interpreter
"""
Kode dari program Python yang Anda bangun akan ditransformasi menjadi kode yang mudah dimengerti oleh mesin menggunakan program compiler atau interpreter. Compiler merupakan program yang akan menerjemahkan bahasa pemrograman menjadi bahasa mesin sebelum dijalankan dan menghasilkan output. Ini artinya program yang Anda bangun secara keseluruhan akan diubah terlebih dahulu semuanya menjadi bahasa mesin. 

Hal berbeda terjadi pada interpreter, yang akan menerjemahkan bahasa Python satu per satu dan menghasilkan output secara langsung. Hal ini memungkinkan Anda untuk melihat hasil program segera setelah satu baris kode dieksekusi hingga selesai. Implementasi interpreter ada pada mode interaktif Python. Anda dapat menjalankan satu atau dua lebih baris kode secara langsung dan melihat hasilnya.
"""

#block code
"""
Sebuah program Python dapat berupa pernyataan atau statement, bisa juga terdiri atas blok kode. Sebuah blok merujuk pada potongan kode program Python yang dijalankan sebagai satu unit. Kode blok dapat berupa modul, fungsi, kelas, control flow, dan sebagainya. Tenang! Anda akan mempelajari istilah-istilah tadi lebih dalam pada materi-materi selanjutnya.
"""

for i in range(10):
    print(i)

"""
Kode di atas merupakan satu unit kode blok perulangan yang akan mencetak angka 0 hingga 9. Perhatikan bahwa kode perulangan di atas juga melakukan aksi sekuensial, yakni setiap kode akan dijalankan lalu diulangi hingga kondisi akhir terpenuhi.

Mengapa memahami kode blok penting? Alasannya adalah Anda harus membuat kode yang mudah dimengerti oleh Anda dan orang lain sebagai seorang programmer. Selain itu, kode blok yang baik dan benar akan memudahkan interpreter atau compiler untuk berjalan dengan baik dan tidak menghasilkan error. 
"""

# for i in range(10):
# print(i)
"""
Kode blok di atas merupakan program yang sama dengan sebelumnya. Perbedaannya terletak pada indentasi kode blok tersebut. Program akan menghasilkan error karena interpreter akan menganggap bahwa kode "print(i)" merupakan bagian dari kode blok "for i in range(10)". Error dihasilkan karena harusnya terdapat indentasi (biasanya berupa empat spasi) sebelum kode "print(i)".
"""

#case sensitive

Teks = "indonesia"
teks = "bestfriend"

print(Teks)
print(teks)
"""
Pada program di atas, Anda membuat dua variabel dengan nama "teks" dan "Teks". Python akan menganggap bahwa variabel tersebut berbeda, walaupun bagi kita sebagai manusia, mereka memiliki arti yang sama.

Bahkan jika Anda menambahkan sintaks "print()" untuk menampilkan variabel "TEks" seperti di bawah ini. Hasilnya akan menampilkan pesan Error.
"""
# print(TEks)
#Hal ini disebabkan variabel "teks", "Teks", dan "TEks" dianggap sebagai variabel yang berbeda oleh Python.

#one-liner
"""
One-liner merupakan gaya penulisan pada Python yang memungkinkan Anda untuk membuat sebuah kode hanya dalam satu baris. One-liner adalah salah satu keunggulan dalam Python yang susah untuk diimplementasikan bagi beberapa bahasa pemrograman lainnya.
"""
x = 1
y = 2

temp = x
x = y
y = temp

print("setelah pertukaran:")
print("x = ", x)
print("y = ", y)
"""
Mari bedah kode tersebut.

Anda menginisialisasi variabel x dengan nilai 1 dan variabel y dengan nilai 2. 
Anda menginisialisasi variabel temp dengan nilainya adalah variabel x. Hal ini menyebabkan variabel temp memiliki nilai 1.
Anda menginisialisasi variabel x dengan nilai baru, yakni variabel y. Hal ini menyebabkan nilai dari variabel x menjadi 2.
Anda menginisialisasi variabel y dengan nilai baru, yakni variabel temp. Hal ini menyebabkan nilai dari variabel y menjadi 1.
Proses penukaran variabel telah selesai. Selanjutnya, Anda menampilkan nilai pada variabel tersebut dengan sintaks "print()".

Phew, cukup memakan tenaga, ya. Namun, tahukah Anda kalau ada kode one-liner yang dapat memudahkan Anda untuk melakukan operasi menukar dua variabel ini? Berikut adalah kodenya.
"""

x = 1
y = 2

x,y = y,x

print("setelah pertukaran:")
print("x = ", x)
print("y = ", y)