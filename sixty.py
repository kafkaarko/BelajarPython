"""
Class, Object, dan Method
Sebelum mengenal secara teknis class, object, dan method. Mari kita berandai-andai sejenak untuk memahami konsep object-oriented programming (OOP). 

Bayangkan Anda adalah seorang penggiat mobil, suatu waktu teman Anda yang berasal dari antah-berantah datang menghampiri. Kalian pun mulai berbincang dan dimulai dengan dia yang bertanya satu hal, "Apa itu mobil?".

Anda bisa menjawab, "Mobil adalah jenis kendaraan dengan empat roda yang memiliki kemampuan untuk bergerak maju, mundur, berbelok, dan berhenti. Mobil dapat melaju dengan kecepatan dari 0 hingga 160 km/jam. Mobil juga memiliki variasi warna yang beragam, termasuk merah, hitam, dan warna lainnya."
Berdasarkan ilustrasi tersebut, mobil dapat dikatakan sebagai sebuah kelas (class) dan perilaku (method) mobil tersebut dapat melaju, mundur, berbelok, dan berhenti. Mobil memiliki atribut warna dan warna tersebut bisa beragam, seperti merah, hitam, dan sebagainya serta memiliki kecepatan berkisar antara 0 hingga 160 km/jam.

Class dapat diibaratkan sebagai blueprint atau cetakan. Dalam contoh percakapan di atas, mobil dapat digambarkan sebagai contoh class atau blueprint. Ketika class telah dibuat, Anda dapat membuat sebuah objek baru berdasarkan class tersebut. Objek baru ini memiliki karakteristik, atribut, dan perilaku sama dengan class yang menjadi cetakannya. Anda pun dapat mengubah nilai atribut dari objek tersebut. Perhatikan gambar di bawah ini.
Pada gambar di atas, kita memiliki sebuah kelas bernama Mobil. Kelas ini memiliki method, yaitu bergerak maju, mundur, berbelok, dan berhenti. Dari kelas ini, kita bisa membuat objek baru, misalkan membuat mobil Dicoding.

Objek baru tersebut memiliki unsur method dan atribut sama dengan kelas yang menjadi cetakannya. Bahkan, kita bisa mengubahnya sesuai keinginan. Misalnya pada objek Mobil Dicoding, kita mengubah warnanya menjadi biru. Jika kita tarik ke perandaian lain, ini mirip seperti manusia di seluruh dunia. Kita memiliki teman bernama Budi, Herman, dan Asep yang walaupun nama mereka berbeda, tetapi mereka tetaplah sama-sama manusia seperti kita.

Tidak hanya objek, Anda juga dapat membuat kelas baru untuk mewarisi kelas yang sudah ada.
Terlihat seperti gambar di atas, anggaplah kita memiliki mobil sebagai kelas dasar dengan method maju, mundur, berbelok, dan berhenti. Selain itu, kelas dasar mobil memiliki atribut warna dan kecepatan.

Ketika membuat kelas baru, seperti Mobil Sport, kita dapat menggunakan kelas yang sudah ada (mobil sebagai kelas dasar) untuk mewarisi beberapa hal, mulai dari atribut warna, kecepatan hingga beberapa perilakunya, yakni maju, mundur, berbelok, dan berhenti. Namun, kita ingin menambahkan metode baru karena ini adalah mobil sport. Metode baru tersebut adalah turbo yang meningkatkan kecepatan secara signifikan.

Secara umum, konsep OOP dalam pemrograman sangat mirip seperti ilustrasi-ilustrasi di atas. Object-oriented programming adalah paradigma pemrograman berorientasi pada pengorganisasian kode menjadi objek-objek yang memiliki atribut dan perilaku (method). Objek merupakan perwujudan dari class dengan anggapan bahwa kelas adalah cetakan yang memungkinkan kita dapat membuat banyak objek berdasarkan cetakan tersebut.

Method adalah perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas. Sebagaimana halnya maju, mundur, berbelok, dan berhenti pada contoh sebelumnya. Atribut adalah variabel yang menjadi identitas dari objek atau kelas, seperti warna dan kecepatan pada contoh sebelumnya.

Mari sederhanakan dengan tabel berikut.

Nama	Deskripsi	Contoh
Class (Kelas)

Cetakan (blueprint) untuk membuat objek-objek yang memiliki karakteristik dan perilaku serupa.

Mobil; Manusia.

Object (Objek)

Perwujudan dari kelas.

Mobil Dicoding; Budi, Herman, Asep.

Perilaku (Method)

Perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas.

Maju, mundur, berbelok, berhenti.

Atribut

Variabel yang menjadi identitas dari objek atau kelas.

Warna, kecepatan, merek.

Class
Pembuatan class dalam Python mirip seperti fungsi, yakni perlu menggunakan keyword untuk bisa membuatnya. Keyword atau kata kunci untuk membuat kelas dalam Python adalah "class". Mari kita buat sebuah kelas bernama mobil.
"""

class Mobil:
    pass
"""
Pada contoh di atas, kita membuat kelas bernama Mobil. Namun, kelas ini atribut dan method-nya belum didefinisikan sehingga kita masukkan pernyataan "pass" supaya tidak menghasilkan error. Ingat bahwa class merupakan blok kode sehingga Anda perlu memperhatikan indentasi untuk membuatnya.

Selanjutnya, mari isi kelas tersebut dengan sebuah atribut. Ingat bahwa atribut adalah variabel yang menjadi identitas dari objek atau kelas.
"""

class Mobil:
    #atribut
    warna = "Merah"
"""
Pada contoh di atas, kita memberikan variabel warna untuk menjadi atribut atau identitas bawaan dari kelas Mobil. Jika Anda jalankan kode tersebut, tidak akan ada output yang keluar. Hal ini karena kita belum memanggil kelas tersebut dan mendefinisikan kembalian nilai (return).

Object (Objek)
Untuk memanggil kelas yang telah dibuat, kita membuat sebuah objek. Berdasarkan KBBI dari kemendikbud, objek merupakan benda, hal, dan sebagainya yang dijadikan sasaran untuk diteliti, diperhatikan, dan sebagainya. Keterkaitan antara objek dan class sangat erat. Contohnya, jika Anda membuat kelas bernama manusia, objeknya adalah manusia dengan nama yang berbeda.

Anda bisa umpamakan kelas adalah bentuk abstrak dari objek, layaknya cetakan atau blueprint. Saat kelas diwujudkan menjadi bentuk yang lebih nyata, proses ini disebut sebagai instansiasi. Itulah sebabnya objek disebut juga sebagai instance atau instance of the class.

Pada contoh sebelumnya, kita telah membuat class. Untuk memanggilnya, kita harus mengubahnya menjadi bentuk yang lebih nyata atau bisa dikatakan objek dari kelas tersebut perlu dibuat. 

class Mobil:
    # Atribut
    warna = "Merah"
 
mobil_1 = Mobil()

Pada contoh di atas, kita memanggil sebuah class dengan menyebutkan namanya diikuti oleh tanda kurung buka dan tutup "()", mirip seperti memanggil fungsi. Selanjutnya pada baris kode "mobil_1 = Mobil()", kita membuat sebuah objek dari kelas Mobil dan menyimpannya dalam variabel mobil_1.

Tidak seperti fungsi, variabel dalam contoh di atas adalah objek yang merupakan perwujudan dari kelas yang telah kita buat. Ini berarti variabel tersebut sekarang memiliki atribut yang identik dengan kelas tersebut.
"""

class Mobil:
    #atribut
    warna = "Merah"

mobil_1 = Mobil()
print(mobil_1.warna)
"""
Pada contoh di atas, kita memanggil atribut objek yang berasal dari kelas Mobil, yaitu "Merah". Untuk memanggil atribut, kita dapat menyebutkan objek atau instance diikuti dengan nama atributnya. 

print(mobil_1.warna) mobil_1  =nama objek warna = atribut

Dengan membuat objek yang merupakan instance dari kelas, kita pun dapat mengubah atribut tersebut sesuai kebutuhan. Contohnya berikut.

"""

class Mobil:
    #atribut
    warna = "Merah"

mobil_1 = Mobil()
mobil_1.warna = "biru"
print(mobil_1.warna)
"""
Pada contoh di atas, kita mengubah atribut kelas yang awalnya bernilai merah menjadi biru dengan mendeklarasikan ulang nilainya. Perhatikan kode "mobil_1.warna = 'Biru'", itu merupakan kode yang digunakan untuk mengubah nilai atribut kelas.

Atribut
Dalam Python, ada dua jenis atribut kelas yang dapat dibagi, yaitu atribut kelas dan atribut objek atau instance. Atribut kelas adalah jenis atribut yang secara otomatis terdefinisi dan menjadi bawaan kelas ketika instance dibuat berdasarkan kelas tersebut. Anda dapat menganggapnya sebagai nilai default atau bawaan dari kelas. Jika Anda membuat beberapa objek berdasarkan kelas yang memiliki jenis atribut ini, setiap objek akan memiliki atribut yang sama dengan nilai yang sama. 

Namun, perlu diperhatikan bahwa jenis atribut kelas memiliki kelemahan, yaitu ketika nilai atribut kelas diubah, perubahan tersebut akan memengaruhi semua objek yang dibuat berdasarkan kelas tersebut.

Perhatikan contoh berikut. Asumsikan bahwa kita membuat sebuah kelas bernama "Mobil" dengan atribut "warna". Lalu, dari kelas tersebut kita akan membuat dua objek atau instance.
"""

class Mobil:
    #atribut class
    warna = "merah"

mobil1 = Mobil()
print(mobil1.warna)

mobil2 = Mobil()
print(mobil2.warna)

#mengubah attr kelas

Mobil.warna = "HITAM"

print(mobil1.warna)
print(mobil2.warna)

"""
Pada contoh di atas, kita membuat kelas bernama "Mobil" dengan atribut "warna" diisi dengan nilai "Merah". Selanjutnya, pada kode di bawah ini kita buat dua instance baru yang diambil dari kelas mobil tersebut. Instance pertama adalah "mobil1" dan instance kedua adalah "mobil2".

Apa yang terjadi dengan objeknya? Kita cetak atribut mobil1 dan mobil2 dengan menggunakan print(). Hasilnya seperti yang Anda lihat sebelumnya bahwa kini kedua atribut pada masing-masing objek ikut mengalami perubahan yang awalnya "Merah" menjadi "Hitam".

Kelemahan ini akan menjadi masalah jika kita ingin setiap objek memiliki atribut masing-masing yang menjadi ciri khasnya. Sama seperti manusia yang bisa beragam dan mempunyai ciri khas walau dalam satu "blueprint" yang sama.

Jenis atribut yang kedua adalah atribut objek atau atribut instance. Jenis atribut ini memungkinkan setiap instance dari kelas memiliki atribut yang berbeda-beda sesuai dengan keinginan. 

Namun, untuk membuat atribut instance kita perlu menggunakan class constructor.

Class Constructor
Pembangun kelas atau class constructor adalah sebuah fungsi khusus dalam Python yang digunakan untuk menentukan nilai awal atau kondisi awal dari suatu kelas. Dengan fungsi ini, saat kita melakukan proses instansiasi atau pembuatan objek baru, hal pertama yang dilakukan adalah memanggilnya terlebih dahulu.

class Mobil:
    def __init__(self):
        self.warna = 'Merah'


Pada contoh di atas, kita membuat fungsi bernama "__init__" sebagai fungsi khusus untuk menjadi constructor. Selanjutnya, kita menggunakan parameter self, yakni sebuah kata kunci untuk merujuk pada objek yang sedang diproses saat ini.

Ini artinya ketika Anda membuat instance baru bernama "mobil_1", constructor akan dipanggil pertama kali dan self akan merujuk pada instance atau objek "mobil_1" tersebut. Begitu pun kalau kita membuat instance baru lainnya bernama "mobil_2", constructor akan dipanggil pertama kali dan self akan merujuk pada instance "mobil_2". 

Hal ini memungkinkan setiap objek baru tersebut memiliki atribut masing-masing, tidak lagi atribut kelas. Jadi, kita dapat mengubah atribut suatu objek tanpa memengaruhi objek lainnya. 

Dengan begitu, self.warna yang didefinisikan dalam constructor adalah jenis dari atribut instance atau atribut objek, yakni atribut yang terkait dengan instance atau objek itu sendiri, bukan kelas. 

Mari kita kembali pada contoh kelas mobil dengan atribut warna. Kali ini kita akan mengubah nilai atribut kembali, tetapi perbedaannya adalah atribut tersebut bukan jenis atribut kelas melainkan atribut instance.
"""

class Mobil:
    #attr instance
    def __init__(self):
        self.warna ='merah'

mobil1 = Mobil()
mobil2 = Mobil()

print(mobil1.warna)
print(mobil2.warna)

#mengubah attr intance

mobil1.warna = "HITAM"

#menampilkan kembali attr warna

print(mobil1.warna)
print(mobil2.warna)

"""
Pada contoh di atas, kita membuat kelas bernama Mobil dengan atribut instance adalah warna dan nilainya merah. Selanjutnya, kita membuat dua instance baru bernama "mobil_1" dan "mobil_2". Jika kita cetak atribut kedua objek tersebut ke layar, hasilnya adalah "Merah" untuk kedua atribut tersebut.

Selanjutnya kita ubah atribut instance pada instance "mobil_1" dengan sintaks mobil_1.warna = "Hitam". Sintaks ini mengganti atribut objek tersebut dari awalnya merah menjadi hitam.

Untuk mengetahui perbedaannya, kita cetak kembali kedua instance tersebut menggunakan fungsi "print()". Hasilnya atribut instance mobil_1 berubah menjadi hitam, sedangkan instance mobil_2 tetap merah. 

Jika terlintas dalam benak Anda, mengapa sintaksnya mobil_1.warna = "Hitam" bukan Mobil.warna = "Hitam"? Jawabannya dapat dilihat jika Anda mengubah kode di atas dengan kode tersebut. Silakan untuk melakukan copy-paste terhadap sintaks yang dimaksud. 

Output yang dihasilkan adalah program menampilkan "Merah" semuanya. Artinya atribut pada setiap objeknya tidak terjadi perubahan. Hal ini karena pada kelas yang kita buat tidak memiliki atribut kelas, sedangkan sintaks Mobil.warna = "Hitam" bertujuan untuk mengubah jenis atribut kelas. 

Jika sebelumnya kita hanya menggunakan parameter self saja dalam class constructor, parameter lain pun dapat ditambahkan sesuai kebutuhan.
"""

class Mobil:
    def __init__ (self,warna,merek,kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

mobil_1 = Mobil("merah","samsung",150)

print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)

"""
Pada contoh di atas, kita membuat kelas yang sama, tetapi ada perbedaan dengan yang sebelumnya. Perbedaannya adalah pada kode di atas, kita membuat parameter tambahan, yaitu "warna, merek, kecepatan". Parameter tambahan ini membuat kita perlu menggunakan argumen ketika memanggil kelas mobil "Mobil('Merah', 'DicodingCar', 160)". Jika Anda memanggil kelas tanpa argumen yang disebutkan, program akan menyebabkan error.

Hal penting yang perlu diketahui adalah perbedaan antara kode di atas dengan kode sebelumnya. Sebelumnya, kode hanya menggunakan parameter "self". Lalu, jika kita menggunakan kode seperti berikut.

Semua atribut yang telah ditetapkan tidak memiliki nilai default. Ketika membuat sebuah objek dari kelas tersebut, kita perlu menambahkan argumen tambahan seperti yang disebutkan, yaitu warna, merek, kecepatan. Inilah sebabnya ketika proses instansiasi atau pembuatan objek, program akan memunculkan error jika tidak memberikan argumen apa pun.

Method
Setelah atribut, saatnya membahas method sebagai perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas. Pada pembuatan metode , sebenarnya kita membuat fungsi di dalam kelas itu sendiri. Dengan kata lain, kita menggunakan kata kunci "def" atau membuat fungsi sebagai suatu metode. Python membagi method menjadi tiga jenis.

Metode dari object (object method).
Metode secara statis (static method).
Metode dari class (class method).
Dua metode terakhir sangat erat kaitannya dengan konsep dekorator. Kita tidak akan membahasnya lebih detail mengenai dekorator, tetapi secara umum saja. 

Dekorator adalah fungsi dalam Python yang mengembalikan fungsi lain, biasanya diawali dengan sintaks "@" di awal.  Contoh sederhana dekorator sebagai berikut.
"""

def my_decorator(func):
    def wrapper():
        print("sebulum ini di eksekusi")
        func()
        print("Setelah di eksekusi")
    return wrapper

#dekorasi fungsi dengan decorator

@my_decorator
def say_hello():
    print("hello world")

#memanggil fungsi yang decorasi
say_hello()
"""
Penjelasan dari contoh di atas adalah berikut.

Pertama, kita mendefinisikan sebuah fungsi bernama my_decorator. Dekorator ini menerima sebuah fungsi func sebagai parameternya.
Dalam fungsi my_decorator, kita mendefinisikan fungsi wrapper(). Fungsi wrapper() bertindak sebagai "pembungkus" yang menambahkan perilaku sebelum dan setelah eksekusi dari fungsi func.
Setelah itu, fungsi  my_decorator mengembalikan (return) fungsi wrapper sebagai hasilnya. Return ini juga menyebabkan fungsi wrapper dijalankan.
Kemudian, kita mendefinisikan fungsi say_hello(). Fungsi ini akan menjadi target dekorasi.
Untuk mendekorasi say_hello(), kita menggunakan simbol "@" diikuti dengan nama dekorator, yaitu @my_decorator sebelum mendefinisikan fungsi say_hello.
Jadi, secara alur, ketika fungsi say_hello() dipanggil, sebenarnya yang dieksekusi adalah fungsi wrapper() yang menjadi hasil dari dekorasi. Oleh karena itu, pesan "Sebelum fungsi dieksekusi." dicetak terlebih dahulu, kemudian fungsi say_hello() dieksekusi dan mencetak "Hello, world!", lalu akhirnya, pesan "Setelah fungsi dieksekusi." dicetak.
Dekorator sangat berguna untuk menambahkan fungsionalitas tambahan pada suatu fungsi atau metode tanpa harus mengubah kode asli dari fungsi tersebut. Anda bisa membaca lebih dalam mengenai dekorator pada laman ini.

Metode dari Objek (Object Method)
Jenis pertama adalah method yang melekat terhadap objek. Ciri dari jenis metode ini adalah adanya parameter self yang merujuk pada objek saat ini. Perhatikan contoh di bawah ini, asumsikan bahwa kita membuat kelas mobil yang sama seperti sebelumnya. Namun, kita menambahkan metode bernama "tambah_kecepatan" dan setiap metode ini dipanggil maka kecepatan mobil akan bertambah 10.
"""

class Mobil():
    def __init__ (self,warna,merek,kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("HITAM","SAMSUNG",190)
print("sebelum di tambahkan : ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()

print("setelah menambahkan kecepatan:")
print(mobil_1.kecepatan)
"""
Pada contoh di atas, kita membuat kelas Mobil dan mengimplementasikannya pada objek bernama "mobil_1". Dalam kelas tersebut, kita memiliki constructor ('__init__') yang digunakan untuk menginisialisasi atribut 'warna', 'merek' dan 'kecepatan' pada objek yang dibuat (mobil_1).

Ketika objek 'mobil_1' dibuat dari kelas Mobil, kita memberikan beberapa argumen yang menjadikannya atribut dari objek tersebut, yakni 'Merah' sebagai warna mobil, 'DicodingCar' sebagai merek, dan 'kecepatan' sebagai kecepatan awal mobil tersebut.

Dalam kelas Mobil yang dibuat, kita menambahkan method berupa fungsi "tambah_kecepatan" dan digunakan untuk meningkatkan kecepatan mobil. Setiap metode ini dipanggil, kecepatan mobil akan bertambah sebesar 10.

Pada bagian kode berikut lebih tepatnya, kita memanggil metode yang telah dibuat tersebut.

Hasilnya bisa kita lihat pada output dalam program tersebut, bahwa sebelum ditambahkan, kecepatannya adalah 160. Namun setelah itu, kecepatannya bertambah menjadi 170.

Jika menyadarinya, perbedaan ketika Anda memanggil method dan atribut terletak pada penempatan tanda kurung “()”. Ketika memanggil atribut, Anda cukup menyebutkan nama atribut tersebut tanpa ada tanda kurung “()”, contohnya “mobil_1.kecepatan”. Namun untuk memanggil method, Anda harus menempatkan tanda kurung “()” setelahnya, contohnya “mobil_1.tambah_kecepatan()”.

Selain itu, saat kode di bawah ini dieksekusi,

Namun, object method adalah metode yang melekat terhadap suatu objek dan menggunakan parameter self. Jadi, kita tidak bisa memanggil metode ini langsung melalui kelasnya.

"""

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10
        
Mobil.tambah_kecepatan()
"""
Pada contoh di atas, kita perlu membuat kelas yang sama seperti sebelumnya. Namun kali ini, kita memanggil object method melalui kelasnya secara langsung. Hal ini menyebabkan error karena kita mendefinisikan fungsi tambah_kecepatan sebagai object method. Artinya, metode ini memerlukan parameter self dan merujuk pada objek yang dibuat, sedangkan kita memanggilnya melalui kelas tanpa membuat objek.

Jika ingin membuat metode yang tidak melekat pada objek, kita bisa menggunakan class method atau static method.

Metode secara Statis (Static Method)
Static method adalah fungsi atau method pada sebuah kelas yang bersifat statis. Artinya, metode atau fungsi ini bersifat independen dan tidak terikat pada instance kelas. Metode ini dapat dianggap seperti kita membuat fungsi seperti biasa, tetapi didefinisikan dalam kelas sehingga ini menjadi perilaku untuk kelas tersebut. Untuk membuat static method, Anda bisa menambahkan dekorator @staticmethod tepat sebelum mendefinisikan fungsi atau metode.


"""

class Mobil():
    def __init__(self,merek):
        self.merek = merek

    @staticmethod
    def intro_mobil():
        print("ini adalh metode dari class mobil")

Mobil.intro_mobil()
mobil_1 = Mobil("SAMSUG")
mobil_1.intro_mobil()
"""
Metode dari Kelas (Class Method)
Metode terakhir adalah class method yang termasuk jenis metode cukup spesial dalam Python. Jika object method identik dengan parameter self yang merujuk pada objek, class method juga memerlukan sebuah parameter yang merujuk pada kelas. Mari buat contoh yang sama dengan sebelumnya, tetapi kali ini menggunakan class method.
"""

class Mobil:
    def __init__(self,merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):
        print("ini adalah metode dari clas mobil")

Mobil.intro_mobil()
mobil_1 = Mobil("SAMSUG")
mobil_1.intro_mobil()

"""
perbedaan, yakni dekorator @classmethod digunakan. Perhatikan baik-baik pada bagian kode berikut.

@classmethod
def intro_mobil(cls):
    print("Ini adalah metode dari kelas Mobil")

Pada bagian fungsi intro_mobil, kita menambahkan parameter cls. Ini adalah parameter wajib dalam menggunakan dekorator @classmethod.

Catatan:
Penamaan cls merupakan kesepakatan bersama dari programmer Python untuk memudahkan pembacaan kode. Anda dapat mengganti namanya, tidak harus cls.

Mengapa demikian? Sebab, ketika menggunakan class method, kita akan menambahkan argumen tambahan pada posisi pertama berupa kelas itu sendiri. Perhatikan kode berikut.
"""

class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(*args):
        print(args)
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()
"""
Pada contoh kode di atas, fungsi intro_mobil() menggunakan variadic positional parameter, yakni *args untuk melihat argumen yang diterima oleh fungsi tersebut. Perhatikan lebih baik output-nya, kode di atas menerima sebuah parameter, yakni kelas Mobil walaupun ketika pemanggilan fungsi intro_mobil() kita tidak memberikan argumen apa pun. 

Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

Ini membuktikan bahwa ketika Anda menggunakan class method, Python akan secara otomatis menambahkan kelas tersebut sebagai argumen pertama.
"""