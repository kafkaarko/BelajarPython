#percabangan dan ternary operator
"""
Control flow adalah sebuah cara untuk memberi tahu program mengenai instruksi yang harus dijalankan dan di mana harus memulai dan berakhir. Pada materi sebelumnya, Anda telah mempelajari aksi sekuensial. Python akan menjalankan kode Anda berdasarkan deretan instruksi yang dibuat secara sekuensial.
"""
#percabangan
"""
Dalam pemrograman, sebuah kode program dapat berjalan berdasarkan kondisi tertentu. Maknanya, Anda dapat memberikan instruksi berdasarkan "Jika-maka" (if-else).

"Setiap hari, Ibu selalu pergi ke pasar untuk membeli bahan makanan. Ibu selalu mengutamakan untuk membeli daging ayam di pasar. Jika daging ayam tidak tersedia, maka Ibu akan membeli tempe sebagai pengganti, lalu memasaknya."
"""

stok = "daging kambing"

if stok == "daging ayam":
    print("ibu masak ayam")
else:
    print("ibu masak tempe")
"""
Kode di atas merupakan program percabangan. Jika variabel "stok" bernilai "Daging ayam", maka akan mengembalikan string "Ibu membeli dan memasak ayam". Kita bisa asumsikan variabel "ketersediaan" sama seperti ketersediaan bahan makanan dari pasar yang ibu kunjungi. Jika pasar tersebut menyediakan "Daging ayam", variabel tersebut bernilai "Daging ayam".
"""

"""
If
If adalah statement Python yang akan mengecek nilai variabel di dalamnya memenuhi kriteria suatu kondisi atau tidak. Jika memenuhi kriteria, kondisi tersebut bernilai true. Jika tidak memenuhi kriteria, kondisi akan bernilai false. Jika kondisi if bernilai true, kode yang berada dalam blok kode if akan dieksekusi.
"""

nilai = 100

if nilai == 100:
    print("abosolute jenius")

"""
Pada kode di atas, program akan mengecek nilai dari variabel "score". Kondisi yang harus terpenuhi adalah "if score == 100" atau bisa diartikan nilai dari variabel "score" harus bernilai "100". Program lalu mengecek variabel dan mengevaluasi nilainya berdasarkan kondisi yang harus dipenuhi. 

Pada kode di atas, kondisi terpenuhi dan program akan menjalankan kode yang berada dalam if statement. Kode tersebut merupakan fungsi "print()" untuk menampilkan teks atau string "Nilai Anda sempurna!".

Hal lain yang perlu diperhatikan adalah Python menganggap setiap nilai kosong (zero) dan null sebagai False. Sebaliknya, nilai yang tidak kosong (non-zero) dan tidak null (non-null) akan bernilai True. Untuk lebih mengetahui maksudnya, mari lihat kode berikut. 
"""

x = ""

if x:
    print("ini true")   

"""
Pada baris pertama kode program di atas, variabel "x" diinisialisasikan dengan string kosong "". Kemudian if statement mengevaluasi variabel "x" dan menghasilkan nilai salah (False). Hal ini terjadi karena variabel "x" berisi string kosong dan Python mengevaluasinya sebagai False. Sebab hasil kondisinya adalah False, blok kode dalam if tidak dijalankan.

Beberapa nilai yang dianggap sebagai false oleh Python sebagai berikut.

Nilai yang sudah didefinisikan bernilai salah: None dan False.
Angka nol dari semua tipe numerik: 0, 0.0, 0j, Decimal(0), Fraction(0,1).
Urutan (sequence) dan koleksi (collection) yang kosong: "", (), {}, set(), range(0).
"""
#versi one-linear

skor = 100

if skor == 100 : print("abosolute jenius")


"""
Else
Else adalah statement yang menjadi jalan keluar saat kondisi atau hasil evaluasi if statement bernilai false. Maksudnya adalah program akan menjalani blok kode if terlebih dahulu dan jika hasilnya adalah false, program akan menjalankan else statement sebagai jalan keluar atau kondisi terakhir.
"""

tinggi_badan = 140

if tinggi_badan >= 190 :
    print("kamu boleh masuk")
else:
    print("kamu gk boleh masuk kamu masih kecil soalnya")

"""
Pada program di atas, Anda seolah berkata "Jika tinggi badannya adalah 160 cm ke atas, maka diperbolehkan naik roller coaster. Jika di bawah 160 cm, maka pengunjung tidak diperbolehkan menaiki roller coaster".
"""

"""
Elif
Elif merupakan kependekan dari else if dan alternatif untuk if bertingkat atau switch case. Elif statement berada pada posisi setelah if. Anda dapat menambahkan elif statement lebih dari satu karena tidak dibatasi dan opsional.
"""

nilai = 86

if nilai >= 90:
    print("kamu dapat A")
    print('pertahankan')
elif nilai >=70:
    print('kamu dapat B')
    print('tingkatkan lagi')
elif nilai >=60:
    print('kamu dapat C')
    print("harus labih giat belajar lagi")
else:
    print("kamu dapaet D")
    print("waduh kamu gk masih ey")


"""
Program di atas merupakan contoh penerapan if, else, dan elif statement. Kasus yang digunakan adalah penilaian tugas siswa. Jika nilai siswa lebih atau sama dengan dari 90, siswa akan mendapatkan nilai A. Jika nilai siswa lebih atau sama dengan dari 70 dan kurang dari 80, siswa akan mendapatkan nilai B. Jika nilai siswa lebih atau sama dengan dari 60 dan kurang dari 70, siswa akan mendapatkan nilai C. Jika nilai siswa kurang dari 60, siswa akan mendapatkan nilai D.

Pada program di atas, diasumsikan bahwa siswa memiliki nilai 65. Jadi, variabel "nilai" diinisialisasi dengan nilai 65. Program akan mengevaluasi satu persatu secara sekuensial dari if statement pertama hingga else statement.

Kondisi if pertama tidak memenuhi kriteria karena nilai harus lebih dari 80, program lanjut ke elif statement pertama dan tidak memenuhi kriteria karena harus bernilai lebih dari 70. Program berlanjut ke elif statement kedua, hasil evaluasinya ternyata memenuhi kriteria, yakni nilai lebih dari 60. Program mengeksekusi blok kode di dalamnya dengan menampilkan teks "Hmm.. Anda mendapat nilai C Ayo semangat!".

Perlu diingat bahwa else statement tidak akan dijalankan jika kondisi sebelumnya terpenuhi seperti pada kasus di atas.

Untuk informasi tambahan, kita juga dapat menambahkan 'and' atau 'or' operator dalam kondisi percabangan. Contohnya seperti di bawah ini. Asumsikan kita membuat program penilaian tugas siswa, tetapi kita memiliki dua indikator, yaitu nilai dan perilaku.
"""

nilai = 90
sikap = "jelek"

if nilai >= 80 and sikap == "baik":
    print("anda memiliki nilai A,dan anda berperilaku bagus")
    print("pertahankan")
elif nilai >= 80 and sikap != "baik":
    print("anda memeliki nilai A,namun anda badung")
    print("ayo belajar akhalak")
else:
    print("yuk belajar lebih giat")

"""
Pada contoh di atas, kita membuat program penilaian tugas siswa dengan dua indikator, yaitu nilai dan perilaku. Jika siswa memiliki nilai di atas 80, tetapi tidak berkelakuan baik, program akan memunculkan teks "Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik". Begitu pun sebaliknya dan kita bisa menambahkan percabangan lain untuk kondisi setelahnya. 
"""

#Ternary Operator

"""
Ternary operators termasuk conditional expressions pada Python. Conditional expressions adalah bentuk ekspresi yang bertujuan untuk mengevaluasi kondisi dan mengembalikan nilai berdasarkan hasil evaluasinya. Anda bisa asumsikan bahwa ternary operators ini merupakan versi one-liner dari if dan else. 

Ternary operators dibangun dengan menempatkan "blok kode jika benar" pada posisi awal, lalu diikuti oleh "if statement" serta "kondisi"-nya. Kemudian "else statement" ditempatkan di akhir beserta dengan "blok kode jika salah".
"""

lulus = True

print("selamat") if lulus else print("perbaiki")
"""
Kode program di atas menampilkan pesan teks "selamat" jika kondisi bernilai true dan menampilkan pesan teks "perbaiki" jika kondisi bernilai false. Jika kita transformasikan menjadi bentuk blok, berikut adalah kodenya.

Perlu diingat bahwa tujuan dari one-liner bukanlah sekadar untuk memudahkan kode dibaca karena hanya dibuat dalam satu baris, melainkan untuk membuat kode menjadi lebih singkat dan jelas.

Opsi lain dari ternary operators adalah melibatkan tuple.
"""
lulus = False
kelulusan  = ("perbaiki,anda masih belom bisa lulus","selamat anda lulus")[lulus]
print(kelulusan)
#Kode program di atas menampilkan pesan teks "Selamat, Anda lulus!" jika kondisi bernilai true dan menampilkan pesan teks "Perbaiki, Anda belum lulus." jika kondisi bernilai false. Jika kita ubah menjadi blok kode IF, berikut penerapannya.

#Perulangan

#For
"""
For termasuk sintaks dalam Python yang bersifat definite iteration. Definite iteration adalah sebuah proses iterasi atau perulangan ketika jumlah pengulangannya ditentukan secara eksplisit sebelumnya.
"""

var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list :
    print(i)
"""
Kode di atas merupakan program yang bertujuan untuk menampilkan angka dari 1 hingga 10 berdasarkan variable list yang sudah diinisialisasikan sebelumnya. Perhatikan bahwa program di atas sebenarnya sama dengan program pada contoh sebelumnya. Jika contoh sebelumnya menggunakan sintaks "print()" yang berulang, program di atas menggunakan sintaks atau statement for.
"""

for i in range(10):
    print(i)
"""
Jika Anda perhatikan lebih baik, program di atas menampilkan angka dari 0 hingga 9 padahal kita menentukannya "10". Mengapa itu terjadi? Pada dasarnya, "range()" adalah fungsi bawaan dalam Python yang akan menghasilkan urutan bilangan dimulai dari indeks ke-0.
"""

#range(start,stop,step)
"""
Berikut adalah penjelasan detail terkait fungsi "range()".

"Start" merupakan nilai awal dari urutan bilangan yang bersifat opsional, jika Anda tidak memasukkannya, nilai awal akan dianggap 0. 
"Stop" merupakan nilai batas yang wajib dimasukkan. Urutan akan berhenti sebelum mencapai nilai "stop" (eksklusif). 
"Step" merupakan nilai penambahan antara setiap dua bilangan dalam urutan yang bersifat opsional. Jika nilai tersebut tidak diberikan, secara default nilai yang dimasukkan adalah 1.
"""

for i in range(1,10,2):
    print(i)
"""
Pada program di atas, kita menampilkan bilangan ganjil yang dimulai dari 1 hingga 10. Perhatikan bahwa program di atas mendefinisikan nilai "1" sebagai "start", nilai "10" sebagai "stop", dan nilai "2" sebagai "step". Ingat bahwa "stop" bersifat eksklusif, yang artinya nilai terakhirnya tidak akan disertakan. 

Dengan begitu, program di atas akan menampilkan kode dari 1 hingga 10 dengan setiap bilangan ke-2 dan kelipatannya akan dilewati atau tidak dicetak.

"""

#while

"""
While termasuk sintaks dalam Python yang bersifat indefinite iteration. Indefinite iteration adalah sebuah proses iterasi yang akan berhenti ketika memenuhi kondisi tertentu.
"""

counter = 5
while counter >= 1 :
    print(counter)
    counter -= 1

"""
Pada contoh di atas, kita menggunakan perulangan "while" untuk menampilkan angka 1 hingga 5. Variabel "counter" diinisialisasi dengan nilai 1 sebelum perulangan dimulai. Ini artinya perulangan akan dimulai dari 1 berdasarkan nilai variabel tersebut. Perulangan lalu berjalan dengan mengevaluasi variabel "counter" yang memiliki nilai "1". Hasil dari evaluasi tersebut bernilai true sehingga blok kode di dalamnya akan dijalankan.
"""