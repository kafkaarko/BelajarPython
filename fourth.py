"""
Fundamental Array
Python tidak memiliki tipe data array yang sering digunakan dalam bahasa pemrograman lain. Sebaliknya, Python memiliki tipe data list yang dapat dikatakan mirip, tetapi tak sama dengan array. 

Perbedaan yang menonjol adalah cara array menyimpan nilai sangat berbeda dengan list. Pada array, nilai di dalamnya harus memiliki tipe data yang sama. Namun, pada list, nilai di dalamnya tidak harus memiliki tipe data yang sama.

kode python = [1 , "dicoding" , True , 1.0]

kode java int[]   myArray = {1,2,3,4,5}

Perlu diketahui oleh Anda, array bukan hanya sebuah tipe data, melainkan salah satu tipe struktur data berjenis linear. Array merupakan kata dalam bahasa Inggris yang jika diterjemahkan ke bahasa Indonesia memiliki arti "sebuah kelompok besar yang terdiri dari beberapa hal atau orang". Arti ini mirip dengan array atau tipe data list dalam Python, sebuah kelompok besar yang terdiri dari beberapa nilai atau data. Lalu, apa arti dari struktur data itu sendiri?

Struktur data adalah cara untuk mengatur dan menyimpan data sehingga data-data tersebut dapat diakses dan bekerja secara efisien. Dengan adanya struktur data, setiap data yang disimpan memiliki hubungan satu sama lain dan kita dapat beroperasi dengan setiap data tersebut.

Ketika mempelajari materi tipe data pada modul "Berinteraksi dengan Data", sebenarnya Anda telah mempelajari struktur data yang beragam jenisnya. Baik tipe data primitif maupun tipe data collection yang telah dibahas sebelumnya termasuk jenis struktur data Python.

Dari sini, kita harus bisa menyamakan persepsi bahwa array dan list merupakan hal yang berbeda dalam Python. Kendati demikian, Anda bisa menggunakan list sebagai array dalam Python.
"""
x = [1,2,3,4,5]
print(x)
"""
Jika Anda benar-benar ingin menggunakan array, Anda pun bisa mendeklarasikan array dalam Python dengan menggunakan library atau modul Python. Salah satunya modul bernama "array". 

Library merupakan sekumpulan kode yang telah dibuat oleh developer atau programmer dan disediakan kepada pengguna lain agar dapat digunakan ulang dalam pengembangan program atau perangkat lunak. Adapun modul merupakan file yang berisikan kode Python dan dapat digunakan kembali oleh programmer lainnya. Anda akan mempelajari library dan modul pada Python lebih jauh nanti. 
"""
import array

x = array.array("i",[1,2,3,4,5,6])
print(x)
print(type(x))

"""
Pada kode di atas, kita melakukan impor module array dengan memberikan sintaks "import array". Dengan mengimpor module, sekarang kita mempunyai beragam kode baru yang dapat digunakan. Contohnya fungsi "array()" yang digunakan untuk membuat array. 

Pada contoh di atas, kita membuat array bertipe integer dengan menyatakan "i" sebelum array. Sekarang, coba Anda ubah nilai array "[1, 2, 3, 4, 5]" menjadi "[1, 2, 3, 4, 5, 'Dicoding']". Apa yang terjadi? Jika yang terjadi adalah error, hal ini disebabkan karena nilai atau elemen dalam array harus bertipe sama atau identik.

Struktur data linear adalah jenis struktur data yang elemen-elemen nilai di dalamnya disusun secara berurutan atau linear. Sebaliknya, struktur data non-linear merupakan jenis struktur data yang elemen-elemen nilai di dalamnya tidak disusun secara linear.

Array adalah salah satu jenis dari struktur data linear. Dalam konteks ini, array terdiri dari kumpulan elemen bertipe data sama dengan indeks yang berurutan atau linear.

Mari lihat salah satu contoh kasus saat kita perlu menggunakan array sebagai solusi yang terbaik.

"Selepas berakhirnya semester genap, para guru dari SMA Dicoding perlu merekap semua nilai ujian akhir semester. Salah satunya adalah guru matematika, guru tersebut perlu merekap nilai dari seluruh siswa yang ada di kelas IPA 1. Guru tersebut membuat program menggunakan Python untuk mempermudah proses rekap nilai."

"""

nama_siswa1 = 90
nama_siswa2 = 100
nama_siswa3 = 50
nama_siswa4 = 80
nama_siswa5 = 85
nama_siswa6 = 45
nama_siswa7 = 80
nama_siswa8 = 75
nama_siswa9 = 50
nama_siswa10 = 60

print(nama_siswa1)
print(nama_siswa2)
print(nama_siswa3)
print(nama_siswa4)
print(nama_siswa5)
print(nama_siswa6)
print(nama_siswa7)
print(nama_siswa8)
print(nama_siswa9)
print(nama_siswa10)

"""
Pada kode di atas, program yang dibuat adalah menyimpan 10 nilai dengan menggunakan 10 variabel yang berbeda. Variabel pertama dimulai dengan "nama_siswa1" dengan nilai siswanya adalah 90. Variabel kedua berlanjut dengan konsep yang sama hingga selesai. 

Namun, Anda mungkin menyadari bahwa membuat program dengan cara tersebut tidak efektif dan membuat kodenya sulit dibaca. Bahkan ini baru 10 nama siswa, bagaimana dengan 100 siswa? 1000 siswa?

Mari lihat peran list dalam kasus ini.
"""
siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]

print(siswa)
print(siswa[0])
"""
Pada kode di atas, alih-alih membuat inisialisasi variabel yang berulang, Anda dapat membuat list untuk menyimpan seluruh nilai tersebut. Jika Anda ingin mendapatkan nilai pertama atau nilai tertentu, cukup lakukan indexing. Pada contoh di atas, kita menggunakan indexing untuk mengakses elemen pertama atau indeks 0.
"""

"""
Implementasi Array dengan Python
Dalam materi ini, Anda akan mempelajari bentuk-bentuk penerapan Array dengan Python. Pertama, kita akan membahas deklarasi array. Kedua, kita akan membahas cara mengakses elemen array.

Mendeklarasikan Array
Pada materi sebelumnya, sudah disebutkan bahwa dalam Python kita dapat mendeklarasikan array menggunakan dua cara. Pertama dengan memanfaatkan list dan kedua menggunakan library Python.

Perlu Anda ingat, setiap elemen yang ada pada list sebetulnya disimpan pada satu memori. Jika list adalah "[1, 2, 3]", sebetulnya Anda memerintahkan memori komputer untuk menyimpan integer "1" ke dalam satu tempat memori, begitu pun integer "2" akan disimpan dalam satu tempat memori, dan seterusnya.

Perhatikan kode di bawah ini.
"""

var_list = [1,2,3]

for elemen in var_list:
    print(id(elemen))
"""
Ketika Anda menjalankan kode di atas, ia akan menghasilkan lokasi memori setiap elemen yang berada pada list. Lokasi tersebut bisa berubah jika Anda menjalankan ulang program, tetapi perhatikan bahwa semua elemen tersebut memiliki ID lokasi penyimpanan yang berbeda.

Sekarang mari lebih detailkan cara deklarasi array dalam Python menggunakan list. Ada dua cara untuk melakukan deklarasi array menggunakan list, yakni berikut.

Mendefinisikan Isi Array
Cara pertama adalah dengan mendeklarasikan variabel array sekaligus mendefinisikan isi array. Cara ini dilakukan jika kita sudah tahu nilai yang perlu diberikan. 
<nama-var> merupakan nama variabel array yang dideklarasikan sebanyak n dengan elemen-elemennya adalah <val0>, <val1>, <val2>, … , <valn-1>. Perlu diingat bahwa elemen tersebut terurut berdasarkan indeks dari 0 hingga n-1. 

Contohnya sebagai berikut.

"""
var_arr = [9,8,7,6,5,4,3,2,1,0]
print(var_arr)
"""
Pada variabel "var_arr" kita menyimpan elemen bertipe integer dengan panjangnya adalah 10 elemen dan alamat setiap elemen array (indeks) adalah indeks ke-0 hingga 9.

Mendefinisikan Nilai Default
Jika tidak mengetahui nilai yang diberikan, kita dapat memberikan nilai default terlebih dahulu sebagai upaya untuk memberikan nilai awal. Umumnya, nilai default ini ditentukan karena kita tidak tahu nilai seharusnya. 

Dalam prosesnya, kita bisa secara perlahan mengganti masing-masing nilai tersebut sesuai kebutuhan. Misal kita memiliki array "[0,0,0,0]", yang kemudian hari kita bisa memperbaruinya menjadi "[1,2,0,4]", dengan begitu kita bisa mengetahui bahwa indeks ke-2 pada array tersebut belum kita perbarui. 

Nilai default ditentukan oleh kesepakatan bersama sesuai kebutuhan yang nilainya di luar dari rentang yang disepakati. Misalnya, tim Anda menentukan nilai dalam list harus berkisar dari 1 hingga 10. Kita bisa menyepakati "0" sebagai nilai default karena di luar jangkauan yang disepakati (1-10).

Berikut adalah struktur mendeklarasikan variabel array dengan mendefinisikan nilai default.

<nama-var> = [<default-val>for in range(<n>)]

Jika Anda merasa familier dengan struktur tersebut, Anda benar. Struktur tersebut merupakan struktur yang sama dengan list comprehension. Anda dapat menginisialisasi variabel array dengan menggunakan list comprehension dan mendefinisikan nilai default. Pada materi List Comprehension, kita menggunakan ekspresi Namun, pada array kita menggunakan default value atau <default-val>.

Berikut adalah penjelasan lebih detail terkait struktur tersebut.

<nama-var> merupakan variabel yang Anda deklarasikan.
<default-val> merupakan nilai default yang Anda definisikan. Umumnya, programmer akan menggunakan nilai di luar range yang telah disepakati sebagai nilai default. Misalnya jika range nilai yang disepakati seharusnya 1 hingga 10, nilai default bisa kita definisikan dengan 0. 
<n> merupakan ukuran panjangnya array.
Mari lihat contoh penerapannya di bawah ini.
"""
var_arr = [0 for i in range(10)]
print(var_arr)
"""
Pada contoh di atas, kita membuat list dengan nilai default-nya adalah "0" sebanyak 10 elemen. Perhatikan bahwa <default-val> yang ada pada struktur sebelumnya diubah menjadi "0" untuk mendapatkan nilai default "0".

Dari sini, Anda dapat mengubah nilai default tersebut dengan nilai yang baru berdasarkan hasil suatu operasi. Misalkan pada contoh di bawah ini.
"""
var_arr = [0 for i in range(10)]

for i in range(10):
    var_arr[i] = i

print(var_arr)
"""
Pada contoh di atas, kita membuat program untuk mengubah nilai default pada variabel array "var_arr" dengan nilai 0 hingga 9. Output dari program tersebut adalah mengubah nilai yang awalnya adalah [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] menjadi [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

Mengakses Elemen Array
Mengakses elemen array dalam Python tidak berbeda dengan mengakses elemen pada list. Hal ini karena kita menggunakan list sebagai "bentuk lain" dari array. Anda dapat melakukan metode indexing untuk mengakses elemen array. Berikut adalah struktur untuk melakukan hal tersebut.

<namaVariableArray>[<index>]

<namaVariabelArray> merupakan nama variabel array yang sebelumnya telah Anda deklarasikan. <indeks> merupakan urutan indeks yang ingin Anda akses sehingga nilai atau elemen tersebut dapat diambil atau ditampilkan.
"""

var_arr = [1,2,3,4,5,6,7,8,9]
print(var_arr[0])
"""
Pada contoh di atas, kita mengambil indeks ke-0 pada variabel "var_arr" yang bernilai 9. Jadi, output yang dihasilkan adalah 9.

Pemrosesan Sekuensial pada Array
Pemrosesan array merujuk kepada operasi-operasi yang dilakukan pada elemen-elemen suatu array. Operasi ini melibatkan manipulasi hingga pengolahan elemen yang ada pada array. 

Adapun pemrosesan sekuensial adalah sebuah pemrosesan setiap elemen array yang dimulai dari elemen pada indeks terkecil hingga terbesar. Pemrosesan sekuensial lebih sering menggunakan pengulangan (loop/iterasi) dalam setiap prosesnya.

Sebab pemrosesan sekuensial melibatkan semua elemen di dalamnya, ada beberapa hal yang perlu diperhatikan.

Setiap elemen array diakses secara langsung melalui indeksnya (metode indexing).
Elemen pertama (first element) adalah elemen array dengan indeks terkecil yang selalu dimulai dari 0. 
Elemen selanjutnya (next element) dicapai melalui suksesor indeks.
Kondisi berhenti dicapai jika indeks yang diproses adalah indeks terbesar yang sudah terdefinisi.
Suatu array tidak boleh kosong, minimal memiliki satu elemen di dalamnya.
Mari bahas lebih lanjut dengan contoh di bawah ini.
"""
var_arr = [1,2,3,4,5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None

    print(f"current element: {current_element} , next elements: {next_element}")

"""
Pada contoh di atas, kita membuat program untuk melakukan pemrosesan sekuensial array. Proses tersebut adalah mencetak setiap elemen yang berada pada variabel array "var_arr" menggunakan perulangan loop. 
Pertama-tama, kita menginisialisasi variabel "var_arr" dengan nilai "[1, 2, 3, 4, 5]". Perulangan for digunakan untuk melakukan iterasi melalui setiap elemen array. Variabel "i" bertindak sebagai indeks saat ini yang digunakan untuk mengakses elemen dalam setiap iterasi atau perulangan.

Kemudian, setiap proses perulangan berlangsung, kita mengambil elemen saat ini menggunakan "var_arr[i]" dan menyimpannya pada variabel "current_element". Selanjutnya adalah mencari indeks berikutnya dengan cara menambahkan nilai "1" pada indeks saat ini atau "i". 

Hasil dari operasi penjumlahan nilai "1" dengan indeks saat ini akan disimpan pada variabel "next_index". "next_index" berperan sebagai "suksesor indeks" yang merujuk pada indeks berikutnya berdasarkan indeks saat ini dengan menambahkan nilai "1". 

Kemudian kita memeriksa "next_index" berada dalam rentang indeks yang valid dalam array atau tidak. Jika iya, artinya masih ada elemen berikutnya, dan kita ambil elemen berikutnya tersebut menggunakan "var_arr[next_index]" serta menyimpannya dalam variabel "next_element". Sebaliknya, jika "next_index" tidak valid atau melebihi rentang array, artinya tidak ada elemen berikutnya sehingga kita menetapkan "next_element" sebagai "None".

Pada langkah terakhir, kita mencetak nilai "current_element" dan "next_element" untuk menunjukkan perbedaan antara elemen sekarang dan selanjutnya.

Mencetak setiap elemen array menggunakan perulangan adalah satu di antara banyaknya contoh-contoh persoalan pemrosesan sekuensial pada array. Contoh lain dari pemrosesan array adalah berikut.

Mengisi array secara sekuensial.
Menghitung nilai rata-rata elemen array.
Mengalikan elemen array dengan suatu nilai.
Mencari nilai terbesar atau terkecil pada array.
Mencari indeks letak suatu nilai ditemukan pertama kali dalam array, dan sebagainya.
Dari sekian banyak contoh pemrosesan tersebut, mari kita pelajari dalam materi berikutnya tentang cara mencari nilai terbesar pada array.


Latihan Array
Pada materi sebelumnya, kita telah memahami bahwa array adalah salah satu jenis dari struktur data linear. Array mengumpulkan elemen-elemen berdasarkan indeks secara berurutan atau linear.

Pemrosesan array merujuk pada operasi-operasi yang dilakukan pada elemen-elemen suatu array. Salah satu operasinya adalah pemrosesan sekuensial yang merupakan sebuah pemrosesan setiap elemen array, dimulai dari elemen pada indeks terkecil hingga indeks terbesar.

Dari sekian banyaknya contoh pemrosesan sekuensial pada array, mari kita pelajari salah satunya, yakni mencari nilai terbesar dalam array.

[1,7,2,89,3]

Kita memiliki array yang beranggotakan nilai integer dengan elemen indeks ke-0 adalah 1, elemen indeks ke-1 adalah 7, elemen indeks ke-2 adalah 2, elemen indeks ke-3 adalah 89, elemen indeks ke-4 adalah 3.

Kita akan mencari nilai atau elemen terbesar dari array tersebut menggunakan algoritma two pointers. Algoritma adalah serangkaian langkah-langkah terstruktur yang dirancang untuk menyelesaikan suatu masalah atau mencapai suatu tujuan. Dalam hal ini, tujuan yang ingin dicapai adalah mencari nilai terbesar pada array.

Algoritma two pointers adalah algoritma yang memiliki pendekatan dengan cara memanipulasi atau memproses urutan data menggunakan dua penanda atau dua pointer secara bersamaan. Kedua pointer tersebut bisa kita sebut sebagai "left" dan "right".

[1,7,2,89,3]
left = 1
right = 7

Untuk memahami algoritma ini, perhatikan beberapa informasi berikut.

Pointer "left" akan berada pada indeks pertama dan menyatakan bahwa pointer "left" selalu menunjukkan nilai terbesar dalam array.
Pointer "right" akan selalu berada pada elemen selanjutnya dan membandingkannya dengan elemen pointer "left".

Mari kita bedah satu per satu setiap langkah-langkahnya, simak penjelasan berikut.

Pertama, kita memulai dengan dua pointer: pointer "left" pada elemen pertama (1) dan pointer "right" pada elemen berikutnya (7). Kita membandingkan nilai 7 dengan nilai 1. Sebab 7 lebih besar dari 1, kita mengganti nilai pointer "left" dari 1 menjadi 7.
Sekarang, pointer "left" berada pada elemen 7 dan pointer "right" berada pada elemen berikutnya (2). Kita membandingkan nilai 7 dengan 2. Sebab 2 tidak lebih besar dari 7, pointer "left" tetap pada nilai 7.
Pointer "right" berpindah ke elemen berikutnya (89), sementara pointer "left" tetap pada nilai 7. Kita membandingkan nilai 89 dengan 7. Sebab 89 lebih besar dari 7, pointer "left" berpindah ke nilai 89.
Sekarang, pointer "left" berada pada elemen 89 dan pointer "right" berada pada elemen berikutnya (3). Kita membandingkan nilai 89 dengan 3. Sebab 3 tidak lebih besar dari 89, pointer "left" tetap pada nilai 89.
Proses berakhir, nilai pada pointer "left" ditetapkan sebagai nilai terbesar dalam array.
Dengan demikian, kita menggunakan dua pointer untuk membandingkan dan mengganti nilai pointer "left" jika ada nilai yang lebih besar saat melintasi array. Pada akhirnya, nilai pada pointer "left" adalah nilai terbesar dalam array.

Sekarang Anda sudah paham secara teoretis cara algoritma two pointers bekerja untuk memproses array dalam mencari nilai terbesar. Selanjutnya, mari kita ubah penjelasan tersebut ke dalam program Python. 
"""
var_arr = [1,7,2,89,3]
left_pointer = var_arr[0]


for i in range(1,len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)

"""
Pada program di atas, hal pertama yang dilakukan adalah menginisialisasi variabel "var_arr" dengan array "[1, 7, 2, 89, 3]". Kedua, kita menginisialisasi variabel "left_pointer" dengan nilainya adalah indeks pertama variabel "var_arr" (var_arr[0]).  

Kita menggunakan perulangan "for" untuk mengakses semua indeks dari indeks ke-1 hingga panjang array. Untuk mengetahui panjang array, kita menggunakan fungsi "len()", yang  bertujuan menghitung panjang atau banyaknya elemen dari list, set, dan string. 

Dalam perulangan "for" tersebut kita mendeklarasikan variabel "right_pointer" yang akan terus berpindah dari indeks ke-1 hingga indeks terakhir (akhir panjang array). Setelah memiliki "left_pointer" dan "right_pointer", kita membandingkan nilai keduanya. Jika "right_pointer" lebih besar dari "left_pointer", kita akan memperbarui nilai "left_pointer" dengan nilai "right_pointer".

Proses tersebut terjadi secara berulang sampai nilai yang tersimpan dalam "left_pointer" dijadikan sebagai nilai maksimal dari array. Lalu, kita mencetak nilai tersebut dengan perintah "print(left_pointer)".
"""

var_arr = [i for i in range(101)]
result = sum(var_arr)
print(result)

"""
Fundamental Matriks
Pada materi sebelumnya, kita telah mempelajari cara menyimpan data yang sama menggunakan array dalam Python dengan list. Untuk pengingat, array merupakan salah satu jenis struktur data linear dan terdiri dari kumpulan elemen bertipe data sama dengan indeks yang berurutan atau linear. 

Sebenarnya, array adalah jenis struktur data 1 dimensi yang menyimpan semua datanya secara linear. Pada materi ini, kita akan mempelajari jenis array 2 dimensi, yakni matriks.

arrray 1 dimensi
[3,6,8,1,9]-> hanya 1 baris dan 5 kolom

array 2 dimensi (matriks)
[3,6,8,1,9]         2 baris dan 5 kolom
[12,13,67,16,90]    

Matriks pada matematika merupakan himpunan yang terdiri dari bilangan atau elemen berdasarkan baris dan kolom. Dalam matematika, struktur matriks sebagai berikut.




    [0  1   0    0   0] -> baris pertama
    [4  2   2    0   0] ->baris kedua
A = [2  4   2   0   0] -> baris ketiga
    [1  1   2   0   0] -> baris keempat
    [0  0   1   2   1] ->baris kelima
    c1  c2  c3  c4  c5


Dalam matematika, penamaan baris dan kolom dibuat secara berurutan, baris ke-1 dimulai dari atas hingga ke bawah dan kolom ke-1 dimulai dari kiri ke kanan.

Contoh matriks dalam matematika beragam jenisnya, beberapa di antaranya sebagai berikut.

Matriks Pengukuran
Matriks pengukuran adalah jenis matriks dengan indeks (i, j) yang merepresentasikan suatu titik koordinat. Setiap elemen dari matriks ini merepresentasikan hasil pengukuran pada suatu titik koordinat tertentu dan termasuk bilangan real atau tipe data float.

        1       2       3       4       5
    1   12.5    7.0     8.9     0.7     6.6
    2   0.0     1.6     2.1     45.9    55.0
    3   6.1     8.0     0.0     3.1     21.9
    4   9.0     1.0     2.7     22.1    6.2
    5   5.0     0.8     0.8     2.0     8.1

Gambar di atas merupakan matriks pengukuran yang merepresentasikan suatu titik koordinat tertentu. Perhatikan bahwa setiap elemennya merupakan bilangan real atau bertipe data float dalam pemrograman.

Matriks Satuan
Selanjutnya adalah matriks satuan dengan elemen bernilai hanya 0 atau 1. Setiap elemen matriks ini bertipe data integer.

        1       2       3       4
    1   1      0       0       0
    2   0      1       0       0
    3   0       0       1       0
    4   0       0       0       1
Gambar di atas merupakan matriks satuan dengan indeks baris adalah 1 sampai dengan 4 dan indeks kolom 1 sampai dengan 4.
Masih banyak penggunaan matriks dalam matematika yang dapat kita pelajari, seperti matriks nama hari yang merepresentasikan nama hari ke-1 hingga hari ke-7 dan elemen matriksnya bertipe string, matriks value, serta masih banyak lagi.

Anda pun dapat melakukan berbagai operasi pada matriks, seperti penjumlahan, perkalian, menentukan determinan, transpose, dan sebagainya. Bahkan matriks juga dapat dipakai untuk persoalan algoritmik, yakni untuk menyimpan informasi yang cirinya ditentukan oleh dua dimensi atau baris dan kolom, seperti cell pada spreadsheet.

Sementara itu dalam pemrograman, matriks adalah kumpulan data yang diatur dalam bentuk tabel dua dimensi dengan setiap elemennya terdefinisi berdasarkan baris dan kolom. Matriks dalam pemrograman diimplementasikan menggunakan array dua dimensi. Bahkan dalam Python, matriks dapat diimplementasikan menggunakan nested list atau list di dalam list.
"""

Matriks = [[1,2,4],
           [4,5,6],
           [7,8,9]]
"""
Dalam gambar di atas, kita mendeklarasikan variabel "matriks" dan menginisialisasikannya dengan nested list atau list di dalam list. Perhatikan lebih baik,  pada gambar tersebut terdapat dua kurung siku "[]" dan kurung siku pertama adalah list yang membungkus tiga list di dalamnya, yakni "[1, 2, 3], [4, 5, 6], [7, 8, 9]". 

Matriks dalam pemrograman dapat kita simpulkan sebagai berikut.

Matriks adalah kumpulan data yang diatur dalam bentuk tabel dua dimensi dengan setiap elemennya terdefinisi berdasarkan baris dan kolom.
Setiap elemen matriks dapat diakses melalui metode indexing jika kedua indeks telah diketahui.
Elemen matriks dideklarasikan memiliki tipe homogen yang artinya elemen tersebut harus mempunyai tipe data yang sama. Jika elemen tersebut adalah bilangan real, seluruh elemen lainnya pun adalah bilangan real. Walaupun dalam list Python Anda dapat membuat matriks dengan tipe data berbeda, alangkah lebih baik jika tetap mengikuti aturan ini.
Selanjutnya mari ubah gambar di atas menjadi kode Python yang dapat dieksekusi.
"""
Matriks = [[1,2,4],
           [4,5,6],
           [7,8,9]]
print(Matriks)
"""
Pada kode di atas, kita mendeklarasikan variabel "matriks" dan menginisialisasikan dengan nested list. Output yang dihasilkan adalah matriks "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]".

Namun, perlu diingat bahwa mendeklarasikan matriks menggunakan list sangat memakan banyak memori. Masih ingatkah Anda dengan materi array yang menyatakan bahwa setiap nilai atau elemen dalam list akan disimpan pada masing-masing tempat memori? Hal ini berlaku juga pada matriks. 

Jika kita membuat matriks dengan 100 kolom dan 100 baris akan menghasilkan 10.000 elemen integer dalam matriks tersebut dan menggunakan 10.000 penyimpanan untuk menampung semua elemen integer.

Oleh karena itu, menggunakan nested list sebagai matriks dianggap cara yang cukup praktis, tetapi tidak efektif dalam mengelola penyimpanan memori. Jika Anda ingin membuat matriks dengan jumlah elemen yang besar, programmer Python biasanya menggunakan library tambahan seperti NumPy untuk melakukan tugasnya. Library merupakan sekumpulan kode yang telah dibuat oleh developer atau programmer dan disediakan kepada pengguna lain agar dapat digunakan ulang dalam pengembangan program atau perangkat lunak. 

Library NumPy sering dipakai oleh programmer Python untuk melakukan tugas-tugas dalam ranah science dan engineering karena dianggap memiliki penggunaan penyimpanan memori yang efisien. 

Silakan periksa bahwa library NumPy tersedia di komputer Anda dengan menjalankan kode berikut di terminal Anda.

pip show numpy

Jika dalam komputer Anda belum memiliki NumPy, silakan buka kembali terminal Anda dan jalankan perintah berikut.

pip install numpy

Mari lanjutkan dengan implementasi matriks menggunakan NumPy.
"""
import numpy

matriks = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriks)
"""
Pada kode di atas, kita mengimpor library "numpy" terlebih dahulu untuk mengambil fungsi-fungsi atau kode yang berada pada library tersebut. Selanjutnya, kita mendeklarasikan variabel "matriks" dan menginisialisasikannya dengan numpy array.

Ingat bahwa matriks adalah array dua dimensi sehingga pada library NumPy kita menggunakan fungsi ".array()" untuk membuat matriks atau array dua dimensi. Pada kode di atas, kita menggunakan fungsi ".array()" dengan nilai di dalamnya adalah nested list.

Jika Anda bertanya, apakah library NumPy bisa dipakai juga untuk array? Jawabannya adalah iya, Anda bisa menggunakan library ini untuk membuat array juga. Programmer sering kali menggunakan library NumPy jika perlu membuat array atau matriks dalam Python.

Sekarang, mari bandingkan ukuran memori yang digunakan jika kita menggunakan matriks Python dan matriks NumPy.
"""
import numpy
import sys

var_list = [[1,2,3],[4,5,6],[7,8,9]]
var_array = numpy.array([[1,2,3],[4,5,6],[7,8,9]])

print("ukuran keseluruhan elemen list dalam bytes =",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen Numpy dalam bytes = ",var_array.size*var_array.itemsize)
"""
Tenang, jika kode di atas cukup sulit dipahami tidak apa-apa. Anda cukup memperhatikan output dari kode di atas. Pada kode program di atas, kita membandingkan ukuran memori yang dihasilkan dari matriks menggunakan numpy array dan list Python.

Dengan menggunakan matriks yang sama, yakni "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]" menghasilkan jumlah memori yang berbeda terhadap masing-masing metode. Jika kita menggunakan NumPy, memori yang digunakan untuk keseluruhan elemen adalah 72. Namun, jika kita menggunakan list, memori yang digunakan untuk keseluruhan elemen adalah 240.

Inilah alasan banyak programmer Python cenderung memilih NumPy untuk memproses matriks bahkan hingga ke tahap machine learning. 

Catatan: Seluruh materi pada modul ini akan menggunakan list Python untuk mengimplementasikan matriks.

Setelah mengetahui perbedaannya, Anda sudah memiliki bekal yang cukup untuk melaju ke pembelajaran berikutnya. Walaupun memakan banyak memori, pada materi ini kita akan menggunakan list Python untuk memproses matriks. Hal ini agar kita memahami fundamental matriks tanpa melibatkan library apa pun.


Implementasi Matriks pada Python
Sebelumnya kita telah belajar cara mengimplementasikan matriks yang merupakan array dua dimensi menggunakan nested list. Ingat bahwa setiap elemen matriks dideklarasikan memiliki tipe homogen, yang artinya elemen tersebut harus memiliki tipe data yang sama. Jika Anda mendeklarasikan suatu elemen bertipe data float, elemen lainnya pun adalah float.

Sekarang, kita pelajari cara mengimplementasikan matriks pada Python lebih dalam. Kita akan mulai dengan cara mendeklarasikan matriks hingga mengakses setiap elemen matriks dengan metode indexing.



Deklarasi Matriks
Ada dua cara untuk mendeklarasikan matriks menggunakan Python sebagai berikut.

Deklarasi sekaligus inisialisasi nilai matriks.
Cara pertama adalah mendeklarasikan matriks sekaligus menginisialisasikan nilainya dengan ukuran N baris dan M Kolom (NxM). Cara ini dilakukan jika kita telah mengetahui nilai yang perlu diberikan.
Berikut adalah struktur untuk mendeklarasikan matriks dengan menginisialisasikan nilainya sekaligus.
<nama-var> = [[<val-11>,<val-12>,...,<val-1m>],
            [<val-21>,<val-22>,...,<val-2m>],
            ...
            [<val-n1>,<val-n2>,...,<val-nm>]]
Gambar di atas merupakan struktur jika kita ingin mendeklarasikan matriks dengan ukuran nxm. Ingat bahwa tipe elemen tersebut akan bergantung pada nilai yang diberikan. Jika nilai yang diberikan adalah bilangan bulat, tipe elemen adalah integer. Jika nilai yang diberikan adalah bilangan real, tipe elemen adalah float.
Mari lihat implementasi kodenya di bawah ini.
"""
matriks = [[1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1]]
print(matriks)

"""
Pada kode di atas, kita mendeklarasikan variabel matriks dan menginisialisasikannya dengan matriks satuan dan memiliki ukuran baris = 5 dan ukuran kolom = 5. Matriks satuan adalah jenis matriks dengan elemen bernilai hanya 0 dan 1.

Deklarasi dengan nilai default.
Cara kedua adalah mendeklarasikan matriks dengan nilai default. Sebagaimana materi array, nilai default ditentukan oleh kesepakatan bersama sesuai kebutuhan dengan nilainya di luar rentang yang ditentukan. Misalnya, tim Anda menentukan nilai dalam list harus berkisar dari 1 hingga 10. Kita bisa menyepakati nilai "0" sebagai nilai default karena di luar jangkauan yang disepakati (1-10). Cara kedua ini melibatkan list comprehension yang sama seperti pada materi array.

Struktur dari deklarasi dengan nilai default sebagai berikut.
<nama-var> = [[<default-val> for j in range (<m>)] for i in range(<n>)]

Terlihat pada struktur tersebut, cara kedua ini menggunakan dua metode sekaligus, yakni nested list dan nested for. Kita menggunakan nested for atau for bersarang untuk membuat baris dan kolom. Perhatikan baik-baik, perulangan dalam atau perulangan kedua diapit oleh tanda siku "[]" yang artinya hasil dari perulangan kedua adalah baris pada matriks, sedangkan perulangan pertama atau perulangan luar menghasilkan kolom pada matriks.

Nilai dari <default-val> ditentukan kesepakatan bersama, misalnya jika range yang disepakati adalah 1 hingga 10, kita bisa memilih 0 untuk nilai default-nya. Ada pula <n> sebagai jumlah baris matriks yang ingin dibuat dan <m> sebagai jumlah kolom matriks yang diinginkan.

Selanjutnya, mari lihat penerapan kodenya di bawah ini.
"""
matriks = [[0 for j in range(4)] for i in range(3)]
print(matriks)
"""
Pada kode di atas, kita mendeklarasikan variabel matriks dan menginisialisasikannya dengan nested list dan nested for serta nilai default-nya adalah 0. Matriks yang dibuat pada program di atas adalah matriks value dengan setiap elemennya bertipe integer serta memiliki ukuran baris = 3 dan ukuran kolom = 4.

Akses Elemen Matriks
Sekarang, mari pelajari cara mengakses elemen pada matriks. Ingat bahwa matriks merupakan tabel data yang terdiri dari baris dan kolom. Jadi, jika Anda ingin mengakses elemen dari matriks, perlu mengetahui indeks dari baris dan kolom.

Kita akan mengakses elemen matriks menggunakan metode indexing. Ini artinya Anda perlu mengetahui indeks dari baris dan kolom yang ingin diakses. Berikut adalah struktur untuk mengakses elemen matriks dengan metode indexing.

<namamatriks>[<nbrs>][<nkl>]

Berdasarkan struktur di atas, <namamatriks> merupakan variabel yang berisi nilai matriks, <nbrs> merupakan nomor indeks baris yang ingin diakses, dan <nkol> nomor indeks kolom yang ingin diakses.

Perhatikan gambar di bawah ini untuk memahami maksud dari indeks baris dan kolom.

       0       1       2       3       4
    0    1         2      3     4       5 i0
    1    6        7      8       9       10 i1
    2    11       12     13      14      15 i12
    3    16       17      18      19       20 i3
    4    21       22       23       34      25 i4
         i0     i1      i2       i3      i4 
Asumsikan Anda memiliki matriks dengan ukuran 5 baris dan 5 kolom yang setiap elemennya berisi angka dari 1 hingga 25 seperti gambar di atas. Indeks baris ke-0 dimulai dari 1 hingga 5, indeks baris ke-1 dimulai dari 6 hingga 10, dan seterusnya. Indeks kolom ke-0 dimulai dari "1, 6, 11, 16, 21", begitu pun indeks kolom ke-1 dimulai dari "2, 7, 12, 17, 22", dan seterusnya.

Jika kita ingin mengakses nilai 12 pada matriks di atas, nilai tersebut berada pada indeks baris ke-2 dan indeks kolom ke-1. Dalam pemrograman, nilai tersebut bisa diasumsikan dengan "[2][1]" dengan nilai 2 adalah indeks atau nomor baris dan nilai 1 adalah indeks atau nomor kolom.

Mari lihat penerapannya di bawah ini.
"""

var_mat = [[1,2,3,4,5],
           [6,7,8,9,10],
           [11,12,13,14,15],
           [16,17,18,19,20],
           [21,22,23,24,25]]
print(var_mat[2][1])
"""
Pada contoh di atas, kita mendeklarasikan variabel "var_mat" dan menginisialisasikan dengan matriks yang sama seperti gambar sebelumnya. Selanjutnya, kita mengakses elemen matriks yang berada pada indeks baris ke-2 dan indeks kolom ke-1 ([2][1]) serta menampilkannya ke layar. Output dari program tersebut adalah "12" dan nilai tersebut adalah elemen yang berada pada indeks yang kita cari.

Silakan bereksplorasi dengan kode di atas untuk mencari nilai yang Anda inginkan. Ubah "var_mat[2][1]" dengan variabel dan indeks yang diinginkan.

Operasi Matriks pada Python
Dalam matematika ataupun pemrograman, operasi matriks dapat melibatkan dua matriks sekaligus atau pun satu matriks saja. Beberapa operasi tersebut di antaranya sebagai berikut.

Operasi 1 matriks.
Menghitung total semua elemen matriks.
Mengalikan elemen matriks dengan konstanta.
Transpose matriks.
Inverse matriks.
Menentukan determinan, dan sebagainya.
Operasi 2 matriks:
Menambahkan dua matriks.
Mengalikan dua matriks.
Pembagian dua matriks, dan sebagainya.
Dari berbagai operasi matriks yang tersedia, mari kita pelajari salah satu di antaranya, yakni mengalikan elemen matriks dengan konstanta.

Dalam matematika, mengalikan elemen matriks dengan konstanta dapat diilustrasikan seperti gambar berikut. Asumsikan ukuran matriksnya adalah 2x2 atau 2 baris dan 2 kolom.

2 x [5 0] = [10 0]
    [1 -2] = [2 -4]

Pada ilustrasi tersebut, kita mengalikan matriks "[5, 0], [1, -2]" dengan konstanta "2". Nilai konstanta tersebut kemudian dikalikan dengan setiap elemen matriks. Kalkulasinya dapat kita urai seperti berikut. 

Pertama, konstanta "2" akan dikalikan dengan elemen 5 yang menghasilkan nilai 10 (2 X 5 = 10).
Kedua, konstanta "2" akan dikalikan dengan elemen 0 yang menghasilkan nilai 0 (2 X 0 = 0).
Ketiga, konstanta "2" akan dikalikan dengan elemen 1 yang menghasilkan nilai 2 (2 X 1 = 2).
Terakhir, konstanta "2" akan dikalikan dengan elemen -2 yang menghasilkan nilai -4 (2x-2 = -4).
Jika kita ubah ke dalam pemrograman, hasilnya sebagai berikut.
"""
#membuat matriks 2x2
var_mat = [[5,0],
           [1,-2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j]*2

print(def_mat)
"""
Perhatikan penjelasan berikut untuk memahami contoh di atas.

Pertama, kita mendeklarasikan variabel "var_mat" dan menginisialisasikannya dengan matriks yang diinginkan. Di sini, matriks yang digunakan berukuran 2x2 atau 2 baris dan 2 kolom.
Kedua, kita perlu mendeklarasikan variabel "def_mat" sebagai matriks default baru dengan nilai (0). Matriks dengan nilai default ini harus berukuran sama dengan matriks yang asli.
Ketiga, kita akan melakukan perulangan berdasarkan dua kondisi. Kondisi pertama adalah perulangan berdasarkan banyaknya list di dalam matriks ([5, 0], [1, -2]) yang merepresentasikan baris. Kondisi kedua adalah perulangan berdasarkan banyaknya elemen pada setiap list (5,0 dan 1,-2).

Perulangan pertama (i) akan mengulang sebanyak dua kali karena variabel "var_mat" memiliki dua list di dalamnya. Perulangan kedua (j) akan mengulang sebanyak dua kali karena setiap elemen list yang diambil memiliki dua nilai. Jadi, elemen list pertama adalah "5 dan 0" serta elemen list kedua adalah "1 dan -2".

Pada setiap perulangannya, nilai i = 0, 1; j =0, 1. Ingat, ini disebabkan kita mengambil panjang dari variabel "var_mat" yang memang memiliki dua list dan panjang elemen dari setiap list-nya. Fungsi "range()" selalu memulai bilangan dari nol.
Selanjutnya, kita akan meng-update matriks default dengan nilai yang dihasilkan berdasarkan perulangan dan mengalikannya dengan konstanta 2.

Jadi, elemen def_mat[0][0] yang bernilai 0 akan diubah dengan elemen var_mat[0][0] yang bernilai 5 lalu dikalikan dengan 2 dan hasilnya adalah 10. Elemen def_mat[0][0] yang awalnya bernilai 0 berubah menjadi 10.
Perulangan ini terus terjadi hingga semua kondisi terpenuhi dan menyebabkan semua elemen variabel "def_mat" berubah sesuai perkalian dengan konstanta 2.
Phew, materi kali ini sangat erat dengan perhitungan matematika. Cara yang kita pelajari di atas terbilang cukup rumit. Nah, sebenarnya ada cara yang lebih efektif, yaitu dengan menggunakan library NumPy. Perhatikan kode di bawah ini.

Phew, materi kali ini sangat erat dengan perhitungan matematika. Cara yang kita pelajari di atas terbilang cukup rumit. Nah, sebenarnya ada cara yang lebih efektif, yaitu dengan menggunakan library NumPy. Perhatikan kode di bawah ini.
"""
import numpy as np

var_mat = np.array([[5, 0],
                   [1, -2]])
result = var_mat * 2

print(result)