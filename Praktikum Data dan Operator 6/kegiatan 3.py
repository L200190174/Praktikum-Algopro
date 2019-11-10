Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Labib Majid'
>>> NIM = 'L200190174'
>>> X = '1' + NIM[7:]
>>> a = int(x)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a = int(x)
NameError: name 'x' is not defined
>>> a = int(X)
>>> b = len(Nama)
>>> 
>>> type(a)
<class 'int'>
>>> #type berarti perintah untuk mendifinisikan tipe tersebut
>>> #bahwa tipe tersebut berupa integer
>>> 
>>> type(b)
<class 'int'>
>>> #berarti tipe dari data tersebut adalah integer
>>> 
>>> a / b
106.72727272727273
>>> #perintah diatas menampilkan pembagian dari nilai X dengan jumlah pada Nama
>>> 
>>> a // b
106
>>> #perintah diatas menampilkan hasil pembagian yang dibulatkan pada nilai X dan jumlah jumlah pada Nama
>>> 
>>> 10 * (a - 999)
1750
>>> #perintah diatas menampilkan operasi bilangan nilai a yaitu 1174 kemudian dikurangi 999 dan dikali 10
>>> 
>>> b ** 2
121
>>> #perintah diatas menampilkan nilai b yaitu 11 dipangkatkan dengan 2
>>> 
>>> a % b
8
>>> #perintah diatas menampilkan sisa pembagian dari nilai a dan b
>>> 
>>> c = 12.5
>>> 
>>> type(c)
<class 'float'>
>>> #perintah diatas menampilkan jenis dari type data dari c. float, yaitu bilangan pecahan
>>> 
>>> a / c
93.92
>>> #perintah diatas menampilkan operasi pembagian dari nilai a yaitu 1174 dibagi dengan nilai c
>>> 
>>> a // c
93.0
>>> #perintah diatas menampilkan operasi pembagian yang dibulatkan dari nilai a dan dibagi nilai c
>>> 
>>> a % c
11.5
>>> 
>>> c > b
True
>>> #perintah diatas menampilkan operatot pebandingan antara nilai c dan b apakah nilai c lebih besar dari nilai b
>>> 
>>> type(c > b)
<class 'bool'>
>>> #printah diatas menampilkan kelas dari type data perbandingan
>>> 
>>> a > b and b > c
False
>>> #perintah diatas menampilkan false and false maka menghasilkan nilai false
>>> 
>>> a > 1100 or b < 10
True
>>> #perintah diatas menampilkan true or false maka hasilnya true 
