var = "kafka"
umur = 12

angka = 2 + 6
kondisi = angka - 3

print(angka , kondisi)

"""
kafka itu orang gitu deh    
"""
"""
name = input("masukan nama anda:")
print(name)

"""

"""
Data typing
"""

age = 17
gaji = 5000000.0

print(type(age))
print(type(gaji))

"""
output

<class 'int'>
<class 'float'>

"""


angka = 6
angakaa = "6"

print(type(angka))
print(type(angakaa))

"""
output

<class 'int'>
<class 'float'>

"""

"""
Tipe Data

"""

"""
Tipe Data Primitif
int
string
complex
"""

intt = 12
stringg = "kafka"
complexx = 1 + 2j

print(type(intt))
print(type(stringg))
print(type(complexx))
"""
output
class 'int'>
<class 'str'>
<class 'complex'>
"""

var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))


"""
Boolean 
true
false
"""

x = True
print(type(x))
x = False
print(type(x))
"""
output
< class 'bool'>
< class 'bool'>
"""

"""
string
""
"""

nama = "kafka"
print(type(nama))
#output <class 'str'>

multi_line = """halo
kapan kita terakhir chatan nihh udh lama,aku rindu loh suara kamu
ngeluh terus heheh"""
print(multi_line)
"""
output
alo
kapan kita terakhir chatan nihh udh lama,aku rindu loh suara kamu
ngeluh terus heheh
"""
 
x = "kafka"
print(x[3])
#output sesuai apa yang sesuai index
# x[0] = 'f'
#output akan eror
# x[0] ='k'
print(x[1:])

#formatted str
nama = "kafka"
print(f"halo nama saya adalah {nama}")
"""
output halo nama saya adalah kafka
Pada kode di atas, Anda menampilkan string dengan menggunakan metode formatted string. Metode ini diperuntukkan untuk menampilkan variabel bertipe string dengan menggunakan huruf “f” di depan string dan menempatkan variabel di dalam kurung kurawal.
"""
#%-formatting
x = "kafka"
print("nama saya adalah %s"%(x))
"""
Pada kode di atas, Anda menampilkan variabel string dengan menggunakan metode “%-formatting”. Metode ini adalah pendekatan lama yang masih didukung oleh Python. Metode ini menggunakan operator Modulo (%) untuk memasukkan nilai variabel ke dalam string dengan menggunakan format khusus yang ditentukan oleh tipe data variabel.
"""
#str.format()
x = "kafka"
print("nama saya adalah {}".format(x))
"""
Pada kode di atas, Anda menampilkan variabel string dengan menggunakan metode “str.format()”. Metode ini memungkinkan penggabungan variabel/nilai ke dalam string dengan menempatkan tanda kurung kurawal atau {} sebagai penempatan variabel. Sekilas mirip dengan formatted string, pembedanya adalah pada penggunaan “.format” setelah string.
"""
#Tipe Data Collection

#list
x = [1 ,2 ,3 ,4 ,"kafka"]
print(type(x))
#<class list>
"""
Pada kode di atas, nilai yang diawali dengan kurung siku “[]” akan dianggap sebagai data bertipe list.

Setiap data atau elemen dalam list memiliki indeks yang selalu dimulai dari 0. Anda dapat mengakses setiap indeks pada list dengan metode indexing. 
"""
print(x[3])
"""
Pada kode di atas, diambil indeks ke-3 dari list yang telah diinisialisasikan. Mungkin Anda sadar bahwa cara tersebut sama persis dengan mengakses substring pada materi string. Hal ini karena string pada Python merupakan urutan karakter yang setiap karakternya memiliki indeks. Persis seperti list yang setiap datanya juga memiliki indeks.

List Python bersifat mutable yang artinya nilai di dalamnya dapat diubah.
"""
x[0] = "ganteng"
print(x)
"""
Pada kode di atas, Anda mengubah “1” dengan string “Indonesia”. Hal ini dapat terjadi dalam Python karena list bersifat mutable.

Konsep indexing merujuk kepada pengambilan data dalam Python berdasarkan indeksnya. Beberapa cara untuk melakukan indexing sebagai berikut.
"""
x = ['laptop','asus','apple','vision','ywudh']
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x[-2])
"""
Pada dua sintaks pertama, Anda memerintahkan untuk menampilkan indeks ke-0 dan indeks ke-2. Selanjutnya, dua sintaks terakhir memerintahkan untuk menampilkan indeks terakhir dan indeks ke-3 dari terakhir. 


"""
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])
"""
Pada sintaks pertama, Anda memerintahkan untuk mengambil data dari indeks ke-0 hingga indeks ke-4 dengan setiap elemen ke-2 dan kelipatannya akan dilewati. Pada sintaks kedua, Anda memerintahkan untuk menampilkan data dari indeks ke-1 hingga terakhir. Pada sintaks ketiga, Anda memerintahkan untuk menampilkan data dari indeks ke-0 hingga indeks ke-2 (ingat, bersifat eksklusif).
"""
#Tuple

x = (1, 'kafka', 1+2j)
print(type(x))

"""
Pada kode di atas, Anda dapat lihat bahwa nilai yang diapit tanda kurung “()” akan dianggap sebagai tuple oleh program. Anda juga dapat melakukan indexing dan slicing pada tuple sama seperti list. 
"""
x = (1, "kafka" , 1+2j,"kafka","arko")
print(x[1])
print(x[0:3])
"""
Tuple adalah jenis dari list yang tidak dapat diubah elemennya. Umumnya, tuple digunakan untuk data yang bersifat sekali deklarasi dan dapat dieksekusi lebih cepat. Tuple didefinisikan dengan kurung “()“ dan setiap elemen di dalamnya dipisahkan dengan koma.
"""

#set

x = {1,2,3,4,5,6,7,8,8}
print(x[0])
"""
Pada kode di atas, program mengembalikan output 'set' object is not subscriptable karena setiap nilai dalam set tidak memiliki indeks sehingga tidak bisa dilakukan indexing.
"""

x = {1,2,3,4,5,6,7,7,8}
print(x)
print(type(x))
"""
Pada kode di atas, Anda dapat melihat bahwa nilai yang diapit tanda kurawal “{}” akan dianggap sebagai set oleh program dan nilai duplikat di dalamnya akan dihapus. Pada kode di atas pun, nilai 3 dan 2 yang duplikat telah dihapus. 
"""

x = {1,2,3,4,5}
y = {6,7,8,9,10}

union = x.union(y)
print("Union:",union)

intre = x.intersection(y)
print("intersection:",intre)
"""
Pada contoh di atas, kita melakukan operasi union atau penggabungan dua variabel bertipe data set, yakni variabel set1 dan variabel set2 dengan menggunakan method “.union()”. Hasilnya adalah tentu nilai gabungan dari kedua variabel. 

Terakhir, kita juga melakukan intersection atau irisan yang merupakan operasi dalam matematika untuk menemukan nilai atau elemen-elemen yang sama dalam dua atau lebih himpunan. Kita menggunakan method “.intersection()” untuk menjalankan operasi ini. Hasilnya adalah nilai 4 dan 5 yang memang berada pada variabel set1 dan variabel set2.
"""
#dictionary
x = { 'name' :'kafka arko','age' : 20 , 'isMarried' : False}    
# print(type(x))
"""
Pada kode di atas, sintaks yang diapit tanda kurawal “{}” dan memiliki pasangan key-value akan dianggap sebagai data bertipe dictionary oleh program.   
"""
# print(x[0])
"""
Kode di atas menghasilkan error karena Anda mencoba mengakses data pada dictionary dengan menggunakan metode indexing.
"""
x['job'] = "Pelajar"
print(x)
"""
Untuk menambahkan data pada Dictionary, Anda cukup memasukkan key dan value-nya seperti pada contoh kode di atas, yakni “x[‘Job’] = ‘Web Developer’”.
"""
del x['isMarried']
print(x)
"""
Anda dapat menghapus data pada Dictionary dengan menggunakan sintaks “del”. Pada kode di atas, data “isMarried” dihapus.
"""

x['name'] = "arko"
print(x)

#Konversi antara Tipe Data

"""
Setelah mengetahui berbagai tipe data pada Python, Anda pun dapat melakukan konversi antar tipe data dengan menggunakan beberapa fungsi.

Fungsi merupakan blok kode yang dapat dipanggil untuk melakukan tugas tertentu. Anda akan mempelajari fungsi lebih detail pada modul subprogram. Saat ini, Anda cukup memahami bahwa fungsi di bawah ini dapat melakukan operasi terhadap list, set, dan string.

Di bawah ini merupakan berbagai fungsi yang dapat digunakan untuk mengonversi data antar list, set, dan string.
"""

#Konversi Integer ke Float
print(float(5))
#Untuk melakukan konversi dari integer ke float cukup menggunakan fungsi float() dengan memasukkan nilai integer di dalamnya.

#Konversi Float ke Integer
print(int(5.6))
print(int(-5.6))
#Untuk melakukan konversi dari float ke integer cukup menggunakan fungsi int() dengan memasukkan nilai float di dalamnya.

#konverensi dari-dan-ke string
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))
"""
Kode di atas merupakan berbagai fungsi untuk mengonversi dari-dan-ke string. Jika ingin melakukan konversi ke string, Anda cukup menggunakan fungsi str().

Perlu Anda perhatikan bahwa konversi dari-dan-ke string akan melalui pengujian dan dipastikan validitasnya. Jika pengujian dan validitasnya gagal, error akan dihasilkan.


"""
print(int("1p"))
#Kode di atas menghasilkan error karena 1p dianggap tidak valid.

#Konversi Kumpulan Data
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list("kafka"))
"""
Untuk melakukan konversi kumpulan data dari-dan-ke set/list/tuple, Anda cukup menggunakan fungsi dari tipe data yang diinginkan. Misalnya, set(), tuple(), dan list() seperti pada kode di atas.
"""
#Konversi ke Dictionary
print(dict([[1,2],[3,4]]))
#Pada kode di atas terdapat list berisi dua list yang berisi pasangan nilai, yakni [1,2] dan [3,4]. Lalu, list tersebut diubah menjadi dictionary dengan nilai 1 dan 3 sebagai key serta nilai 2 dan 4 sebagai value.
print(dict([[3,22],[4,44]]))
"""
Pada kode di atas terdapat list yang berisi dua tuple dengan pasangan nilai, yakni (3,26) dan (4,44). Setelah diubah menjadi dictionary, nilai 3 dan 4 menjadi key, sedangkan nilai 26 dan 44 menjadi value.
"""

firstName = "kafka arko"
lastName = "ganteng"
age = 1996
isMarried = False
print("nama saya " , firstName , "dan nama terakhir saya", lastName ,  "saya umur", age,"dan saya belom menikah" , isMarried)

#Transformasi Angka, Karakter, dan String

#Mengubah Huruf Besar/Kecil
#upper()
kata = "kafka"
kata = kata.upper()
print(kata)
"""
Pada kode di atas, Anda mengubah string "dicoding" menjadi uppercase dengan menggunakan method .upper(). Hasilnya, string tersebut berubah menjadi "DICODING".
"""
#lower()
kata = "KAFKA"
kata = kata.lower()
print(kata)
"""
Pada kode di atas, Anda mengubah string "DICODING" menjadi lowercase dengan menggunakan method .lower(). Hasilnya, string tersebut berubah menjadi "dicoding".
"""
#r.strip()
print("kafka                    ".rstrip())
"""
Pada kode di atas, Anda menghapus spasi yang berada di sebelah kanan setelah string "Dicoding" menggunakan metode ".rstrip()".
"""
#lstrip()
print("kafak             kafka".lstrip())
"""
Pada kode di atas, Anda menghapus spasi yang berada di sebelah kiri sebelum string "Dicoding" menggunakan metode ".lstrip()".
"""
#strip()
print("     kafka       ".strip())
"""
Pada kode di atas, Anda menghapus spasi yang berada di sebelah kiri dan kanan setelah string "Dicoding" menggunakan metode "strip()".
"""
kata = 'codecodecodekafkacodecodecode'
print(kata.strip("code"))
"""
Anda dapat mengganti whitespace dengan kata atau hal lainnya. Caranya adalah memberikan nilai pada ".strip()". Kode di atas menghapus kata "Code" pada variabel "kata".
"""
#startwith()
print('dicoding indonesia'.startswith('dicoding'))
"""
Pada kode di atas, Anda mencari string "Dicoding" pada string pertama "Dicoding Indonesia". Operasi ini mengembalikan nilai True karena pada string "Dicoding Indonesia" memang diawali dengan string "Dicoding".
"""
#endswith()
print('dicoding indonesia'.endswith('indonesia'))
"""
Pada kode di atas, Anda mencari string "Dicoding" pada string pertama "Dicoding Indonesia". Operasi ini mengembalikan nilai True karena pada string "Dicoding Indonesia" memang diawali dengan string "Dicoding".
"""
#Memisah dan Menggabung String

#join()
print(' '.join(['kafka','indonesia','!']))
"""
Pada kode di atas, Anda menggabungkan string "Dicoding", "Indonesia", dan "!" yang telah disimpan pada variabel list. Perhatikan bahwa pada sintaks awal sebelum ".join()" Anda menambahkan single quotes di sana. Single quotes ini bermaksud agar Anda menentukan delimiter pada setiap kata/nilai yang ingin Anda gabungkan. Pada kode di atas, delimiter-nya adalah whitespace atau spasi.
"""
print('123 '.join(['kafka','indonesia','!']))

#split()
print("kafka arko ardissya".split())
"""
Pada kode di atas, Anda memisahkan string "Dicoding Indonesia !" menjadi "Dicoding",  "Indonesia", dan "!". Perhatikan bahwa kedua string tersebut disimpan sebagai list. 
"""
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))
#Pada kode di atas, Anda memisahkan kalimat panjang yang dibatas oleh newline lalu menyimpannya ke dalam sebuah list.

#Mengganti Elemen String

#replace()
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))
"""
Perhatikan kode di atas, Anda mengubah kata "Coding" menjadi "Pemrograman". Perlu diingat bahwa replace() bersifat case-sensitive. Contohnya, Anda dapat lihat dalam kode di atas bahwa kata "coding" pada "Dicoding" tidak ikut berubah. Hanya kata "Coding" saja yang diubah menjadi "Pemrograman". Hal ini karena kata "coding" pada "Dicoding" berawalan huruf c kecil.
"""
#Pengecekan String

#isupper()
kata = 'KAFKA'
print(kata.isupper())
#Pada kode di atas, Anda memastikan variabel kata mengandung string UPPERCASE atau tidak. Jika iya, nilai "True" dikembalikan.

#islower()
kata = "kafka"
print(kata.islower())
#Pada kode di atas, Anda memastikan variabel kata mengandung string lowercase atau tidak. Jika iya, nilai "True" dikembalikan.

#isalpha()
kata = "kafka"
print(kata.isalpha())
#Pada kode di atas, Anda mencari tahu variabel kata mengandung string alfabet tanpa adanya karakter selain huruf. Jika iya, nilai "True" dikembalikan.
 
 #isalnum()
kata = "kafka123"
print(kata.isalnum())
#Pada kode di atas, Anda memastikan variabel kata mengandung string alfabet dengan numerik atau tidak. Jika iya, nilai "True" akan dikembalikan.

#isdecimal()
print('123'.isdecimal())
#Pada kode di atas, Anda memastikan string Anda berisi angka/numerik. Jika iya, nilai "True" dikembalikan.

#isspace()
print("         ".isspace())
#Pada kode di atas, Anda memastikan string Anda merupakan whitespace atau tidak. Jika iya, nilai "True" akan dikembalikan.

#istitle()
print('dicoding indonesia'.istitle())
#Dalam kode di atas, Anda memastikan string Anda mengandung huruf kapital pada setiap kata pertamanya. Jika iya, nilai "True" akan dikembalikan.

#Formatting pada String

#zfill()
teks = 'code'
tambah_number = teks.zfill(5)
print(tambah_number)
"""
Kita bedah kode di atas lebih detail.

Variabel teks menyimpan nilai string berupa "Code". Perlu dipahami bahwa kata "Code" hanya memiliki 4 huruf atau sederhananya panjang kata "Code" adalah 4.
Variabel tambah_number menyimpan nilai variabel teks dengan memanggil metode zfill(5).  Angka 5 tersebut merupakan parameter untuk menentukan panjang yang diinginkan oleh string. Sederhananya, Anda memastikan bahwa panjang kata "Code" haruslah 5 dan bukan 4. Jadi, program akan menambahkan angka 0 di depan kata "Code" untuk memastikan bahwa panjangnya adalah 5.
Metode zfill() ini berguna ketika ingin memastikan bahwa angka atau nilai dalam string memiliki panjang tetap dan sesuai dengan format yang diinginkan. Metode zfill() dapat diterapkan untuk menetapkan nomor nota atau nomor antrian.


"""

#rjust()
print('kafka'.rjust(50))
"""
Berdasarkan kode di atas, perhatikan bahwa secara default, rjust() akan menambahkan whitespace untuk membuat teks menjorok ke sebelah kanan. Angka 20 yang Anda masukkan bersifat sama seperti pada zfill(). Metode rjust() akan memastikan bahwa panjang teksnya adalah 20 termasuk dengan kata "Dicoding".

Anda bisa menambahkan teks lain, tidak hanya whitespace.
"""
print('dicoding'.rjust(20,"1"))
#Pada kode di atas, Anda menambahkan karakter "!" sebelum string "Dicoding"

#ljust()
print('dicoing'.ljust(20))
#Pada kode di atas, Anda menambahkan karakter whitespace setelah string "Dicoding" sehingga teks tersebut menjadi rata kiri.
print('dicoding'.ljust(20,"1"))
#Pada kode di atas, Anda menambahkan karakter "1" sesudah string "Dicoding"

#center

print('dicoding'.center(20, '-'))
"""
Pada kode di atas, Anda menambahkan karakter strip "-" pada kiri kanan string "Dicoding" sehingga teks tersebut menjadi rata tengah. 

Sekali lagi, Anda harus ingat bahwa zfill(), rjust(), ljust(), dan center() berfungsi sama, yakni memastikan panjang teks sesuai dengan yang diminta.


"""

#string Literals

print("kafka\nkapan terakir bertemu\n sekarang hari jum/'at")
#Pada kode di atas, Anda menampilkan baris teks dalam satu baris kode menggunakan escape character "\n". Jadi, ketika teks tersebut muncul pada layar akan menampilkan baris teks yang awalnya hanya satu baris menjadi tiga baris dan dipisahkan oleh line break.

#raw string
print(r'dicodng\tIndonesia')
"""Pada kode di atas, Anda menampilkan raw string dari "Dicoding\tIndonesia". Perhatikan bahwa escape character (\t) ikut tercetak pada teks tersebut. Hal ini karena raw string akan mencetak string sesuai dengan apa pun input atau teks yang diberikan."""

#Operasi pada List, Set, dan String

#sum()
#menghitung jumlah seluruh total elemen
var_arr = [1,2,3,4]
result = sum(var_arr)
print(result)
#output 10


#len()
#list
contoh_list = [1,2,3,4,5,6,7,8,8,9]

print(contoh_list)
print(len(contoh_list))
"""
Dalam kode di atas, Anda menampilkan panjang dari anggota yang berada pada list. Anda bisa memperhatikan lebih detail setiap anggota list memang berjumlah 9 atau tidak.
"""

#set

contoh_list = set([1,2,2,3,3,5,5,7,8,9,9,9])

print(contoh_list)
print(len(contoh_list))
"""
Pada kode di atas, Anda mengonversi list menjadi set terlebih dahulu. Hal ini menyebabkan anggota list berubah menjadi anggota set yang tidak memiliki duplikat. Setelah itu, Anda mencetak jumlah anggota dari set. Hasilnya adalah anggota set berjumlah 5.
"""

#string

contoh_list = "belajar python seru banget"

print(contoh_list)
print(len(contoh_list))
"""
Pada kode di atas, Anda menghitung jumlah karakter string yang ada pada variabel "contoh_list". Perhatikan bahwa karakter space dihitung sebagai karakter string.


"""

#max () , min ()

angka = [90,100,354,3455,654,442,455]

print(min(angka))
print(max(angka))

"""
Pada kode di atas, Anda mencari anggota dengan nilai terkecil (minimal) dan nilai terbesar (maksimal) pada variabel "angka" yang merupakan list.
"""

#count()

angka = [2,2,2,3,4,5,6]

print(angka.count(2))
#Pada kode di atas, program akan menghitung banyaknya angka 6 dalam list. Namun, pada kode di bawah, program akan menghitung banyaknya substring/huruf "a" dalam string.

string = "kafka itu hebat tau"
sub = "a"

print(string.count(sub))

#in dan Not in

kata = "kafka suka sama ganyu sekarang"

print('nabila' in kata)
print('ganyu' in kata)
print('ganyu' in kata)
print('nabila' in kata)
"""
Ada empat baris kode di atas. Pada baris pertama, Anda mencari kata atau substring "Dicoding" dalam variabel kalimat. Hasilnya, kata tersebut ada dalam variabel kalimat sehingga mengembalikan nilai True. 

Hal ini berlaku sebaliknya pada baris kode ketiga, Anda justru memastikan bahwa substring "Dicoding" tidak ada dalam variabel kalimat. Hasilnya tentu False karena kita sudah tahu pada baris kode pertama bahwa substring "Dicoding" ada dalam variabel kalimat. 

Hal ini juga yang dilakukan pada baris kode kedua dan keempat. Pada kode tersebut yang dicari adalah substring "tidak". Apakah jawabannya? Silakan Anda telaah lebih dalam.
"""
#Memberikan Nilai untuk Multiple Variable

data = ['shirt','white','L','katun']
appereal , color , size , bahan = data

print(data)
print(appereal)
print(color)
print(size)
print(bahan)

"""
Pada kode di atas, Anda melakukan hal yang sama dengan kode sebelumnya. Anda mengakses indeks 0, 1, dan 2 pada variabel "data" yang merupakan list. Namun, alih-alih melakukannya satu persatu, Anda melakukannya sekaligus dalam satu baris kode.

Perlu diperhatikan bahwa jumlah variabel yang ingin Anda masukkan haruslah sama dengan jumlah variabel yang ada pada list atau tuple. Pada variabel data di atas, list yang telah diinisialisasikan beranggota sebanyak tiga dan statement kedua juga melakukan inisialisasi tiga data, yakni "apparel, color, size". Tidak percaya? Silakan ubah kode "apparel, color, size" menjadi "apparel, color, size, size_chart".
"""

#sort()

kendaraan = ['mobil','pesawat','angkot','taxi']
kendaraan.sort()

print(kendaraan)

"""
Pada kode di atas, Anda mengurutkan anggota variabel "kendaraan" yang merupakan list. Perhatikan cara fungsi sort() mengurutkan anggota di dalamnya. Anggota list merupakan string maka akan diurutkan berdasarkan huruf pertamanya dalam alfabet.
"""

kendaraan.sort(reverse=True)
print(kendaraan)
"""
Pada kode di atas, Anda mengurutkan variabel "kendaraan" secara descending atau menurun. Hal ini membuktikan bahwa secara default fungsi sort() akan mengurutkan secara ascending atau menaik.

Metode sort tidak dapat mengurutkan list yang memiliki angka dan string sekaligus di dalamnya.

Metode sort menggunakan urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).
"""

